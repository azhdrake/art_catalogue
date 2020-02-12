# Main.py: It runs things!™

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blargitsasecretthatdoesntmatterforthiscontext'

import gui
