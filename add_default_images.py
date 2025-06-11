import os
import django
import shutil

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tyre_trust.settings')
django.setup()

from django.conf import settings
from pathlib import Path

def create_default_images():
    print("Создание папок для медиа-файлов...")
    
    # Создание необходимых директорий
    tyres_dir = os.path.join(settings.MEDIA_ROOT, 'tyres')
    rims_dir = os.path.join(settings.MEDIA_ROOT, 'rims')
    
    os.makedirs(tyres_dir, exist_ok=True)
    os.makedirs(rims_dir, exist_ok=True)
    
    print(f"Папки созданы: {tyres_dir}, {rims_dir}")
    
    # Создание пустого изображения для шин по умолчанию
    default_tyre_path = os.path.join(tyres_dir, 'default_tyre.jpg')
    if not os.path.exists(default_tyre_path):
        # Создаем пустое изображение или копируем заготовку из статических файлов
        with open(default_tyre_path, 'wb') as f:
            # В этом примере просто создаем пустой файл
            f.write(b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00')
        print(f"Создано изображение по умолчанию для шин: {default_tyre_path}")
    else:
        print(f"Изображение по умолчанию для шин уже существует: {default_tyre_path}")
    
    # Создание пустого изображения для дисков по умолчанию
    default_rim_path = os.path.join(rims_dir, 'default_rim.jpg')
    if not os.path.exists(default_rim_path):
        # Создаем пустое изображение или копируем заготовку из статических файлов
        with open(default_rim_path, 'wb') as f:
            # В этом примере просто создаем пустой файл
            f.write(b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00')
        print(f"Создано изображение по умолчанию для дисков: {default_rim_path}")
    else:
        print(f"Изображение по умолчанию для дисков уже существует: {default_rim_path}")

if __name__ == "__main__":
    create_default_images()
    print("Задача выполнена!") 