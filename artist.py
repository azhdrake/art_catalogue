# The artist class Talks to the database.

from Models import Artist
from Models import Art
from peewee import IntegrityError

def add_artist(artist):
    try:
        artist.save()
    except IntegrityError:
        raise ArtistError(f'{artist.name} already in system.')

def get_artist_id(artist_name):
    try:
        query = Artist.select().where(Artist.name == artist_name)
        artist_id = list(query)
        return artist_id[0].id
    except:
        raise ArtistNotFound(f'There is no artist named {artist_name}.')

def get_all_artists():
    query = Artist.select()
    return list(query)

def show_artists_art(artist_id):
    artist = Artist.get_or_none(Artist.id == artist_id)
    query = Art.select().join(Artist, on=(Artist.id == Art.artist)).where(Artist.id == artist.id)
    return list(query)

class ArtistError(Exception):
    pass

class ArtistNotFound(Exception):
    pass