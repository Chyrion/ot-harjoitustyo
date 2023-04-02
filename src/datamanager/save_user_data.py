class UserDataSaver:
    """Saves user data"""

    def __init__(self, username):
        self._username = username

    def save_to_file(self, files):
        if self._username not in files.userlist():
            files.new_user(self._username)
        return
