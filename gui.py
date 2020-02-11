from main import app
from flask import render_template, flash, redirect, url_for
import art
from art import Art
import artist
from artist import Artist
from get_info import ArtInputForm, ArtistInputForm

@app.route('/')
@app.route('/art', methods=['GET', 'POST'])
def show_art():
    art_list = art.get_all_art()
    return render_template('display_art.html', art_list = art_list)

@app.route('/artists')
def show_artists():
    artists = artist.get_all_artists()
    return render_template('display_artists.html', artists = artists)

@app.route('/addart', methods=['GET', 'POST'])
def addart():
    form = ArtInputForm()
    if form.validate_on_submit():
        artwork = Art(name=form.name.data, artist=form.artist.data, price=form.price.data)
        art.add_art(artwork)
        flash('Your post has been created!', 'success')
        return redirect(url_for('show_art'))
    return render_template('add_art.html', title='AddArt', form=form)

@app.route('/addartist')
def addartist():
    form = ArtistInputForm()
    return render_template('add_artist.html', title='AddArtist', form=form)