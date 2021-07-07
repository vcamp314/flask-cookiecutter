from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title='Sample App', version='0.0.1', doc=('/' if env != 'prod' else False))
    migrate = Migrate(app, db)

    register_routes(api, app)
    db.init_app(app)
    ma.init_app(app)

    @app.route('/health')
    def health():
        return jsonify('healthy')

    return app
