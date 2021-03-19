# Nudity detection and word extraction from image.
1. Файл image_classification.py классифицирует изображение с помощью зафайнтюненой модели InceptionV3.
2. Файл text_extraction.py извлекает текст с помощью tesseract-ocr и openCV. 
3. Файл filter_mata.py проверяет текст на наличие мата. Если находит, то заменяет слово по типу данной маски: word -> w***
