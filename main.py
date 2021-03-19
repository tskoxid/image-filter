from PIL import Image
import numpy as np
import requests
from image_classification import nudity_check
from text_extraction import preprocessing_image, extract_text
from filter_mata import obscene_filter


WIDTH = 512
HEIGHT = 512
IMAGE_SIZE = (WIDTH, HEIGHT)
MODEL_PATH = r'.\model'
PATH_CORPUS = r"C:/Users/Artem/obscene_words_ru/profane_corpus.csv"
URL_IMAGE = r'https://mass-images.pro/files/preview/5/12/cf5a5bfa30bd11bd032baa19457504a3.jpg?1616155802690'


if __name__ == '__main__':
    opened_image = Image.open(requests.get(URL_IMAGE, stream=True).raw)
    predict_class = nudity_check(MODEL_PATH, opened_image, WIDTH, HEIGHT)
    print("Изображение прошло проверку\n" if predict_class[0] == 0 else "Изображение заблокировано!")
    if predict_class[0] == 0:
        gray_image = preprocessing_image(np.asarray(opened_image))
        text_from_image = extract_text(gray_image)
        text_from_image = text_from_image.replace('\n', ' ').replace('  ', ' ').replace('        ', '')
        text_from_image = text_from_image.replace('?', '').replace('.', '').replace('  ', ' ').lower()[:-2]
        print("Find text in image :", text_from_image, '\n')

        text_after_filter = obscene_filter(PATH_CORPUS, text_from_image)

        print("Text after filter: ", text_after_filter)
