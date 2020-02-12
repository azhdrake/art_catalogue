from main import app
from flask import render_template, flash, redirect, url_for, request
import art
from art import Art
import artist
from artist import Artist
from get_info import ArtInputForm, ArtistInputForm

# Most of my Flask knowledge was gained using these tutorials: https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

# routes gives the url ending and method the page will accept. Method under route is what runs when that route is reached.
@app.route('/', methods=['GET', 'POST'])
@app.route('/art', methods=['GET', 'POST'])
@app.route('/addart', methods=['GET', 'POST'])
def addart():
    form = ArtInputForm()
    art_list = art.get_all_art()
    if form.validate_on_submit():
        artwork = Art(name=form.name.data, artist=form.artist.data, price=form.price.data)
        art.add_art(artwork)
        flash('The new artwork has been added!', 'success')
        art_list = art.get_all_art()
    return render_template('add_art.html', title='AddArt', form=form, art_list=art_list)

@app.route('/artists', methods=['GET', 'POST'])
@app.route('/addartist', methods=['GET', 'POST'])
def addartist():
    form = ArtistInputForm()
    artists = artist.get_all_artists()
    if form.validate_on_submit():
        new_artist = Artist(name=form.name.data, email_address=form.email_address.data)
        artist.add_artist(new_artist)
        flash('The new artist has been added!', 'success')
        artists = artist.get_all_artists()
    return render_template('add_artist.html', title='AddArtist', form=form, artists=artists)

@app.route('/delete_art', methods=['POST'])
def delete_art():
    art_form = ArtInputForm()
    if request.form['submit_button'] == 'delete':
        id_list = request.form.getlist('selected')
        for art_id in id_list:
            art.delete_art(art_id)
        flash('The art has been deleted!', 'success')
    elif request.form['submit_button'] == 'change':
        id_list = request.form.getlist('selected')
        for art_id in id_list:
            art.change_available(art_id)
        flash('The deed is done!', 'success')
    art_list = art.get_all_art()
    return render_template('add_art.html', title='AddArt', form=art_form, art_list=art_list)

@app.route('/change_status', methods=['POST'])
def change_status():
    art_form = ArtInputForm()
    
    art_list = art.get_all_art()
    return render_template('add_art.html', title='AddArt', form=art_form, art_list=art_list)