# Nudity detection and word extraction from image.
1. Файл image_classification.py классифицирует изображение с помощью зафайнтюненой модели InceptionV3.
2. Файл text_extraction.py извлекает текст с помощью tesseract-ocr и openCV. 
3. Файл filter_mata.py проверяет текст на наличие мата. Если находит, то заменяет слово по типу данной маски: word -> w***

Для работы нужно добавить папку с моделью. Скачать можно по ссылке: https://www.dropbox.com/sh/q9wo1gg6bsaau68/AAAB8FR7Ekrjnr7j-tTiqJ8ta?dl=0
