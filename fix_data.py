import os
import django
import random
from PIL import Image, ImageDraw

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tyre_trust.settings')
django.setup()

from django.conf import settings
from tyres.models import TyreModel, TyreVariant, RimModel, RimVariant

# Создаем реалистичные изображения для товаров
def create_image(filepath, width=800, height=800, color=None):
    if color is None:
        color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
    
    img = Image.new('RGB', (width, height), color=color)
    draw = ImageDraw.Draw(img)
    
    # Рисуем круг для имитации шины/диска
    circle_x = width // 2
    circle_y = height // 2
    radius = min(width, height) // 2 - 50
    
    draw.ellipse((circle_x - radius, circle_y - radius, 
                  circle_x + radius, circle_y + radius), 
                  fill=(30, 30, 30))
    
    # Добавляем внутренний круг для имитации диска
    inner_radius = radius - 100
    draw.ellipse((circle_x - inner_radius, circle_y - inner_radius, 
                  circle_x + inner_radius, circle_y + inner_radius), 
                  fill=(200, 200, 200))
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    img.save(filepath, quality=95)
    return filepath

def fix_tyre_images():
    print("Исправление изображений для шин...")
    tyres_count = TyreModel.objects.count()
    print(f"Найдено моделей шин: {tyres_count}")
    
    for tyre in TyreModel.objects.all():
        # Создаем директорию для изображений шин
        target_dir = os.path.join(settings.MEDIA_ROOT, 'tyres')
        os.makedirs(target_dir, exist_ok=True)
        
        # Генерируем уникальное имя файла изображения
        image_path = os.path.join(target_dir, f"tyre_{tyre.brand}_{tyre.name}.jpg".replace(' ', '_').lower())
        
        # Создаем новое изображение
        create_image(image_path, color=(240, 240, 240))
        
        # Обновляем путь к изображению в модели
        relative_path = os.path.relpath(image_path, settings.MEDIA_ROOT)
        tyre.image = relative_path
        tyre.save()
        
        print(f"Обновлено изображение для шины: {tyre.brand} {tyre.name} -> {relative_path}")

def fix_rim_images():
    print("\nИсправление изображений для дисков...")
    rims_count = RimModel.objects.count()
    print(f"Найдено моделей дисков: {rims_count}")
    
    for rim in RimModel.objects.all():
        # Создаем директорию для изображений дисков
        target_dir = os.path.join(settings.MEDIA_ROOT, 'rims')
        os.makedirs(target_dir, exist_ok=True)
        
        # Генерируем уникальное имя файла изображения
        image_path = os.path.join(target_dir, f"rim_{rim.brand}_{rim.name}.jpg".replace(' ', '_').lower())
        
        # Создаем новое изображение с серебристым оттенком (как диски)
        create_image(image_path, color=(220, 220, 230))
        
        # Обновляем путь к изображению в модели
        relative_path = os.path.relpath(image_path, settings.MEDIA_ROOT)
        rim.image = relative_path
        rim.save()
        
        print(f"Обновлено изображение для диска: {rim.brand} {rim.name} -> {relative_path}")

if __name__ == "__main__":
    fix_tyre_images()
    fix_rim_images()
    print("\nИсправление данных завершено!") 