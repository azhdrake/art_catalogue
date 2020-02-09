from model import *

def add_artist(artist):
    try:
        artist.save()
        return True
    except peewee.IntegrityError:
        return False

def show_artists_art(artist_id):
    artist = Artist.select().where(Artist.id == artist_id)
    query = Art.select(Art).join(Art).where(Art.artist = artist.name)
    return list(query)