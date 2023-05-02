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
        self._flights.append(flight)
        flight_plane = None
        for _plane in self._planes:
            if _plane.plane_id == flight.plane.plane_id:
                flight_plane = _plane

        flight_plane.add_flight_hours(flight.duration)
        self._hours = self._update_hours()

    def add_plane(self, model: str, year: int, tailnumber: str):
        '''Adds a plane to the user's planes list

        args:
            model:
                Model of the plane
            year:
                Year of the plane
            tailnumber:
                Tailnumber of the plane
        '''
        plane = Plane(model, year, tailnumber, len(self.planes))
        self._planes.append(plane)

    def update_plane(self, plane_id: int, hours: float):
        """Updates plane hours

        args:
            plane_id (int):
                plane_id of the plane
            hours (float):
                hours to be added
        """
        plane = None
        for _plane in self._planes:
            if _plane.plane_id == plane_id:
                plane = _plane
        plane.add_flight_hours(hours)

    def _update_hours(self):
        hours = 0
        if len(self._flights) > 0:
            for flight in self._flights:
                hours += flight.duration
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
