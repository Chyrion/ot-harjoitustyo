class FlightPlan:
    '''Class representing a flight plan'''

    def __init__(self, start: str, destination: str):
        self._start = start
        self._destination = destination

    @property
    def start(self):
        return self._start

    @property
    def destination(self):
        return self._destination

    def text_representation(self):
        return f'{self.start}-{self.destination}'
