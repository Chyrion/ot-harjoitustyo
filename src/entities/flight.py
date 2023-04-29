import datetime
from entities.plane import Plane


class Flight:
    """Class representing a flight log entry"""

    def __init__(self, start: str, destination: str, duration: float, date: datetime.date, plane: Plane):
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
        """

        self._start = start
        self._destination = destination
        self._duration = duration
        self._date = date
        self._plane = plane

    @property
    def start(self):
        return self._start

    @property
    def destination(self):
        return self._destination

    @property
    def date(self):
        return self._date

    @property
    def duration(self):
        return self._duration

    @property
    def plane(self):
        return self._plane

    def to_dict(self):
        """Returns a dict with the start and destination"""
        return {'start': self._start, 'destination': self._destination, 'duration': self._duration, 'date': self._date.isoformat(), 'plane': self._plane.tailnumber}
