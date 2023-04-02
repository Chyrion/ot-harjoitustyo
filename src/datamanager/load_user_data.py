class UserDataLoader:
    """Loads user data"""

    def __init__(self, username):
        self._username = username
        self._userdata = None

    def load_user(self, files):
        if self._username in files.userlist():
            print('User found!')
        else:
            print('User not found')
