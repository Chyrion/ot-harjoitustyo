import os
import json


class FileManager:
    """Manages user data files and folder"""

    def __init__(self):
        self._workingdirectory = os.getcwd()
        self._data_folder_path = None
        self._userlist = []

        self._get_data_folder()
        self._get_users()

    def _get_data_folder(self):
        """Gets the main data folder which contains user data folders"""

        data_folder_exists = os.path.isdir('userfiles')
        if not data_folder_exists:
            os.mkdir('userfiles')
        self._data_folder_path = self._workingdirectory + '/userfiles/'

    def _get_users(self):
        """Gets user folders, which are named after each user"""

        self._userlist = next(os.walk(self._data_folder_path))[1]

    def new_user(self, username):
        """Adds a new user by creating a folder for the user and adding them to the userlist

        args:
            username:
                The username of the new user
        """

        if username not in self._userlist:
            os.mkdir(self._data_folder_path + '/' + username)
            self._userlist.append(username)
            userpath = self._data_folder_path + '/' + username
            with open(userpath+'/'+username+'.json', 'w') as file:
                data = {
                    'username': username
                }
                json.dump(data, file)
            return True
        else:
            return False

    def delete_user(self, username):
        """Deletes a user and their user folder

        args:
            username:
                The username of the user to be deleted
        """
        if username in self._userlist:
            os.rmdir(self._data_folder_path + '/' + username)
            self._get_users()
            return True
        else:
            return False

    def userlist(self):
        return self._userlist

    def load_user_data(self, username):
        """Loads user data"""
        if username in self._userlist:
            userfile = self._data_folder_path + f'/{username}/{username}.json'
            with open(userfile, 'r') as file:
                return json.load(file)
        else:
            return False

    def save_user_data(self, username):
        """Saves user data"""
        if username not in self._userlist:
            self.new_user(username)
            return True
        return False
