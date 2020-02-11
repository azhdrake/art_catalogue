from main import app
from flask import render_template, flash, redirect, url_for
import art
from art import Art
import artist
from artist import Artist
from get_info import ArtInputForm, ArtistInputForm

@app.route('/artists')
def show_artists():
    artists = artist.get_all_artists()
    return render_template('display_artists.html', artists = artists)

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


@app.route('/addartist', methods=['GET', 'POST'])
def addartist():
    form = ArtistInputForm()
    if form.validate_on_submit():
        new_artist = Artist(name=form.name.data, email_address=form.email_address.data)
        artist.add_artist(new_artist)
        flash('The new artist has been added!', 'success')
        return redirect(url_for('show_artists'))
    return render_template('add_artist.html', title='AddArtist', form=form)