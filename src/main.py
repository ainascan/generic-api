import logging

from flask import Flask
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)

import config

logging.info('Initializing Configuration...')
config.initialize()

app = Flask(__name__)

from routes import get_route
from routes import list_route
from routes import create_route
from routes import update_route
from routes import delete_route
from routes import exists_route

app.register_blueprint(get_route.mod)
app.register_blueprint(list_route.mod)
app.register_blueprint(create_route.mod)
app.register_blueprint(update_route.mod)
app.register_blueprint(delete_route.mod)
app.register_blueprint(exists_route.mod)

if __name__ == '__main__':
    logging.info('Starting Generic API...')
    app.run(host=config.HTTP_HOST, port=config.HTTP_PORT, debug=False)