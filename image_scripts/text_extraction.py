import pytesseract

PATH_TESSERACT: str = r'C:\Users\Artem\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = PATH_TESSERACT


def extract_text(gray):
    text = pytesseract.image_to_string(gray, lang='rus', config=r"--oem 3 --psm 6")
    return text
