from ArtCatDB import Art
from peewee import IntegrityError

def add_art(art):
    try:
        art.save()
        return True
    except IntegrityError:
        return False

def get_all_art():
    query = Art.select()
    return list(query)

def change_available(art_id):
    art = get_art_by_id(art_id)
    if not art:
        return False
    if art.available == True:
        art.available = False
    else:
        art.available = True
    art.save()
    return True

def delete_art(art_id):
    rows_deleted = Art.delete().where(Art.id == art_id).execute()
    if rows_deleted == 0:
        raise ArtError('Error deleting art piece.')

def get_art_by_id(art_id):
    return Art.get_or_none(Art.id == art_id)

def get_art_by_availability():
    query = Art.select().where(Art.available == True)
    return list(query)

class ArtError(Exception):
    pass