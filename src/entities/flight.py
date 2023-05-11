import datetime
from entities.plane import Plane


class Flight:
    """Class representing a flight log entry"""

    def __init__(self, start: str, destination: str, duration: float, date: datetime.date, plane: Plane, flight_id: int):
        """Class constructor

        args:
            start:
                The starting airport of the flight

            destination:
                The destination airport of the flight

            duration:
                The time duration of the flight

            date:
                The date of the flight in datetime.date form

            plane:
                The plane used in the flight as a Plane object

            flight_id:
                Flight's id. Sequential, obtained with len(user flights)
        """

        self._start = start
        self._destination = destination
        self._duration = duration
        self._flight_date = date
        self._plane = plane
        self._flight_id = flight_id

    @property
    def start(self):
        return self._start

    @property
    def destination(self):
        return self._destination

    @property
    def flight_date(self):
        return self._flight_date

    @property
    def duration(self):
        return self._duration

    @property
    def plane(self):
        return self._plane

    @property
    def flight_id(self):
        return self._flight_id
