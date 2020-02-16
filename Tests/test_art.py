from unittest import TestCase
import peewee
from Models import Art, Artist
from art import *

db = SqliteDatabase('Test_Art.sqlite', pragmas={'foreign_keys': 1})

class TestArt(TestCase):
    def remake_tables(self):
        db.drop_tables([Art, Artist])
        db.create_tables([Art, Artist])
    
    def add_test_data(self):
        Sethany = Artist.create(name = 'Sethany Jeffimmons', email_address = 'Seffimmons@artmail.com')
        Bobrick = Artist.create(name = 'Bobrick Bobberson', email_address = 'Bobs_the_word@artmail.com')
        Jame = Artist.create(name = 'Jame Hopketon', email_address = 'JameH@artmail.com')

        Void = Art.create(artist = 1, name = 'Mostly Void, Partially Stars', price = 0.50, available = True)
        Dark = Art.create(artist = 1, name = 'Dark, Endless, and Impossible to Sleep Through', price = 50.00, available = True)
        Belief = Art.create(artist = 1, name = 'Belief', price = 19.99, available = False)
        Proud = Art.create(artist = 2, name = 'Be Proud For You Are', price = 413.00, available = True)
        Perfection = Art.create(artist = 2, name = 'Perfection is Not Real', price = 612.00, available = False)
        Story = Art.create(artist = 2, name = 'This Isn\'t Your Story, Nor is it Mine', price = 10.25, available = False)
        Jellyfish = Art.create(artist = 3, name = 'Covered In Jellyfish', price = 11.11, available = True)

    def test_add_art_with_empty_artist_table(self):
        with self.assertRaises(ArtError):
            Void = Art(artist = 1, name = 'Mostly Void, Partially Stars', price = 0.50)
            Void.add_art()
