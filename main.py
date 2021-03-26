from PIL import Image
import numpy as np
import requests
from image_classification import nudity_check
from text_extraction import preprocessing_image, extract_text
from filter_mata import obscene_filter
import pandas as pd


WIDTH = 512
HEIGHT = 512
IMAGE_SIZE = (WIDTH, HEIGHT)
MODEL_PATH = r'.\model'
URL_IMAGE = r'https://gorod.tomsk.ru/uploads/32813/1240403255/72434_ya_vas_schas_vyiebu_i_vyisushu.jpg'
PATH_CORPUS = r".\profane_corpus.csv"

corpus = pd.read_csv(PATH_CORPUS)
corpus = set(corpus['Words'])

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

        text_after_filter = obscene_filter(corpus, text_from_image)

        print("Text after filter: ", text_after_filter)
