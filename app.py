from flask import Flask
from flask_cors import CORS

from config import Config
from services import api_bp


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["SECRET_KEY"] = Config.SECRET_KEY
    app.register_blueprint(api_bp)

    print(app.url_map)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8003)
