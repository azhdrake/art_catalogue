from main import app
from flask import render_template
import art

@app.route('/')
@app.route('/art')
def show_art():
    art_list = art.get_all_art()
    return render_template('desplay_art.html', art_list = art_list)