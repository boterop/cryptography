import base64
import requests


class Crypto():
    def base64(text, method):
        return base64.b64encode(text.encode()).decode() if method == 'encode' else base64.b64decode(text).decode()

    def base64_image(image_url):
        return "data:image/jpeg;base64,{}".format(base64.b64encode(requests.get(image_url).content).decode())
