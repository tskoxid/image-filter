import numpy as np
import requests
from tensorflow.python.client import device_lib
import tensorflow as tf
from image_scripts.image_classification import nudity_check
from image_scripts.text_extraction import extract_text
from image_scripts.filter_mata import obscene_filter
from PIL import Image


WIDTH: int = 512
HEIGHT: int = 512
MODEL_PATH: str = r'.\model'
IMAGE_SIZE = (WIDTH, HEIGHT)
URL_IMAGE = r'https://gorod.tomsk.ru/uploads/32813/1240403255/72434_ya_vas_schas_vyiebu_i_vyisushu.jpg'


def get_available_devices():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos]


if __name__ == '__main__':
    opened_image = Image.open(requests.get(URL_IMAGE, stream=True).raw)

    get_available_devices()

    with tf.device('/cpu:0'):
        predict_class = nudity_check(MODEL_PATH, opened_image, WIDTH, HEIGHT)

    if predict_class[0] == 0:
        text_from_image = extract_text(np.asarray(opened_image))
        text_after_filter = obscene_filter(text_from_image)
        print("Изображение содержит мат\n" if not text_after_filter else "Изображение прошло проверку")
    else:
        print("Изображение заблокировано!\n")
