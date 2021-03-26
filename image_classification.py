import tensorflow as tf
import numpy as np
from PIL import ImageFile


ImageFile.LOAD_TRUNCATED_IMAGES = True

WIDTH = 512
HEIGHT = 512
CHANNELS = 3
IMAGE_SIZE = (WIDTH, HEIGHT)
LOAD_PATH = r'C:\Users\Artem\nsfw_data_scraper\data\models'
URL_IMAGE = r'http://i.imgur.com/V2Tyr5T.jpg'

gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized
        print(e)


def nudity_check(path_model, image, width, height, channels=3):
    model = tf.keras.models.load_model(path_model)
    image_resize = image.resize((width, height))
    image_arr = np.asarray(image_resize) / 255
    mean = np.mean(image_arr)
    std_dv = np.std(image_arr)
    image_arr = (image_arr - mean) / std_dv
    image_arr = image_arr.reshape((1, width, height, channels))
    predict = model.predict(image_arr)
    predicted = np.argmax(predict, axis=-1)
    return predicted
