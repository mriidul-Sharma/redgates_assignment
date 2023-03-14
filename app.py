from flask import Flask
from routes.endpoints import rg_app

app = Flask(__name__)

app.register_blueprint(rg_app)

if __name__ == "__main__":
    app.run()