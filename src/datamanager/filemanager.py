import os
import shutil
import datetime
import pickle
from entities.flight import Flight
from entities.user import User
from entities.plane import Plane


class FileManager:
    """Manages user data files and folders"""

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
            with open(userpath+'/'+username+'.pkl', 'wb') as file:
                user = User(username)
                pickle.dump(user, file, protocol=pickle.HIGHEST_PROTOCOL)
            return True
        return False

    def delete_user(self, user: User):
        """Deletes a user and their user folder

        args:
            username:
                The username of the user to be deleted
        """
        if user.username in self._userlist:
            shutil.rmtree(self._data_folder_path + '/' + user.username)
            self._get_users()
            return True
        return False

    @property
    def userlist(self):
        return self._userlist

    def load_user_data_from_file(self, username: str):
        """Loads user data

        args:
            username:
                Username of the user as a string
        """

        if username in self._userlist:
            userfile = self._data_folder_path + f'{username}/{username}.pkl'
            with open(userfile, 'rb') as file:
                user: User = pickle.load(file)
                return user
        else:
            return False

    def save_new_flight(self, user: User, start: str, dest: str, duration: float, date: datetime.date, plane: Plane):
        """Saves a new Flight object into the user's data file

        args:
            user:
                User object of the user whose flight is being saved
            start:
                Start airport ICAO
            dest:
                Destination airport ICAO
            duration:
                Duration of the flight in hours as a float value
            date:
                Date of the flight as a datetime.date object
        """

        userfile = self._data_folder_path + \
            f'/{user.username}/{user.username}.pkl'

        user.add_flight(Flight(start, dest, duration,
                        date, plane, len(user.flights)))
        with open(userfile, 'wb') as file:
            pickle.dump(user, file, protocol=pickle.HIGHEST_PROTOCOL)

    def save_new_plane(self, user: User, model: str, year: int, tailnumber: str):
        '''Saves a new Plane object into the user's data file

        args:
            user:
                User's User object
            model:
                Model of the plane
            tailnumber:
                Tailnumber of the plane
        '''

        userfile = self._data_folder_path + \
            f'/{user.username}/{user.username}.pkl'

        user.add_plane(model, year, tailnumber)

        with open(userfile, 'wb') as file:
            pickle.dump(user, file, protocol=pickle.HIGHEST_PROTOCOL)
