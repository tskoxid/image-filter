import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Artem\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def preprocessing_image(image):
    preprocess = "thresh"
    # загрузить образ и преобразовать его в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)
    return gray


def extract_text(gray):
    text = pytesseract.image_to_string(gray, lang='rus')
    return text
