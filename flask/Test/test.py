import base64
import requests
import json

import config


def convert_base64(path: str):
    """
    convert the image into base64 encoded format and
    create the payload structure
    """
    with open(path, 'rb') as image_file:
        payload = base64.b64encode(image_file.read())
    
    payload_structure = {
        "body": {
            "image": payload.decode('utf-8')
        }
    }

    return payload_structure
    

def get_features(path: str, url: str = config.ENDPOINT_URL):
    """
    send a post REST api request to flask backend
    """
    image_payload = convert_base64(path)
    headers = {'Content-Type': 'application/json'}
    endpoint_response = requests.post(url, data = json.dumps(image_payload), headers = headers)
    response = getattr(endpoint_response, '_content').decode("utf-8")
    print(response)
    #final_response = json.loads(response)

    return response


if __name__ == "__main__":
    image_path = "test_image.png"
    print(image_path)
    response = get_features(image_path)
    print(response)