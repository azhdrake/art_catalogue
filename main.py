from art import Art
from artist import Artist
import art
import artist
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blargitsasecretthatdoesntmatterforthiscontext'

import gui
