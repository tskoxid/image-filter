import tensorflow as tf
import pytesseract
from PIL import ImageFile
from csv import reader
from image_scripts.classes import ImageClassification

MODEL_PATH: str = r'.\model'
PATH_TESSERACT: str = r'C:\Users\Artem\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
PATH_CORPUS: str = r".\data\profane_corpus.csv"
pytesseract.pytesseract.tesseract_cmd = PATH_TESSERACT
ImageFile.LOAD_TRUNCATED_IMAGES = True

model_keras = tf.keras.models.load_model(MODEL_PATH)
corpus_list = []
with open(PATH_CORPUS, 'r', encoding='utf8') as f:
    csv_reader = reader(f)
    for row in csv_reader:
        corpus_list.append(row[0])
corpus_words: set = set(corpus_list)


def main(url_image, model=model_keras, corpus=None):
    if corpus is None:
        corpus = corpus_words
    with tf.device('/cpu:0'):
        new_examaple = ImageClassification(url_image, model, corpus)
        opened_image = new_examaple.open_image()
        normalized_image = new_examaple.normalized_image(opened_image)
        if new_examaple.classify_image(normalized_image):
            text = new_examaple.extract_text(opened_image)
            filtered_text = new_examaple.preprocessing_text(text)
            result = new_examaple.obscene_filter(filtered_text)
            print("Изображение содержит мат" if not result else "Изображение прошло проверку")
        else:
            print("Изображение содержит обнаженку")


if __name__ == '__main__':
    url_image_list = ['https://i.pinimg.com/564x/ff/12/c4/ff12c41417f4d15220628479754ede42.jpg',
                      'https://i.pinimg.com/564x/0b/76/24/0b7624609162e8336908df59231735c5.jpg',
                      'https://i.pinimg.com/564x/ef/25/22/ef2522bab80dc1f9291d1c159a346ce1.jpg']
    for URL_IMAGE in url_image_list:
        main(URL_IMAGE)
