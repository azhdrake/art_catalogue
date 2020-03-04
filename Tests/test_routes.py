import unittest 
from unittest import TestCase 

from peewee import SqliteDatabase

import database_config
from Models import Art, Artist

from main import app 
import wtforms

# Disable CSRF validation for forms, but only for testing
app.config['WTF_CSRF_ENABLED'] = False

class TestArtRoutes(TestCase):

    def setUp(self):        
        database_config.db_path = 'test_db.sqlite'
        self.database = SqliteDatabase(database_config.db_path, pragmas={'foreign_keys': 1})
        
        self.database.drop_tables([Art, Artist])
        self.database.create_tables([Art, Artist])

        self.test_app = app.test_client() 


    def test_add_artist(self):
        response = self.test_app.post('/artists', data={'name': 'cheese', 'email_address':'whatever@whatever.com'}, follow_redirects=True)
        
        # response is a stream of bytes, decode into a string
        response_text = response.data.decode('utf-8')

        # Is data on page? Could also assert data is in specific HTML elements with a little more work
        # A HTML parser like Beautiful Soup could help https://www.crummy.com/software/BeautifulSoup/bs4/doc/
        self.assertIn('cheese', response_text )
        self.assertIn('whatever@whatever.com', response_text)

        # Flash message shown?
        self.assertIn('The new artist has been added!', response_text)

        # new artist in DB?
        new_artist = Artist.get_or_none(Artist.name=='cheese' and Artist.email_address=='whatever@whatever.com')
        self.assertIsNotNone(new_artist)


    def test_no_duplicate_artist(self):
        self.ats1 = Artist.create(name = 'ats1', email_address = 'art1@artmail.com').save()
        response = self.test_app.post('/artists', data={'name': 'ats1', 'email_address':'dupe@dupe.com'})

        response_text = response.data.decode('utf-8')        
      
        # Flash message?
        self.assertIn('Artist ats1 has already been added.', response_text)
        
        # Still only one artist in DB? 
        artist_count = Artist.select().count()
        self.assertEqual(1, artist_count)

        # artist with duplicate name not added 
        new_artist = Artist.get_or_none(Artist.name=='ats1' and Artist.email_address=='dupe@dupe.com')
        self.assertIsNone(new_artist)



if __name__ == '__main__':
    unittest.main()
    