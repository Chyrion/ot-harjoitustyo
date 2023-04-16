import datetime


class Flight:
    """Class representing a flight log entry"""

    def __init__(self, start: str, destination: str, date: datetime.date):
        """Class constructor

        args:
            start:
                The starting airport of the flight

            destination:
                The destination airport of the flight

            date:
                The date of the flight in datetime.date form
        """

        self._start = start
        self._destination = destination
        self._date = date

    @property
    def start(self):
        return self._start

    @property
    def destination(self):
        return self._destination

    @property
    def date(self):
        return self._date

    def to_dict(self):
        """Returns a dict with the start and destination"""
        return {'start': self._start, 'destination': self._destination, 'date': self._date.isoformat()}
