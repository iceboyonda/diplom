from PIL import Image
import os

def crop_to_square(image_path):
    # Открываем изображение
    img = Image.open(image_path)
    width, height = img.size
    
    # Определяем размер квадрата (берем минимальную сторону)
    size = min(width, height)
    
    # Вычисляем координаты для обрезки
    # Центрируем по горизонтали
    left = (width - size) // 2
    right = left + size
    
    # Для вертикали берем верхнюю часть, так как диск обычно в верхней части изображения
    top = 0
    bottom = size
    
    # Обрезаем изображение
    cropped_img = img.crop((left, top, right, bottom))
    
    # Сохраняем обрезанное изображение
    cropped_img.save(image_path)
    print(f"Изображение обработано и сохранено: {image_path}")

if __name__ == "__main__":
    # Путь к изображению
    image_path = "media/rims/lasr.jpg"
    
    # Проверяем существование файла
    if os.path.exists(image_path):
        crop_to_square(image_path)
    else:
        print(f"Файл не найден: {image_path}") 