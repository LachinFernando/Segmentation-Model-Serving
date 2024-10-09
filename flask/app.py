from flask import Flask, request, jsonify
import logging
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from Utils import response_utils as rutils
from Utils import image_utils as iutils
from Utils import model_utils as mutils


# constants
IMAGE_SAVE_NAME = "output.png"

# setup flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)


@app.route("/inference", methods=["POST"])
def inference():
    if request.method == "POST":
        data = request.json
        params = data["body"]
        image_data = params["image"]

        # load the row image
        try:
            payload = iutils.get_image_payload(image_data)
            process_payload = iutils.preprocess_image_input(payload)

            # load the model
            segment_model = mutils.load_model()
            predictions = segment_model.predict(process_payload, verbose = 0)
            # save the image
            plt.imsave(IMAGE_SAVE_NAME,np.squeeze(predictions))
            # get image bytes
            pred_to_bytes = iutils.convert_to_bytes(IMAGE_SAVE_NAME)

            # send the response
            return jsonify(rutils.success_response({"prediction": pred_to_bytes}))

        except Exception as error:
            app.logger.info(str(error))
            message = "unable to get features. Error message: {}".format(str(error))
            error_info = {"errorCode": None, "message": message, "suggestions": None}
            return jsonify(rutils.failuer_response([error_info]))
    else:
        message = "Invalid HTTP method"
        error_info = {"errorCode": None, "message": message, "suggestions": None}
        return jsonify(rutils.failuer_response([error_info]))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")