#-*- coding: utf-8 -*-

from app import app

@app.route('/')
def root():
    return app.send_static_file('index.html')


