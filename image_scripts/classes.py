import numpy as np
from PIL import Image
import pytesseract
import tensorflow as tf
import typing


class ImageClassification:
    __WIDTH: int = 512
    __HEIGHT: int = 512
    __CHANNELS: int = 3
    corpus: set
    model_path: str

    def __init__(self, corpus: set, model_path: str):
        self.corpus = corpus
        self.model = tf.keras.models.load_model(model_path)

    @staticmethod
    def open_image(image_bytes):
        image = Image.open(image_bytes)
        return image

    def normalized_image(self, image: bytearray):
        image_resize = image.resize((self.__WIDTH, self.__HEIGHT))
        image_arr = np.asarray(image_resize) / 255
        mean = np.mean(image_arr)
        std_dv = np.std(image_arr)
        image_arr = (image_arr - mean) / std_dv
        image_arr = image_arr.reshape((1, self.__WIDTH, self.__HEIGHT, self.__CHANNELS))
        return image_arr

    def classify_image(self, image_arr: bytearray):
        predict = self.model.predict(image_arr)
        predicted = np.argmax(predict, axis=-1)
        return False if predicted == 1 else True

    @staticmethod
    def extract_text_from_image(image_arr: bytearray):
        text = pytesseract.image_to_string(image_arr, lang='rus', config=r"--oem 3 --psm 6")
        return text

    @staticmethod
    def preprocessing_text(text: str):
        text = text.lower().replace('\n', ' ').replace('\x0c', '')
        text = text.split(' ')
        filtered_list = []
        for word in text:
            filtered_text = [character for character in word if character.isalnum()]
            filtered_list.append("".join(filtered_text))
        return filtered_list

    def obscene_filter(self, filtered_text: typing.List[str]):
        for word in filtered_text:
            if word in self.corpus:
                return False
            else:
                continue
        return True
