from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from waitress import serve
from routes.cryptography import cryptography

load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(cryptography)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=6010)
