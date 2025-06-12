from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Prefetch, Min, Max
from django.db.models.functions import Lower
from .models import TyreModel, TyreVariant, Favourite, RimModel, RimVariant, FavouriteRim
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from urllib.parse import urlencode
from .forms import TyreModelForm, TyreVariantFormSet, RimModelForm, RimVariantFormSet
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
from django.template.loader import render_to_string
from django.core.files.storage import default_storage

def annotate_tyres(tyres):
    for tyre_model in tyres:
        variants = tyre_model.variants.all()
        
        radiuses = sorted(list(set(v.radius for v in variants if v.radius is not None)))
        tyre_model.radius_range = ', '.join(f'R{r}' for r in radiuses) if radiuses else '—'

        prices = [v.price for v in variants if v.price is not None]
        tyre_model.min_price = min(prices) if prices else None

        seasons = sorted(list(set(v.get_season_display() for v in variants)))
        tyre_model.season_display = ', '.join(seasons) if seasons else '—'
    return tyres

def annotate_rims(rims):
    for rim in rims:
        variants = list(rim.variants.all())
        # Диапазон диаметров и ширин
        diameters = sorted(list(set(v.diameter for v in variants if v.diameter is not None)))
        widths = sorted(list(set(v.width for v in variants if v.width is not None)))
        bolt_patterns_list = sorted(list(set(v.bolt_pattern for v in variants if v.bolt_pattern is not None and v.bolt_pattern != '')))
        
        rim.diameter_display = ', '.join(str(d) for d in diameters) if diameters else '—'
        rim.width_display = ', '.join(str(w) for w in widths) if widths else '—'
        rim.bolt_patterns_display = ', '.join(bolt_patterns_list) if bolt_patterns_list else '—'

        # Минимальная цена
        prices = [v.price for v in variants if v.price is not None]
        rim.min_price = min(prices) if prices else None
    return rims

