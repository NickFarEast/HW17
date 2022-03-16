from flask import Flask, request
from flask_restx import Api, Resource
from marshmallow import Schema, fields
from app.config import Config
from app.database import db


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace('movies')














movie_schema = MoviesSchema()
movies_schema = MoviesSchema(many=True)





if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    app.run()
