from unittest import TestCase
from peewee import *

import database_config
database_config.db_path = 'test_db.sqlite'
database = SqliteDatabase(database_config.db_path, pragmas={'foreign_keys': 1})

from Models import Art, Artist
from art import *


class TestArt(TestCase):
    def remake_tables(self):
        database.drop_tables([Art, Artist])
        database.create_tables([Art, Artist])
    
    def add_test_data(self):
        self.ats1 = Artist.create(name = 'ats1', email_address = 'Seffimmons@artmail.com')
        self.ats2 = Artist.create(name = 'ats2', email_address = 'Bobs_the_word@artmail.com')
        self.ats3 = Artist.create(name = 'ats3', email_address = 'JameH@artmail.com')

        self.art1 = Art.create(artist = 1, name = 'art1', price = 0.50, available = True)
        self.art2 = Art.create(artist = 1, name = 'art2', price = 50.00, available = True)
        self.art3 = Art.create(artist = 1, name = 'art3', price = 19.99, available = False)

    def test_add_art_with_empty_artist_table(self):
        self.remake_tables()
        with self.assertRaises(ArtError):
            art1 = Art(artist = 1, name = 'art1', price = 0.50)
            add_art(art1)

    def test_add_art_with_existing_artist(self):
        self.remake_tables()

        Sethany = Artist.create(name = 'ats1', email_address = 'Seffimmons@artmail.com')
        art1 = Art(artist = 1, name = 'art1', price = 0.50)
        
        add_art(art1)
        fetch_art = Art.select().where(Art.name == 'art1')

        print(fetch_art)
        self.assertTrue(art1 == fetch_art[0], msg=f'{art1} is not the same as {fetch_art}')
        
    def test_add_art_with_ununique_name(self):
        self.remake_tables()
        self.add_test_data()

        art1 = Art(artist = 1, name = 'art1', price = 0.50)
        
        with self.assertRaises(ArtError):
            add_art(art1)

    def test_add_art_with_missing_data(self):
        self.remake_tables()

        art1 = Art(artist = 1, name = 'art1')

        with self.assertRaises(ArtError):
            add_art(art1)
    
