import os
import json


class UserDataLoader:
    """Loads user data, assuming the data folder exists"""

    def __init__(self, username: str):
        """Class constructor

        args:
            username:
                The username of the target user
        """
        self._username = username
        self._userdata = None
        self._userfile = os.getcwd() + '/userfiles/' + self._username + \
            '/' + self._username + '.json'

    def load_user(self, files):
        if self._username in files.userlist():
            with open(self._userfile, 'r') as file:
                for line in file:
                    self._userdata = json.dumps(line)
            return self._userdata
        else:
            return False
