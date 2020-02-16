from peewee import *

db = SqliteDatabase('ArtCat.sqlite', pragmas={'foreign_keys': 1})


class Artist(Model):
    class Meta:
        database = db
        constraints = [SQL('UNIQUE(name COLLATE NOCASE)')]

    name = CharField()
    email_address = CharField()

    def __str__(self):
        return f'ID {self.id}, Name: {self.name}, Email: {self.email_address}'

class Art(Model):
    class Meta:
        database = db
        constraints = [SQL('UNIQUE(name COLLATE NOCASE)')]

    artist = ForeignKeyField(Artist)
    name = CharField()
    price = DoubleField()
    available = BooleanField(default=True)

    def __str__(self):
        available_status = 'is' if self.available else 'is not'
        return f'ID {self.id}, Name: {self.name}, Artist: {self.artist} Price: {self.price}. This piece {available_status} available to buy.'

db.connect()
db.create_tables([Art, Artist])

"""db.drop_tables([Art, Artist])

db.create_tables([Art, Artist])


Sethany = Artist.create(name = 'Sethany Jeffimmons', email_address = 'Seffimmons@artmail.com')
Bobrick = Artist.create(name = 'Bobrick Bobberson', email_address = 'Bobs_the_word@artmail.com')
Jame = Artist.create(name = 'Jame Hopketon', email_address = 'JameH@artmail.com')

Void = Art.create(artist = 1, name = 'Mostly Void, Partially Stars', price = 0.50, available = True)
Dark = Art.create(artist = 1, name = 'Dark, Endless, and Impossible to Sleep Through', price = 50.00, available = True)
Belief = Art.create(artist = 1, name = 'Belief', price = 19.99, available = False)
Proud = Art.create(artist = 2, name = 'Be Proud For You Are', price = 413.00, available = True)
Perfection = Art.create(artist = 2, name = 'Perfection is Not Real', price = 612.00, available = False)
Story = Art.create(artist = 2, name = 'This Isn\'t Your Story, Nor is it Mine', price = 10.25, available = False)
Jellyfish = Art.create(artist = 3, name = 'Covered In Jellyfish', price = 11.11, available = True)"""
