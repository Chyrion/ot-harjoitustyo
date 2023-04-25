from entities.flight import Flight


class User:
    '''Class representing a user profile'''

    def __init__(self, username: str):
        '''Class constructor

        args:
            username:
                The username of the user
        '''
        self._username = username
        self._flights: list[Flight] = list()
        self._planes = list()

    @property
    def username(self):
        return self._username

    @property
    def flights(self):
        return self._flights

    @property
    def planes(self):
        return self._planes

    def add_flight(self, flight: Flight):
        '''Adds a flight object to the user's flights list

        args:
            flight:
                Flight object representing the flight to be added
        '''
        self._flights.append(flight)

    def add_plane(self, plane):
        '''Adds a plane to the user's planes list'''
        return

    def user_info(self):
        '''Returns a dictionary with the user's information'''
        return {
            'username': self._username,
            'flights': self._flights,
            'planes': self._planes
        }
