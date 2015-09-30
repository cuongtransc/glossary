#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app

if app.debug is not True:
    import logging
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler('logs/glossary.log', maxBytes=1024 * 1024 * 100, backupCount=20)
    #file_handler.setLevel(logging.ERROR)
    #file_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

app.run(host='0.0.0.0', debug=app.debug)
#app.run(host='0.0.0.0')

