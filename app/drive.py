import base64
import numpy as np
from numpy import asarray
import io
from PIL import Image, ImageOps
from flask import Flask

# Disable Tensorflow messages
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array



def get_model():
    model = load_model('keras_model.h5')
    print(" ***** Model loaded! ***** ")
    return model

def process_image(encoded_image):
    decoded_image = base64.b64decode(encoded_image)
    print("Decoded")
    image = Image.open(io.BytesIO(decoded_image))
    print("opened")
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    print("resized")
    image_array = np.asarray(image)[:,:,:3]
    print(image_array.shape)
    print(data[0].shape)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    return data

def model_response(model, encoded_image):
    data = process_image(encoded_image)
    prediction = model.predict(data)
    print(prediction)
    prediction = model.predict(data)
    value = np.argmax(prediction.item(0))
    print(value)
    if prediction[0][0] > prediction[0][1]:
        result = "safe"
    else:
        result = "unsafe"
    return {
        'prediction': result
    }
