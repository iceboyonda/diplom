from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db import transaction
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.models import Cart
from tyres.models import TyreVariant, RimVariant

@login_required
def order_create(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.error(request, 'Ваша корзина пуста')
        return redirect('cart:cart_detail')
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # Проверяем наличие товаров на складе
                    for item in cart:
                        if item['type'] == 'tyre':
                            tyre = TyreVariant.objects.select_for_update().get(id=item['product'].id)
                            if tyre.stock < item['quantity']:
                                raise ValueError(f'Недостаточно товара на складе: {tyre.model.brand} {tyre.model.name}')
                        else:  # rim
                            rim = RimVariant.objects.select_for_update().get(id=item['product'].id)
                            if rim.stock < item['quantity']:
                                raise ValueError(f'Недостаточно товара на складе: {rim.model.brand} {rim.model.name}')

                    # Создаем заказ
                    order = form.save(commit=False)
                    order.user = request.user
                    order.save()
                    
                    # Создаем элементы заказа и обновляем остатки
                    for item in cart:
                        if item['type'] == 'tyre':
                            tyre = TyreVariant.objects.select_for_update().get(id=item['product'].id)
                            OrderItem.objects.create(
                                order=order,
                                tyre=tyre,
                                price=item['price'],
                                quantity=item['quantity']
                            )
                            tyre.stock -= item['quantity']
                            tyre.save()
                        else:  # rim
                            rim = RimVariant.objects.select_for_update().get(id=item['product'].id)
                            OrderItem.objects.create(
                                order=order,
                                rim=rim,
                                price=item['price'],
                                quantity=item['quantity']
                            )
                            rim.stock -= item['quantity']
                            rim.save()
                    
                    # Очищаем корзину
                    cart.clear()
                    messages.success(request, 'Заказ успешно оформлен')
                    return redirect('orders:order_detail', order_id=order.id)
            except ValueError as e:
                messages.error(request, str(e))
            except Exception as e:
                messages.error(request, 'Произошла ошибка при создании заказа. Пожалуйста, попробуйте позже.')
                # Здесь можно добавить логирование ошибки
    else:
        # Предзаполняем форму данными пользователя
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
        form = OrderCreateForm(initial=initial_data)
    
    return render(request, 'orders/create.html', {
        'cart': cart,
        'form': form
    })

@login_required
def order_list(request):
    orders = request.user.orders.all().prefetch_related(
        'items__tyre__model',
        'items__rim__model'
    )
    return render(request, 'orders/list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(request.user.orders.prefetch_related('items__tyre__model', 'items__rim__model'), id=order_id)
    return render(request, 'orders/detail.html', {'order': order})

@login_required
def order_receipt(request, order_id):
    """
    Простой чек заказа в HTML формате.
    Открывается в новом окне браузера.
    """
    order = get_object_or_404(request.user.orders.prefetch_related('items__tyre__model', 'items__rim__model'), id=order_id)
    return render(request, 'orders/receipt.html', {'order': order})

@user_passes_test(lambda u: u.is_staff)
def admin_orders(request):
    orders = Order.objects.all().select_related('user')
    return render(request, 'orders/admin_orders.html', {'orders': orders})

@user_passes_test(lambda u: u.is_staff)
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order.objects.select_related('user'), id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status and new_status != order.status:
            order.status = new_status
            order.save()
    return render(request, 'orders/admin_order_detail.html', {'order': order})

@user_passes_test(lambda u: u.is_staff)
def admin_order_delete(request, order_id):
    order = get_object_or_404(Order.objects.select_related('user'), id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('orders:admin_orders')
    return render(request, 'orders/admin_order_delete.html', {'order': order}) 