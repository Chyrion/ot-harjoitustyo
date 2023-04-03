import unittest
import uuid
from datamanager.filemanager import FileManager


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.files = FileManager()
        self.user = str(uuid.uuid4())

    def tearDown(self):
        self.files.delete_user(self.user)

    def test_delete_invalid_user(self):
        delete = self.files.delete_user(str(uuid.uuid4()))
        self.assertFalse(delete)

    def test_brand_new_user(self):
        add_user = self.files.new_user(self.user)
        self.assertTrue(add_user)

    def test_add_existing_user(self):
        self.files.new_user(self.user)
        add = self.files.new_user(self.user)
        self.assertFalse(add)

    def test_userlist_grows_with_new_user(self):
        startlen = len(self.files.userlist)
        self.files.new_user(self.user)
        endlen = len(self.files.userlist)
        self.assertEqual(endlen, startlen+1)

    def test_userlist_doest_grow_with_existing_user(self):
        self.files.new_user(self.user)
        startlen = len(self.files.userlist)
        self.files.new_user(self.user)
        endlen = len(self.files.userlist)
        self.assertEqual(endlen, startlen)
