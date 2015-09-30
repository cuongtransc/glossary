import os

basedir = os.path.abspath(os.path.dirname(__file__))

# DEBUG = True
DEBUG = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# FLASK_LOG_LEVEL = 'DEBUG'
if DEBUG:
    FLASK_LOG_LEVEL = 'DEBUG'
else:
    FLASK_LOG_LEVEL = 'INFO'

