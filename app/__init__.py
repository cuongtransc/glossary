from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.log import Logging

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)

flask_log = Logging(app)

from app.models import user
from app.models import term

from app.routes import index
from app.routes import users
from app.routes import glossary
