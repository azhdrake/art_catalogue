from model import *

def add_art(art):
    try:
        art.save()
        return True
    except peewee.IntegrityError:
        return False

def show_all_art():
    query = Art.select()
    return list(query)

def change_available(art_id, availability):
    art = get_art_by_id(art_id)
    if not art:
        return False
    art.available = availability
    art.save()
    return True)

def delete_art(art):
    rows_deleted = Art.delete().where(Art.id == art.id).execute()
    if rows_deleted == 0:
        raise ArtError('Error deleting art piece.')

def get_art_by_id(art_id):
    return Art.get_or_none(Art.id == art_id)

class ArtError(Exception):
    pass