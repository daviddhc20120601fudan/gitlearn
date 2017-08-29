from __init__ import app
from flask import Flask


@app.route('/')
def index():
    return 'Hello World!'