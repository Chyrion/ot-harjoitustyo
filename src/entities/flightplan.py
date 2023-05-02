class FlightPlan:
    '''Class representing a flight plan'''

    def __init__(self, start: str, destination: str):
        '''Class constructor

        args:
            start:
                The starting airport for the flight plan
            destination:
                The destination airport of the flight plan
        '''
        self._start = start
        self._destination = destination

    @property
    def start(self):
        return self._start

    @property
    def destination(self):
        return self._destination

    def text_representation(self):
        '''Returns a text representation of the flight plan'''
        return f'{self.start}-{self.destination}'
