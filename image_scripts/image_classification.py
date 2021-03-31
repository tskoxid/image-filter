import tensorflow as tf
import numpy as np
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

WIDTH: int = 512
HEIGHT: int = 512
CHANNELS: int = 3
IMAGE_SIZE = (WIDTH, HEIGHT)


def nudity_check(path_model, image, width=WIDTH, height=HEIGHT, channels=CHANNELS):
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
