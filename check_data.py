import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tyre_trust.settings')
django.setup()

from tyres.models import TyreModel, TyreVariant, RimModel, RimVariant

def check_tyres():
    print("\n=== ПРОВЕРКА ШИН ===")
    tyres_count = TyreModel.objects.count()
    print(f"Общее количество моделей шин в базе: {tyres_count}")
    
    for tyre in TyreModel.objects.all():
        variants = tyre.variants.all()
        variant_count = variants.count()
        print(f"\nМодель: {tyre.brand} {tyre.name}")
        print(f"  Описание: {tyre.description[:50]}...")
        print(f"  Изображение: {tyre.image}")
        print(f"  Количество вариантов: {variant_count}")
        
        if variant_count > 0:
            for i, variant in enumerate(variants[:3], 1):
                print(f"  Вариант {i}: {variant.width}/{variant.profile} R{variant.radius}, "
                      f"{variant.get_season_display()}, цена: {variant.price} руб., на складе: {variant.stock} шт.")
            if variant_count > 3:
                print(f"  ... и еще {variant_count - 3} вариантов")

def check_rims():
    print("\n=== ПРОВЕРКА ДИСКОВ ===")
    rims_count = RimModel.objects.count()
    print(f"Общее количество моделей дисков в базе: {rims_count}")
    
    for rim in RimModel.objects.all():
        variants = rim.variants.all()
        variant_count = variants.count()
        print(f"\nМодель: {rim.brand} {rim.name}")
        print(f"  Описание: {rim.description[:50]}...")
        print(f"  Изображение: {rim.image}")
        print(f"  Количество вариантов: {variant_count}")
        
        if variant_count > 0:
            for i, variant in enumerate(variants[:3], 1):
                print(f"  Вариант {i}: {variant.diameter}x{variant.width}, "
                      f"{variant.bolt_pattern}, цена: {variant.price} руб., на складе: {variant.stock} шт.")
            if variant_count > 3:
                print(f"  ... и еще {variant_count - 3} вариантов")

if __name__ == "__main__":
    check_tyres()
    check_rims()
    print("\nПроверка завершена.") 