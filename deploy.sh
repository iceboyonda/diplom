#!/bin/bash
# Скрипт для развертывания на сервере

# Цвета для вывода
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Начинаем развертывание приложения...${NC}"

# Создание директорий, если они не существуют
echo -e "${BLUE}Проверка и создание необходимых директорий...${NC}"
mkdir -p media/tyres
mkdir -p media/rims
mkdir -p static
mkdir -p logs

# Установка необходимых пакетов
echo -e "${BLUE}Установка зависимостей...${NC}"
pip install -r requirements.txt

# Миграция базы данных
echo -e "${BLUE}Применение миграций...${NC}"
python manage.py migrate

# Сбор статических файлов
echo -e "${BLUE}Сбор статических файлов...${NC}"
python manage.py collectstatic --noinput

# Создание дефолтных изображений, если они отсутствуют
echo -e "${BLUE}Проверка наличия файлов-заглушек...${NC}"
if [ ! -f "media/tyres/default_tyre.jpg" ]; then
    echo -e "${RED}Файл default_tyre.jpg отсутствует, создаем заглушку...${NC}"
    touch media/tyres/default_tyre.jpg
fi

if [ ! -f "media/rims/default_rim.jpg" ]; then
    echo -e "${RED}Файл default_rim.jpg отсутствует, создаем заглушку...${NC}"
    touch media/rims/default_rim.jpg
fi

# Настройка прав доступа
echo -e "${BLUE}Настройка прав доступа...${NC}"
chmod -R 755 .
chmod -R 777 media
chmod -R 777 static
chmod -R 777 logs

# Диагностика продакшн окружения
echo -e "${BLUE}Запуск диагностики продакшн окружения...${NC}"
python debug_production.py

echo -e "${GREEN}Развертывание завершено успешно!${NC}"
echo -e "${GREEN}Не забудьте перезапустить веб-сервер и проверить логи!${NC}"
echo -e "${BLUE}Для запуска тестового сервера выполните:${NC} python manage.py runserver 0.0.0.0:8000 