from ArtCatDB import Artist
from ArtCatDB import Art

def add_artist(artist):
    try:
        artist.save()
        return True
    except peewee.IntegrityError:
        return False

def get_all_artists():
    query = Artist.select()
    return list(query)

def show_artists_art(artist_id):
    artist = Artist.get_or_none(Artist.id == artist_id)
    query = Art.select().join(Artist, on=(Artist.name == Art.artist)).where(Artist.id == artist.id)
    return list(query)