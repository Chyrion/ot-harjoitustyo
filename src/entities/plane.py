class Plane:
    '''A class representing a plane that a user can select to use'''

    def __init__(self, model: str, tailnumber: str):
        self._model = model
        self._tailnumber = tailnumber
        self._hours = 0

    @property
    def model(self):
        return self._model

    @property
    def tailnumber(self):
        return self._tailnumber

    @property
    def hours(self):
        return self._hours

    def add_flight_hours(self, hours: float):
        self._hours += hours
