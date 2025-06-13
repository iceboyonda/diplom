#!/usr/bin/env python
"""
Скрипт для диагностики проблем в продакшн окружении Django-приложения
"""

import os
import sys
import django
import logging
from pathlib import Path

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler("production_debug.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def main():
    # Определение текущей директории
    base_dir = Path(__file__).resolve().parent
    logger.info(f"Базовая директория: {base_dir}")
    
    # Настройка окружения Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tyre_trust.settings')
    sys.path.insert(0, str(base_dir))
    
    try:
        django.setup()
        logger.info("Django успешно инициализирован")
    except Exception as e:
        logger.error(f"Ошибка при инициализации Django: {e}")
        return

    # Импортируем модели после настройки Django
    try:
        from django.contrib.auth import get_user_model
        from tyres.models import TyreModel, RimModel
        from orders.models import Order
        from django.conf import settings
        
        User = get_user_model()
        
        # Проверка наличия пользователей
        user_count = User.objects.count()
        logger.info(f"Количество пользователей в базе: {user_count}")
        
        # Проверка наличия администраторов
        staff_count = User.objects.filter(is_staff=True).count()
        logger.info(f"Количество администраторов: {staff_count}")
        
        # Проверка количества товаров
        tyre_count = TyreModel.objects.count()
        rim_count = RimModel.objects.count()
        logger.info(f"Количество моделей шин: {tyre_count}")
        logger.info(f"Количество моделей дисков: {rim_count}")
        
        # Проверка заказов
        order_count = Order.objects.count()
        logger.info(f"Количество заказов: {order_count}")
        
        # Проверка настроек
        logger.info(f"DEBUG включен: {settings.DEBUG}")
        logger.info(f"База данных: {settings.DATABASES['default']['ENGINE']}")
        logger.info(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
        logger.info(f"STATIC_ROOT: {settings.STATIC_ROOT}")
        
        # Проверка наличия файлов в media
        media_root = Path(settings.MEDIA_ROOT)
        if media_root.exists():
            logger.info(f"Директория MEDIA_ROOT существует: {media_root}")
            media_files_count = sum(1 for _ in media_root.glob('**/*') if _.is_file())
            logger.info(f"Количество файлов в MEDIA_ROOT: {media_files_count}")
        else:
            logger.error(f"Директория MEDIA_ROOT не существует: {media_root}")
        
        # Проверка наличия файлов в static
        static_root = Path(settings.STATIC_ROOT)
        if static_root.exists():
            logger.info(f"Директория STATIC_ROOT существует: {static_root}")
            static_files_count = sum(1 for _ in static_root.glob('**/*') if _.is_file())
            logger.info(f"Количество файлов в STATIC_ROOT: {static_files_count}")
        else:
            logger.error(f"Директория STATIC_ROOT не существует: {static_root}")
        
        # Проверяем права доступа к директориям
        for path in [media_root, static_root]:
            if path.exists():
                logger.info(f"Права доступа к {path}: {oct(path.stat().st_mode)[-3:]}")
                
        # Проверяем настройки веб-сервера
        logger.info(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
            
    except Exception as e:
        logger.error(f"Ошибка при проверке данных: {e}")

if __name__ == '__main__':
    logger.info("Начало выполнения скрипта диагностики")
    main()
    logger.info("Завершение выполнения скрипта диагностики") 