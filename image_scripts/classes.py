import numpy as np
# import numpy.typing as npt
import pytesseract
import tensorflow as tf
import typing
import requests
import io
from PIL import Image


class ImageClassification():
    __WIDTH: int = 512
    __HEIGHT: int = 512
    __CHANNELS: int = 3
    model_path: str

    def __init__(self, corpus: typing.Set[str], model_path: str):
        self.corpus = corpus
        self.model = tf.keras.models.load_model(model_path)

    @staticmethod
    def download_image_from_url(url_image: str):
        response = requests.get(url_image)
        image_bytes = io.BytesIO(response.content)
        return image_bytes

    @staticmethod
    def open_image(image_bytes: bytearray):
        image = Image.open(image_bytes)
        return image

    def normalized_image(self, image):
        image_resize = image.resize((self.__WIDTH, self.__HEIGHT))
        image_arr = np.asarray(image_resize) / 255
        mean = np.mean(image_arr)
        std_dv = np.std(image_arr)
        image_arr = (image_arr - mean) / std_dv
        image_arr = image_arr.reshape((1, self.__WIDTH, self.__HEIGHT, self.__CHANNELS))
        return image_arr

    def classify_single_image(self, image_arr: bytearray):
        predict = self.model.predict(image_arr)
        predicted = np.argmax(predict, axis=-1)
        return False if predicted == 1 else True

    @staticmethod
    def extract_text_from_image(image_arr: bytearray):
        text = pytesseract.image_to_string(image_arr, lang='rus', config=r"--oem 3 --psm 6")
        return text

    def obscene_filter(self, filtered_text: typing.List[str]):
        for word in filtered_text:
            if word in self.corpus:
                return False
            else:
                continue
        return True
