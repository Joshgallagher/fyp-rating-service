from unittest import TestCase
from app import app
from core.database import database


class BaseTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.database = database.get_db()

    def tearDown(self):
        for collection in self.database.list_collection_names():
            self.database.drop_collection(collection)
