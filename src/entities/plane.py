class Plane:
    '''A class representing a plane that a user can select to use'''

    def __init__(self, model: str, year: int, tailnumber: str):
        self._model = model
        self._tailnumber = tailnumber
        self._year = year
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

    @property
    def year(self):
        return self._year

    def add_flight_hours(self, hours: float):
        self._hours += hours

    @property
    def plane_info(self):
        return {
            'model': self._model,
            'year': self._year,
            'tailnumber': self._tailnumber,
            'hours': self._hours
        }