@cache_page(60 * 15)  # Кэширование на 15 минут
def catalogue(request):
    tyres = TyreModel.objects.prefetch_related(
        Prefetch('variants', queryset=TyreVariant.objects.select_related('model'))
    ).all()
    
    # Применяем фильтры
    brand = request.GET.get('brand')
    if brand:
        tyres = tyres.filter(brand__icontains=brand)
    
    season = request.GET.get('season')
    if season:
        tyres = tyres.filter(variants__season=season).distinct()
    
    width = request.GET.get('width')
    if width:
        tyres = tyres.filter(variants__width=width).distinct()
    
    profile = request.GET.get('profile')
    if profile:
        tyres = tyres.filter(variants__profile=profile).distinct()
    
    radius = request.GET.get('radius')
    if radius:
        tyres = tyres.filter(variants__radius=radius).distinct()
    
    min_price = request.GET.get('min_price')
    if min_price:
        tyres = tyres.filter(variants__price__gte=min_price).distinct()

    max_price = request.GET.get('max_price')
    if max_price:
        tyres = tyres.filter(variants__price__lte=max_price).distinct()
    
    # Сортировка
    sort = request.GET.get('sort', 'name')
    if sort == 'price_asc':
        tyres = tyres.annotate(min_price=models.Min('variants__price')).order_by('min_price')
    elif sort == 'price_desc':
        tyres = tyres.annotate(min_price=models.Min('variants__price')).order_by('-min_price')
    else:
        tyres = tyres.order_by(Lower('brand'), Lower('name'))
    
    # Пагинация
    paginator = Paginator(tyres, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Аннотации для отображения
    annotated_tyres = annotate_tyres(page_obj.object_list)

    # Создаем query_string без параметра page
    query_params = request.GET.dict()
    if 'page' in query_params:
        del query_params['page']
    query_string = urlencode(query_params)
    if query_string:
        query_string = '&' + query_string
    
    context = {
        'tyres': annotated_tyres,
        'page_obj': page_obj,
        'brands': TyreModel.objects.values_list('brand', flat=True).distinct().order_by('brand'),
        'seasons': TyreVariant.SEASON_CHOICES,
        'widths': TyreVariant.objects.values_list('width', flat=True).distinct().order_by('width'),
        'profiles': TyreVariant.objects.values_list('profile', flat=True).distinct().order_by('profile'),
        'radiuses': TyreVariant.objects.values_list('radius', flat=True).distinct().order_by('radius'),
        'selected_brand': brand,
        'selected_season': season,
        'selected_width': width,
        'selected_profile': profile,
        'selected_radius': radius,
        'min_price': min_price,
        'max_price': max_price,
        'current_sort': sort,
        'query_string': query_string,
    }
    
    return render(request, 'tyres/catalogue.html', context)

@cache_page(60 * 15)  # Кэширование на 15 минут
def tyre_detail(request, tyre_id):
    tyre = get_object_or_404(
        TyreModel.objects.prefetch_related(
            Prefetch('variants', queryset=TyreVariant.objects.select_related('model'))
        ),
        id=tyre_id
    )
    variants = tyre.variants.all()
    widths = sorted(set(v.width for v in variants))
    profiles = sorted(set(v.profile for v in variants))
    radiuses = sorted(set(v.radius for v in variants))
    speed_indexes = sorted(set(v.speed_index for v in variants))
    seasons = sorted(set(v.get_season_display() for v in variants))
    studded = any(v.studded for v in variants)
    favourite_ids = []
    if request.user.is_authenticated:
        favourite_ids = list(Favourite.objects.filter(
            user=request.user,
            variant__model=tyre
        ).values_list('variant__id', flat=True))
    return render(request, 'tyres/tyre_detail.html', {
        'tyre': tyre,
        'variants': variants,
        'widths': widths,
        'profiles': profiles,
        'radiuses': radiuses,
        'speed_indexes': speed_indexes,
        'seasons': seasons,
        'studded': studded,
        'favourite_ids': favourite_ids,
    })

def search_tyres(request):
    query = request.GET.get('q')
    if query:
        tyres = TyreModel.objects.filter(
            Q(name__icontains=query) |\
            Q(brand__icontains=query) |\
            Q(description__icontains=query)
        )
    else:
        tyres = TyreModel.objects.all()
    
    annotate_tyres(tyres) # Аннотируем результаты поиска шин
    
    return render(request, 'tyres/catalogue.html', {'tyres': tyres, 'query': query}) # Возвращаем на страницу каталога шин

def faq(request):
    return render(request, 'tyres/faq.html')

@require_POST
@login_required
def add_to_favourites(request, variant_id):
    variant = get_object_or_404(TyreVariant, id=variant_id)
    favourite, created = Favourite.objects.get_or_create(user=request.user, variant=variant)
    
    if request.headers.get('HX-Request'):
        html = render_to_string('tyres/_favourite_button.html', {
            'variant': variant,
            'favourite_ids': [variant.id]
        }, request=request)
        return HttpResponse(html)
    return JsonResponse({'status': 'success'})

@require_POST
@login_required
def remove_from_favourites(request, variant_id):
    Favourite.objects.filter(user=request.user, variant_id=variant_id).delete()
    
    if request.headers.get('HX-Request'):
        variant = get_object_or_404(TyreVariant, id=variant_id)
        html = render_to_string('tyres/_favourite_button.html', {
            'variant': variant,
            'favourite_ids': []
        }, request=request)
        return HttpResponse(html)
    return JsonResponse({'status': 'success'})

@require_POST
@login_required
def add_rim_to_favourites(request, rim_variant_id):
    rim_variant = get_object_or_404(RimVariant, id=rim_variant_id)
    favourite, created = FavouriteRim.objects.get_or_create(user=request.user, rim_variant=rim_variant)
    
    if request.headers.get('HX-Request'):
        html = render_to_string('tyres/_favourite_rim_button.html', {
            'rim_variant': rim_variant,
            'favourite_rim_ids': [rim_variant.id]
        }, request=request)
        return HttpResponse(html)
    return JsonResponse({'status': 'success'})

@require_POST
@login_required
def remove_rim_from_favourites(request, rim_variant_id):
    FavouriteRim.objects.filter(user=request.user, rim_variant_id=rim_variant_id).delete()
    
    if request.headers.get('HX-Request'):
        rim_variant = get_object_or_404(RimVariant, id=rim_variant_id)
        html = render_to_string('tyres/_favourite_rim_button.html', {
            'rim_variant': rim_variant,
            'favourite_rim_ids': []
        }, request=request)
        return HttpResponse(html)
    return JsonResponse({'status': 'success'})

@login_required
def favourites(request):
    tyre_favourites = TyreVariant.objects.filter(
        favourited_by__user=request.user
    ).select_related('model')
    
    rim_favourites = RimVariant.objects.filter(
        favourited_by_rims__user=request.user
    ).select_related('model')
    
    context = {
        'tyre_favourites': tyre_favourites,
        'rim_favourites': rim_favourites,
    }
    return render(request, 'tyres/favourites.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_tyres(request):
    tyres = TyreModel.objects.prefetch_related(
        Prefetch('variants', queryset=TyreVariant.objects.select_related('model'))
    ).all()
    
    # Применяем фильтры
    brand = request.GET.get('brand')
    if brand:
        tyres = tyres.filter(brand__icontains=brand)
    
    query = request.GET.get('q')
    if query:
        tyres = tyres.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query) |
            Q(description__icontains=query)
        )
    
    # Сортировка
    sort = request.GET.get('sort', 'name')
    if sort == 'price_asc':
        tyres = tyres.annotate(min_price=models.Min('variants__price')).order_by('min_price')
    elif sort == 'price_desc':
        tyres = tyres.annotate(min_price=models.Min('variants__price')).order_by('-min_price')
    else:
        tyres = tyres.order_by(Lower('brand'), Lower('name'))
    
    # Пагинация
    paginator = Paginator(tyres, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Аннотации для отображения
    tyres = annotate_tyres(page_obj)
    
    context = {
        'tyres': tyres,
        'page_obj': page_obj,
        'brands': TyreModel.objects.values_list('brand', flat=True).distinct().order_by('brand'),
    }
    return render(request, 'tyres/admin_tyres.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_tyre_add(request):
    if request.method == 'POST':
        form = TyreModelForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the main tyre model
            tyre = form.save(commit=False)
            
            # Get the release year if provided
            release_year = request.POST.get('release_year')
            if release_year and release_year.strip():
                tyre.release_year = int(release_year)
            
            tyre.save()
            
            # Process the variants
            variant_sizes = request.POST.getlist('variant_size[]')
            variant_seasons = request.POST.getlist('variant_season[]')
            variant_studded = request.POST.getlist('variant_studded[]')
            variant_speed_indices = request.POST.getlist('variant_speed_index[]')
            variant_prices = request.POST.getlist('variant_price[]')
            variant_stocks = request.POST.getlist('variant_stock[]')
            
            # Create variants
            for i in range(len(variant_sizes)):
                if not variant_sizes[i]:  # Skip empty rows
                    continue
                
                # Parse size (format: 195/65 R15)
                try:
                    size_parts = variant_sizes[i].strip().split('/')
                    if len(size_parts) != 2:
                        continue
                    
                    width = int(size_parts[0])
                    
                    # Handle the profile and radius part (e.g., "65 R15")
                    profile_radius = size_parts[1].strip().split(' ')
                    if len(profile_radius) == 2:
                        profile = int(profile_radius[0])
                        # Remove 'R' from radius if present
                        radius = int(profile_radius[1].replace('R', ''))
                    else:
                        # Try to handle format like "65R15"
                        import re
                        match = re.match(r'(\d+)R(\d+)', size_parts[1])
                        if match:
                            profile = int(match.group(1))
                            radius = int(match.group(2))
                        else:
                            continue
                    
                    # Create the variant
                    variant = TyreVariant(
                        model=tyre,
                        width=width,
                        profile=profile,
                        radius=radius,
                        season=variant_seasons[i],
                        studded=variant_studded[i] == 'true',
                        speed_index=variant_speed_indices[i],
                        price=float(variant_prices[i]) if variant_prices[i] else 0,
                        stock=int(variant_stocks[i]) if variant_stocks[i] else 0
                    )
                    variant.save()
                except (ValueError, IndexError) as e:
                    messages.error(request, f'Ошибка при обработке размера: {variant_sizes[i]}. Проверьте формат (например: 195/65 R15)')
                    continue
            
            messages.success(request, 'Шина успешно добавлена')
            return redirect('tyres:admin_tyres')
    else:
        form = TyreModelForm()
    return render(request, 'tyres/admin/tyre_form.html', {'form': form, 'title': 'Добавить шину'})

@user_passes_test(lambda u: u.is_staff)
def admin_tyre_edit(request, tyre_id):
    tyre = get_object_or_404(TyreModel, id=tyre_id)
    if request.method == 'POST':
        form = TyreModelForm(request.POST, request.FILES, instance=tyre)
        if form.is_valid():
            try:
                # Проверяем, было ли загружено новое изображение
                if 'image' in request.FILES:
                    # Если старое изображение существует и это не изображение по умолчанию, удаляем его
                    if tyre.image and tyre.image.name != 'tyres/default_tyre.jpg' and default_storage.exists(tyre.image.name):
                        default_storage.delete(tyre.image.name)
                
                # Сохраняем форму
                tyre_instance = form.save(commit=False)
                
                # Если был указан год выпуска
                release_year = request.POST.get('release_year')
                if release_year and release_year.strip():
                    tyre_instance.release_year = int(release_year)
                
                tyre_instance.save()
                messages.success(request, 'Шина успешно обновлена')
                return redirect('tyres:admin_tyres')
            except Exception as e:
                messages.error(request, f'Ошибка при сохранении: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Ошибка в поле '{field}': {error}")
    else:
        form = TyreModelForm(instance=tyre)
    
    return render(request, 'tyres/admin/tyre_form.html', {
        'form': form, 
        'title': 'Редактировать шину',
        'tyre': tyre
    })

@user_passes_test(lambda u: u.is_staff)
def admin_tyre_delete(request, tyre_id):
    tyre = get_object_or_404(TyreModel, id=tyre_id)
    if request.method == 'POST':
        tyre.delete()
        messages.success(request, 'Шина успешно удалена.')
        return redirect('tyres:admin_tyres')
    return render(request, 'tyres/admin_tyre_delete.html', {'tyre': tyre})

@user_passes_test(lambda u: u.is_staff)
def admin_categories(request):
    return render(request, 'tyres/admin_categories.html')

@cache_page(60 * 15)  # Кэширование на 15 минут
def rim_list(request):
    # Получаем все диски и применяем фильтры
    rims = RimModel.objects.all().prefetch_related('variants')
    
    # Фильтрация
    brand = request.GET.get('brand')
    if brand:
        rims = rims.filter(brand=brand)
    
    diameter = request.GET.get('diameter')
    if diameter:
        rims = rims.filter(variants__diameter=float(diameter))
    
    width = request.GET.get('width')
    if width:
        rims = rims.filter(variants__width=float(width))
    
    bolt_pattern = request.GET.get('bolt_pattern')
    if bolt_pattern:
        rims = rims.filter(variants__bolt_pattern=bolt_pattern)
    
    material = request.GET.get('material')
    if material:
        rims = rims.filter(variants__material=material)
    
    color = request.GET.get('color')
    if color:
        rims = rims.filter(variants__color=color)
    
    min_price = request.GET.get('min_price')
    if min_price:
        rims = rims.filter(variants__price__gte=float(min_price))
    
    max_price = request.GET.get('max_price')
    if max_price:
        rims = rims.filter(variants__price__lte=float(max_price))
    
    # Сортировка
    sort = request.GET.get('sort', 'name')
    if sort == 'price_asc':
        rims = rims.order_by('variants__price')
    elif sort == 'price_desc':
        rims = rims.order_by('-variants__price')
    else:
        rims = rims.order_by('brand', 'name')
    
    # Удаляем дубликаты, которые могли появиться из-за связи с вариантами
    rims = rims.distinct()
    
    # Аннотируем диски дополнительной информацией
    rims = annotate_rims(rims)
    
    # Пагинация
    paginator = Paginator(rims, 9)  # 9 дисков на странице
    page = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    
    # Получаем доступные значения для фильтров
    brands = RimModel.objects.values_list('brand', flat=True).distinct()
    available_diameters = RimVariant.objects.values_list('diameter', flat=True).distinct()
    available_widths = RimVariant.objects.values_list('width', flat=True).distinct()
    available_bolt_patterns = RimVariant.objects.values_list('bolt_pattern', flat=True).distinct()
    materials = RimVariant.objects.values_list('material', flat=True).distinct()
    colors = RimVariant.objects.values_list('color', flat=True).distinct()
    
    # Формируем строку запроса для пагинации
    query_params = request.GET.copy()
    if 'page' in query_params:
        del query_params['page']
    query_string = '&' + query_params.urlencode() if query_params else ''
    
    context = {
        'page_obj': page_obj,
        'brands': brands,
        'available_diameters': available_diameters,
        'available_widths': available_widths,
        'available_bolt_patterns': available_bolt_patterns,
        'materials': materials,
        'colors': colors,
        'selected_brand': brand,
        'selected_diameter': diameter,
        'selected_width': width,
        'selected_bolt_pattern': bolt_pattern,
        'selected_material': material,
        'selected_color': color,
        'min_price': min_price,
        'max_price': max_price,
        'current_sort': sort,
        'query_string': query_string,
    }
    
    return render(request, 'tyres/rim_list.html', context)

@cache_page(60 * 15)  # Кэширование на 15 минут
def rim_detail(request, rim_id):
    rim = get_object_or_404(
        RimModel.objects.prefetch_related(
            Prefetch('variants', queryset=RimVariant.objects.select_related('model'))
        ),
        id=rim_id
    )
    variants = rim.variants.all()
    diameters = sorted(set(v.diameter for v in variants))
    widths = sorted(set(v.width for v in variants))
    bolt_patterns = sorted(set(v.bolt_pattern for v in variants))
    offsets = sorted(list(set(v.offset for v in variants if v.offset)))
    dias = sorted(list(set(v.dia for v in variants if v.dia)))
    colors = sorted(list(set(v.color for v in variants if v.color)))
    materials = sorted(list(set(v.material for v in variants if v.material)))
    favourite_rim_ids = []
    if request.user.is_authenticated:
        favourite_rim_ids = list(FavouriteRim.objects.filter(
            user=request.user,
            rim_variant__model=rim
        ).values_list('rim_variant_id', flat=True))
    return render(request, 'tyres/rim_detail.html', {
        'rim': rim,
        'variants': variants,
        'diameters': diameters,
        'widths': widths,
        'bolt_patterns': bolt_patterns,
        'offsets': offsets,
        'dias': dias,
        'colors': colors,
        'materials': materials,
        'favourite_rim_ids': favourite_rim_ids,
    })

@user_passes_test(lambda u: u.is_staff)
def admin_rims(request):
    rims = RimModel.objects.prefetch_related(
        Prefetch('variants', queryset=RimVariant.objects.select_related('model'))
    ).all()
    
    # Применяем фильтры
    brand = request.GET.get('brand')
    if brand:
        rims = rims.filter(brand__icontains=brand)
    
    query = request.GET.get('q')
    if query:
        rims = rims.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query) |
            Q(description__icontains=query)
        )
    
    # Сортировка
    sort = request.GET.get('sort', 'name')
    if sort == 'price_asc':
        rims = rims.annotate(min_price=models.Min('variants__price')).order_by('min_price')
    elif sort == 'price_desc':
        rims = rims.annotate(min_price=models.Min('variants__price')).order_by('-min_price')
    else:
        rims = rims.order_by(Lower('brand'), Lower('name'))
    
    # Пагинация
    paginator = Paginator(rims, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Аннотации для отображения
    rims = annotate_rims(page_obj)
    
    context = {
        'rims': rims,
        'page_obj': page_obj,
        'brands': RimModel.objects.values_list('brand', flat=True).distinct().order_by('brand'),
    }
    return render(request, 'tyres/admin_rims.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_rim_add(request):
    if request.method == 'POST':
        form = RimModelForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the main rim model
            rim = form.save(commit=False)
            
            # Get the release year if provided
            release_year = request.POST.get('release_year')
            if release_year and release_year.strip():
                rim.release_year = int(release_year)
            
            rim.save()
            
            # Process the variants
            variant_sizes = request.POST.getlist('variant_size[]')
            variant_offsets = request.POST.getlist('variant_offset[]')
            variant_dias = request.POST.getlist('variant_dia[]')
            variant_colors = request.POST.getlist('variant_color[]')
            variant_materials = request.POST.getlist('variant_material[]')
            variant_prices = request.POST.getlist('variant_price[]')
            variant_stocks = request.POST.getlist('variant_stock[]')
            variant_images = request.FILES.getlist('variant_image[]')
            
            # Create variants
            for i in range(len(variant_sizes)):
                if not variant_sizes[i]:  # Skip empty rows
                    continue
                
                # Parse size (format: 16.0x7.0 5x100)
                try:
                    # Split by space to separate dimensions from bolt pattern
                    size_parts = variant_sizes[i].strip().split(' ')
                    if len(size_parts) < 2:
                        continue
                    
                    # Parse dimensions (e.g., "16.0x7.0")
                    dimensions = size_parts[0].split('x')
                    if len(dimensions) != 2:
                        continue
                    
                    diameter = float(dimensions[0])
                    width = float(dimensions[1])
                    
                    # Get bolt pattern (e.g., "5x100")
                    bolt_pattern = size_parts[1]
                    
                    # Parse offset (e.g., "ET40" -> "40")
                    offset = variant_offsets[i].replace('ET', '').strip() if variant_offsets[i] else ''
                    
                    # Create the variant
                    variant = RimVariant(
                        model=rim,
                        diameter=diameter,
                        width=width,
                        bolt_pattern=bolt_pattern,
                        offset=offset,
                        dia=variant_dias[i] if variant_dias[i] else '',
                        color=variant_colors[i],
                        material=variant_materials[i],
                        price=float(variant_prices[i]) if variant_prices[i] else 0,
                        stock=int(variant_stocks[i]) if variant_stocks[i] else 0
                    )
                    
                    # Handle image if available
                    if i < len(variant_images) and variant_images[i]:
                        variant.image = variant_images[i]
                        
                    variant.save()
                except (ValueError, IndexError) as e:
                    messages.error(request, f'Ошибка при обработке размера: {variant_sizes[i]}. Проверьте формат (например: 16.0x7.0 5x100)')
                    continue
            
            messages.success(request, 'Диск успешно добавлен')
            return redirect('tyres:admin_rims')
    else:
        form = RimModelForm()
    return render(request, 'tyres/admin/rim_form.html', {'form': form, 'title': 'Добавить диск'})

@user_passes_test(lambda u: u.is_staff)
def admin_rim_edit(request, rim_id):
    rim = get_object_or_404(RimModel, id=rim_id)
    if request.method == 'POST':
        form = RimModelForm(request.POST, request.FILES, instance=rim)
        if form.is_valid():
            try:
                # Проверяем, было ли загружено новое изображение
                if 'image' in request.FILES:
                    # Если старое изображение существует и это не изображение по умолчанию, удаляем его
                    if rim.image and rim.image.name != 'rims/default_rim.jpg' and default_storage.exists(rim.image.name):
                        default_storage.delete(rim.image.name)
                
                # Сохраняем форму
                rim_instance = form.save(commit=False)
                
                # Если был указан год выпуска
                release_year = request.POST.get('release_year')
                if release_year and release_year.strip():
                    rim_instance.release_year = int(release_year)
                
                rim_instance.save()
                messages.success(request, 'Диск успешно обновлен')
                return redirect('tyres:admin_rims')
            except Exception as e:
                messages.error(request, f'Ошибка при сохранении: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Ошибка в поле '{field}': {error}")
    else:
        form = RimModelForm(instance=rim)
    
    return render(request, 'tyres/admin/rim_form.html', {
        'form': form, 
        'title': 'Редактировать диск',
        'rim': rim
    })

@user_passes_test(lambda u: u.is_staff)
def admin_rim_delete(request, rim_id):
    rim = get_object_or_404(RimModel, id=rim_id)
    if request.method == 'POST':
        rim.delete()
        messages.success(request, 'Диск успешно удален.')
        return redirect('tyres:admin_rims')
    return render(request, 'tyres/admin_rim_delete.html', {'rim': rim})

@user_passes_test(lambda u: u.is_staff)
def add_tyre(request):
    if request.method == 'POST':
        form = TyreModelForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the main tyre model
            tyre = form.save(commit=False)
            
            # Get the release year if provided
            release_year = request.POST.get('release_year')
            if release_year and release_year.strip():
                tyre.release_year = int(release_year)
            
            tyre.save()
            
            # Process the variants
            variant_sizes = request.POST.getlist('variant_size[]')
            variant_seasons = request.POST.getlist('variant_season[]')
            variant_studded = request.POST.getlist('variant_studded[]')
            variant_speed_indices = request.POST.getlist('variant_speed_index[]')
            variant_prices = request.POST.getlist('variant_price[]')
            variant_stocks = request.POST.getlist('variant_stock[]')
            
            # Create variants
            for i in range(len(variant_sizes)):
                if not variant_sizes[i]:  # Skip empty rows
                    continue
                
                # Parse size (format: 195/65 R15)
                try:
                    size_parts = variant_sizes[i].strip().split('/')
                    if len(size_parts) != 2:
                        continue
                    
                    width = int(size_parts[0])
                    
                    # Handle the profile and radius part (e.g., "65 R15")
                    profile_radius = size_parts[1].strip().split(' ')
                    if len(profile_radius) == 2:
                        profile = int(profile_radius[0])
                        # Remove 'R' from radius if present
                        radius = int(profile_radius[1].replace('R', ''))
                    else:
                        # Try to handle format like "65R15"
                        import re
                        match = re.match(r'(\d+)R(\d+)', size_parts[1])
                        if match:
                            profile = int(match.group(1))
                            radius = int(match.group(2))
                        else:
                            continue
                    
                    # Create the variant
                    variant = TyreVariant(
                        model=tyre,
                        width=width,
                        profile=profile,
                        radius=radius,
                        season=variant_seasons[i],
                        studded=variant_studded[i] == 'true',
                        speed_index=variant_speed_indices[i],
                        price=float(variant_prices[i]) if variant_prices[i] else 0,
                        stock=int(variant_stocks[i]) if variant_stocks[i] else 0
                    )
                    variant.save()
                except (ValueError, IndexError) as e:
                    messages.error(request, f'Ошибка при обработке размера: {variant_sizes[i]}. Проверьте формат (например: 195/65 R15)')
                    continue
            
            messages.success(request, 'Шина успешно добавлена')
            return redirect('tyres:admin_tyres')
    else:
        form = TyreModelForm()
    return render(request, 'tyres/admin/tyre_form.html', {'form': form, 'title': 'Добавить шину'})

@user_passes_test(lambda u: u.is_staff)
def edit_tyre(request, tyre_id):
    tyre = get_object_or_404(TyreModel, id=tyre_id)
    if request.method == 'POST':
        form = TyreModelForm(request.POST, request.FILES, instance=tyre)
        if form.is_valid():
            try:
                # Проверяем, было ли загружено новое изображение
                if 'image' in request.FILES:
                    # Если старое изображение существует и это не изображение по умолчанию, удаляем его
                    if tyre.image and tyre.image.name != 'tyres/default_tyre.jpg' and default_storage.exists(tyre.image.name):
                        default_storage.delete(tyre.image.name)
                
                # Сохраняем форму
                tyre_instance = form.save(commit=False)
                
                # Если был указан год выпуска
                release_year = request.POST.get('release_year')
                if release_year and release_year.strip():
                    tyre_instance.release_year = int(release_year)
                
                tyre_instance.save()
                messages.success(request, 'Шина успешно обновлена')
                return redirect('tyres:admin_tyres')
            except Exception as e:
                messages.error(request, f'Ошибка при сохранении: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Ошибка в поле '{field}': {error}")
    else:
        form = TyreModelForm(instance=tyre)
    
    return render(request, 'tyres/admin/tyre_form.html', {
        'form': form, 
        'title': 'Редактировать шину',
        'tyre': tyre
    })

@user_passes_test(lambda u: u.is_staff)
def delete_tyre(request, tyre_id):
    tyre = get_object_or_404(TyreModel, id=tyre_id)
    if request.method == 'POST':
        tyre.delete()
        messages.success(request, 'Шина успешно удалена')
        return redirect('tyres:admin_tyres')
    return render(request, 'tyres/admin/tyre_confirm_delete.html', {'tyre': tyre})

@user_passes_test(lambda u: u.is_staff)
def add_rim(request):
    if request.method == 'POST':
        form = RimModelForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the main rim model
            rim = form.save(commit=False)
            
            # Get the release year if provided
            release_year = request.POST.get('release_year')
            if release_year and release_year.strip():
                rim.release_year = int(release_year)
            
            rim.save()
            
            # Process the variants
            variant_sizes = request.POST.getlist('variant_size[]')
            variant_offsets = request.POST.getlist('variant_offset[]')
            variant_dias = request.POST.getlist('variant_dia[]')
            variant_colors = request.POST.getlist('variant_color[]')
            variant_materials = request.POST.getlist('variant_material[]')
            variant_prices = request.POST.getlist('variant_price[]')
            variant_stocks = request.POST.getlist('variant_stock[]')
            variant_images = request.FILES.getlist('variant_image[]')
            
            # Create variants
            for i in range(len(variant_sizes)):
                if not variant_sizes[i]:  # Skip empty rows
                    continue
                
                # Parse size (format: 16.0x7.0 5x100)
                try:
                    # Split by space to separate dimensions from bolt pattern
                    size_parts = variant_sizes[i].strip().split(' ')
                    if len(size_parts) < 2:
                        continue
                    
                    # Parse dimensions (e.g., "16.0x7.0")
                    dimensions = size_parts[0].split('x')
                    if len(dimensions) != 2:
                        continue
                    
                    diameter = float(dimensions[0])
                    width = float(dimensions[1])
                    
                    # Get bolt pattern (e.g., "5x100")
                    bolt_pattern = size_parts[1]
                    
                    # Parse offset (e.g., "ET40" -> "40")
                    offset = variant_offsets[i].replace('ET', '').strip() if variant_offsets[i] else ''
                    
                    # Create the variant
                    variant = RimVariant(
                        model=rim,
                        diameter=diameter,
                        width=width,
                        bolt_pattern=bolt_pattern,
                        offset=offset,
                        dia=variant_dias[i] if variant_dias[i] else '',
                        color=variant_colors[i],
                        material=variant_materials[i],
                        price=float(variant_prices[i]) if variant_prices[i] else 0,
                        stock=int(variant_stocks[i]) if variant_stocks[i] else 0
                    )
                    
                    # Handle image if available
                    if i < len(variant_images) and variant_images[i]:
                        variant.image = variant_images[i]
                        
                    variant.save()
                except (ValueError, IndexError) as e:
                    messages.error(request, f'Ошибка при обработке размера: {variant_sizes[i]}. Проверьте формат (например: 16.0x7.0 5x100)')
                    continue
            
            messages.success(request, 'Диск успешно добавлен')
            return redirect('tyres:admin_rims')
    else:
        form = RimModelForm()
    return render(request, 'tyres/admin/rim_form.html', {'form': form, 'title': 'Добавить диск'})

@user_passes_test(lambda u: u.is_staff)
def edit_rim(request, rim_id):
    rim = get_object_or_404(RimModel, id=rim_id)
    if request.method == 'POST':
        form = RimModelForm(request.POST, request.FILES, instance=rim)
        if form.is_valid():
            try:
                # Проверяем, было ли загружено новое изображение
                if 'image' in request.FILES:
                    # Если старое изображение существует и это не изображение по умолчанию, удаляем его
                    if rim.image and rim.image.name != 'rims/default_rim.jpg' and default_storage.exists(rim.image.name):
                        default_storage.delete(rim.image.name)
                
                # Сохраняем форму
                rim_instance = form.save(commit=False)
                
                # Если был указан год выпуска
                release_year = request.POST.get('release_year')
                if release_year and release_year.strip():
                    rim_instance.release_year = int(release_year)
                
                rim_instance.save()
                messages.success(request, 'Диск успешно обновлен')
                return redirect('tyres:admin_rims')
            except Exception as e:
                messages.error(request, f'Ошибка при сохранении: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Ошибка в поле '{field}': {error}")
    else:
        form = RimModelForm(instance=rim)
    
    return render(request, 'tyres/admin/rim_form.html', {
        'form': form, 
        'title': 'Редактировать диск',
        'rim': rim
    })

@user_passes_test(lambda u: u.is_staff)
def delete_rim(request, rim_id):
    rim = get_object_or_404(RimModel, id=rim_id)
    if request.method == 'POST':
        rim.delete()
        messages.success(request, 'Диск успешно удален')
        return redirect('tyres:admin_rims')
    return render(request, 'tyres/admin/rim_confirm_delete.html', {'rim': rim})