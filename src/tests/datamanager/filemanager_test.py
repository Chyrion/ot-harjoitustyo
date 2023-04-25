import unittest
import uuid
from datamanager.filemanager import FileManager
from entities.user import User


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.files = FileManager()
        self.user = User(str(uuid.uuid4()))
        self.username = self.user.username

    def tearDown(self):
        self.files.delete_user(self.user)

    def test_delete_invalid_user(self):
        delete = self.files.delete_user(User(str(uuid.uuid4())))
        self.assertFalse(delete)

    def test_brand_new_user(self):
        add_user = self.files.new_user(self.username)
        self.assertTrue(add_user)

    def test_add_existing_user(self):
        self.files.new_user(self.username)
        add = self.files.new_user(self.username)
        self.assertFalse(add)

    def test_userlist_grows_with_new_user(self):
        startlen = len(self.files.userlist)
        self.files.new_user(self.username)
        endlen = len(self.files.userlist)
        self.assertEqual(endlen, startlen+1)

    def test_userlist_doesnt_grow_with_existing_user(self):
        self.files.new_user(self.username)
        startlen = len(self.files.userlist)
        self.files.new_user(self.username)
        endlen = len(self.files.userlist)
        self.assertEqual(endlen, startlen)

    def test_load_user_data_with_valid_user(self):
        self.files.new_user(self.username)
        self.assertIs(
            type(self.files.load_user_data_from_file(self.username)), User)

    def test_load_user_data_with_invalid_user(self):
        self.assertFalse(
            self.files.load_user_data_from_file(str(uuid.uuid4())))
