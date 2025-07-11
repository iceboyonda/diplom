from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from tyres.models import TyreVariant, RimVariant
from .models import Cart

@require_POST
def cart_add(request, tyre_id):
    cart = Cart(request)
    tyre = get_object_or_404(TyreVariant, id=tyre_id)
    quantity_str = request.POST.get('quantity', '').strip()
    try:
        quantity = int(quantity_str)
        if quantity < 1:
            quantity = 1
    except (ValueError, TypeError):
        quantity = 1
    update_quantity = request.POST.get('update_quantity') == 'true' or quantity > 1
    
    if quantity > tyre.stock:
        messages.error(request, f'К сожалению, на складе только {tyre.stock} шт.')
        return redirect('tyres:tyre_detail', tyre_id=tyre.tyre_model.id)
    
    cart.add(tyre=tyre, quantity=quantity, update_quantity=update_quantity)
    messages.success(request, 'Товар добавлен в корзину')
    return redirect('cart:cart_detail')

def cart_remove(request, tyre_id):
    cart = Cart(request)
    tyre = get_object_or_404(TyreVariant, id=tyre_id)
    cart.remove(tyre=tyre)
    messages.success(request, 'Товар удален из корзины')
    if request.headers.get('HX-Request') == 'true':
        return render(request, 'cart/_cart_table.html', {'cart': cart})
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def cart_update(request, tyre_id):
    cart = Cart(request)
    tyre = get_object_or_404(TyreVariant, id=tyre_id)
    quantity_str = request.POST.get('quantity', '').strip()
    try:
        quantity = int(quantity_str)
        if quantity < 1:
            quantity = 1
    except (ValueError, TypeError):
        quantity = 1
    
    if quantity > tyre.stock:
        messages.error(request, f'К сожалению, на складе только {tyre.stock} шт.')
    else:
        cart.add(tyre=tyre, quantity=quantity, update_quantity=True)
        messages.success(request, 'Количество товара обновлено')
    
    if request.headers.get('HX-Request') == 'true':
        return render(request, 'cart/_cart_table.html', {'cart': cart})
    return redirect('cart:cart_detail')

@require_POST
def cart_add_rim(request, rim_variant_id):
    cart = Cart(request)
    rim_variant = get_object_or_404(RimVariant, id=rim_variant_id)
    quantity_str = request.POST.get('quantity', '').strip()
    try:
        quantity = int(quantity_str)
        if quantity < 1:
            quantity = 1
    except (ValueError, TypeError):
        quantity = 1
    update_quantity = request.POST.get('update_quantity') == 'true' or quantity > 1

    if quantity > rim_variant.stock:
        messages.error(request, f'К сожалению, на складе только {rim_variant.stock} шт.')
        return redirect('tyres:rim_detail', rim_id=rim_variant.model.id)

    cart.add(rim=rim_variant, quantity=quantity, update_quantity=update_quantity)
    messages.success(request, 'Диск добавлен в корзину')
    return redirect('cart:cart_detail')

def cart_remove_rim(request, rim_variant_id):
    cart = Cart(request)
    rim_variant = get_object_or_404(RimVariant, id=rim_variant_id)
    cart.remove(rim=rim_variant)
    messages.success(request, 'Диск удален из корзины')
    if request.headers.get('HX-Request') == 'true':
        return render(request, 'cart/_cart_table.html', {'cart': cart})
    return redirect('cart:cart_detail')

def cart_update_rim(request, rim_variant_id):
    cart = Cart(request)
    rim_variant = get_object_or_404(RimVariant, id=rim_variant_id)
    quantity_str = request.POST.get('quantity', '').strip()
    try:
        quantity = int(quantity_str)
        if quantity < 1:
            quantity = 1
    except (ValueError, TypeError):
        quantity = 1

    if quantity > rim_variant.stock:
        messages.error(request, f'К сожалению, на складе только {rim_variant.stock} шт.')
    else:
        cart.add(rim=rim_variant, quantity=quantity, update_quantity=True)
        messages.success(request, 'Количество дисков обновлено')

    if request.headers.get('HX-Request') == 'true':
        return render(request, 'cart/_cart_table.html', {'cart': cart})
    return redirect('cart:cart_detail')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, 'Корзина полностью очищена!')
    return redirect('cart:cart_detail') 