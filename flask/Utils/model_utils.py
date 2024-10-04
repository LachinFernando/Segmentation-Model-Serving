import segmentation_models as sm
import tensorflow as tf
import os


def load_model():
    # load the model
    final_model = tf.keras.models.load_model("./Models/Unet.h5", custom_objects={"iou_score": sm.metrics.iou_score})
    return final_model