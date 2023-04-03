class Flight:
    """Class representing a flight log entry"""

    def __init__(self, start: str, destination: str):
        """Class constructor

        args:
            start:
                The starting airport of the flight

            destination:
                The destination airport of the flight
        """

        self._start = start
        self._destination = destination

    @property
    def start(self):
        return self._start

    @property
    def destination(self):
        return self._destination

    def to_dict(self):
        """Returns a dict with the start and destination"""
        return {'start': self.start, 'destination': self.destination}
