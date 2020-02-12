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
    # Get the input form and the list of all art. Checks if someone submitted the form. If not feeds art to page and displays. 
    # If someone did submit the form and it's valid, feeds that information to the database, gets the new list of art and refreshes page.
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
    # It's the same thing as addart but it's artist instead.
    form = ArtistInputForm()
    artists = artist.get_all_artists()
    if form.validate_on_submit():
        new_artist = Artist(name=form.name.data, email_address=form.email_address.data)
        artist.add_artist(new_artist)
        flash('The new artist has been added!', 'success')
        artists = artist.get_all_artists()
    return render_template('add_artist.html', title='AddArtist', form=form, artists=artists)

@app.route('/modify_art', methods=['POST'])
def modify_art():
    # Called when a button's pressed in the art page. Checks which button was pressed, if it's delete, it deletes the art.
    # If the button was change, it changes the availablity status of the art.  Then it rerenders the art page.
    # If the button was show_available, it pulls the art that's available and feeds the page that instead of the full list.
    # TODO add are you sure to delete method
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
    if request.form['submit_button'] == 'show_available':
        art_list = art.get_art_by_availability()
    return render_template('add_art.html', title='AddArt', form=art_form, art_list=art_list)

@app.route('/show_artists_art', methods=['POST'])
def show_artists_art():
    # Gets artist id from form, plugs it into the artist method and gives add_art.html the resulting artwork list.
    art_form = ArtInputForm()
    artist_id = request.form.get('explore')
    art_list = artist.show_artists_art(artist_id)
    return render_template('add_art.html', title='AddArt', form=art_form, art_list=art_list)
