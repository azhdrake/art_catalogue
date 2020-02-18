from unittest import TestCase
from peewee import *

import database_config
database_config.db_path = 'test_db.sqlite'
database = SqliteDatabase(database_config.db_path, pragmas={'foreign_keys': 1})

from Models import Art, Artist
from artist import *

class TestArtist(TestCase):
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

    def test_add_artist_empty_database(self):
        self.remake_tables()

        ats1 = Artist(name = 'ats1', email_address = 'ats@art.com')
        add_artist(ats1)

        fetch_artist = Artist.select().where(Artist.name == 'ats1')

        self.assertTrue(ats1 == fetch_artist[0])

    def test_add_artist_not_empty_database(self):
        self.remake_tables()

        ats1 = Artist(name = 'ats1', email_address = 'ats@art.com')
        add_artist(ats1)
        ats2 = Artist(name = 'ats2', email_address = 'ats@art.com')
        add_artist(ats2)

        fetch_ats2 = Artist.select().where(Artist.name == 'ats2')

        self.assertTrue(ats2 == fetch_ats2[0])

    def test_add_artist_with_duplicate_name(self):
        self.remake_tables()

        ats1 = Artist(name = 'ats1', email_address = 'ats@art.com')
        add_artist(ats1)
        ats2 = Artist(name = 'ats1', email_address = 'ats@art.com')
        
        with self.assertRaises(ArtistError):
            add_artist(ats2)

    def test_add_artist_missing_data(self):
        self.remake_tables()

        ats1 = Artist(name = 'ats1')
        with self.assertRaises(ArtistError):
            add_artist(ats1)