# -*-coding=utf-8 -*-
#!flask/bin/python
from app import app
from getIp import getIp
import os

app.run(debug = False,host=getIp(),port=4443)