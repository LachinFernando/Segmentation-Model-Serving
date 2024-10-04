import base64
from io import BytesIO
from PIL import Image
import numpy as np
from skimage.transform import resize

IMG_SIZE = 256


def convert_to_bytes(path):

    with open(path, "rb") as image:
        payload = base64.b64encode(image.read())

    return payload.decode('utf-8')


def get_image_payload(data):
    """
    Get the base64 encoded data of an image and
    convert it to a bytearray
    """
    image = base64.b64decode(data)
    payload = bytearray(image)
    return payload


def preprocess_image_input(img):
    """
    Convert the bytestream to RGB.
    And apply the same preprocessing used in training.
    """
    # convert byte stream to RGB
    stream = BytesIO(img)
    img = Image.open(stream).convert("RGB")
    img_array = np.array(img)
    # resize the image
    img_array = resize(img_array, (IMG_SIZE, IMG_SIZE, 3), mode="constant", preserve_range=True)
    # expand the dimension to represent batch
    img_batch = np.expand_dims(img_array, axis = 0)
    return img_batch