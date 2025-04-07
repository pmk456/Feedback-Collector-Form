from flask import Flask
from .routes import routes

def create_app():
    app = Flask('app')
    app.register_blueprint(routes)
    return app