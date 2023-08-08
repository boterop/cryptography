import uuid
from flask import request, Blueprint
from lib.crypto import Crypto

cryptography = Blueprint('cryptography', __name__)


def get(prop):
    data = request.get_json(force=True)
    return data[prop]


def response(code, message):
    return {'status': code, 'response': message}


@cryptography.route('/base64', methods=['POST'])
def base64():
    text = get("text")
    method = get("method")
    return response(200, Crypto.base64(text, method))


@cryptography.route('/base64-image', methods=['POST'])
def base64_image():
    text = get("image-url")
    return response(200, Crypto.base64_image(text))

@cryptography.route('/gen-uuid', methods=['GET'])
def gen_uuid():
    return response(200, str(uuid.uuid4()))

@cryptography.route('/health', methods=['POST'])
def health():
    return response(200, "OK")
