
from celery import Celery

from flask import Flask


import app.config as app_config

import os




def create_app_load_configurations():
    #load_configurations_file()
    app = Flask(__name__, static_folder='static', static_url_path='/static/')

    app.secret_key = app_config.SECRET_KEY

    return app


def init_celery(app):
    client = Celery(app.name, backend=app_config.CELERY_RESULT_BACKEND,
                    broker=app_config.CELERY_BROKER_URL)
    client.conf.update(app.config)
    return client

