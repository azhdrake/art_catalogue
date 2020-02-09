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

""""db.create_tables([Artist])
Sethany = Artist.create(name = 'Sethany Jeffimmons', email_address = 'Seffimmons@artmail.com')
Bobrick = Artist.create(name = 'Bobrick Bobberson', email_address = 'Bobs_the_word@artmail.com')
Jame = Artist.create(name = 'Jame Hopketon', email_address = 'JameH@artmail.com')

Void = Art.create(artist = 'Sethany Jeffimmons', name = 'Mostly Void, Partially Stars', price = 0.50, availble = True)
Dark = Art.create(artist = 'Sethany Jeffimmons', name = 'Dark, Endless, and Impossible to Sleep Through', price = 50.00, availble = True)
Belief = Art.create(artist = 'Sethany Jeffimmons', name = 'Belief', price = 19.99, availble = False)
Proud = Art.create(artist = 'Jame Hopketon', name = 'Be Proud For You Are', price = 413.00, availble = True)
Perfection = Art.create(artist = 'Jame Hopketon', name = 'Perfection is Not Real', price = 612.00, availble = False)
Story = Art.create(artist = 'Jame Hopketon', name = 'This Isn\'t Your Story, Nor is it Mine', price = 10.25, availble = False)
Jellyfish = Art.create(artist = 'Bobrick Bobberson', name = 'Covered In Jellyfish', price = 11.11, availble = True)
""""