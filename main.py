from flask import Flask
from flask_restful import Api
from resources.foo import Foo
from models import db
from config import app_config
import os


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(app_config[environment])
    db.init_app(app)
    api = Api(app)
   
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    return app

if __name__ == "__main__":
    app = create_app(os.getenv('environment'))
    app.run()

