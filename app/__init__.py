from flask import Flask
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'password'

from app import routes
