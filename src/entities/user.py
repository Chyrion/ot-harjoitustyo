from entities.flight import Flight
from entities.plane import Plane


class User:
    '''Class representing a user profile'''

    def __init__(self, username: str, flights: list[Flight] = None, planes: list[Plane] = None):
        '''Class constructor

        args:
            username:
                The username of the user
        '''
        self._username = username
        if flights is None:
            self._flights = []
        else:
            self._flights = flights
        if planes is None:
            self._planes = []
        else:
            self._planes = planes
        self._hours = self._update_hours()

    @property
    def username(self):
        return self._username

    @property
    def flights(self):
        return self._flights

    @property
    def planes(self):
        return self._planes

    @property
    def hours(self):
        return self._hours

    def add_flight(self, flight: Flight):
        '''Adds a flight object to the user's flights list

        args:
            flight:
                Flight object representing the flight to be added
        '''
        flight = flight.to_dict()
        self._flights.append(flight)
        flight.plane.add_flight_hours(flight.duration)
        self._hours = self._update_hours()

    def add_plane(self, model: str, year: int, tailnumber: str):
        '''Adds a plane to the user's planes list'''
        plane = Plane(model, year, tailnumber)
        self._planes.append(plane.plane_info)

    def _update_hours(self):
        hours = 0
        if len(self._flights) > 0:
            for flight in self._flights:
                hours += flight['duration']
        return round(hours, 3)

    @property
    def user_info(self):
        '''Returns a dictionary with the user's information'''
        return {
            'username': self._username,
            'hours': self._hours,
            'flights': self._flights,
            'planes': self._planes
        }
