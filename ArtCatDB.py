from peewee import *

db = SqliteDatabase('ArtCat.sqlite')

class Art(Model):
    class Meta:
        database = db

    artist = CharField()
    name = CharField()
    price = DoubleField()
    availble = BooleanField()


class Artist(Model):
    class Meta:
        database = db

    name = CharField()
    email_address = CharField()


db.connect()
#db.create_tables([Artist])


    

"""Your app needs to save this data about each artist:

name
email address
and data about the artworks:

artist
name of artwork - each artist's artwork has a unique name
price
whether the artwork is available, or if it has been sold """