from unittest import TestCase
import peewee 

db = SqliteDatabase('Test_Art.sqlite', pragmas={'foreign_keys': 1})