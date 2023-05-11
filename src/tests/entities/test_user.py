import unittest
import datetime
from entities.flight import Flight
from entities.plane import Plane
from entities.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.plane = Plane('Model', 2000, 'TAIL-N', 0)
        self.user = User('TestUser', planes=[self.plane])

    def test_user_properties_correct(self):
        user = User('PropertyUser')
        self.assertEqual(user.username, 'PropertyUser')
        self.assertIsNotNone(user.flights)
        self.assertIsNotNone(user.flightplans)
        self.assertIsNotNone(user.planes)
        self.assertEqual(user.hours, 0)

    def test_add_flight_adds_to_flightlist(self):
        flightlist_start_length = len(self.user.flights)
        flight_to_add = Flight('Start', 'Dest', 1.5,
                               datetime.datetime.now().date(), self.plane, 0)
        self.user.add_flight(flight_to_add)
        flightlist_end_length = len(self.user.flights)

        self.assertGreater(flightlist_end_length, flightlist_start_length)

    def test_hours_increase_with_new_flight(self):
        hours_start = self.user.hours

        flight_to_add = Flight('Start', 'Dest', 1.5,
                               datetime.datetime.now().date(), self.plane, 0)
        self.user.add_flight(flight_to_add)

        hours_end = self.user.hours
        self.assertGreater(hours_end, hours_start)
        self.assertEqual(self.user.hours, 1.5)

    def test_sorting_flights(self):
        plane_2 = Plane('Plane2', 2000, 'TAIL-A', 1)
        self.user.add_plane(plane_2.model, plane_2.year, plane_2.tailnumber)
        date_1 = '1900-01-01'
        date_2 = '2000-01-01'
        flight_1 = Flight('Flight1', 'Dest1', 0, datetime.datetime.fromisoformat(
            date_1).date(), self.plane, 0)
        flight_2 = Flight('Flight2', 'AAA', 5, datetime.datetime.fromisoformat(
            date_2).date(), plane_2, 1)

        self.user.add_flight(flight_1)
        self.user.add_flight(flight_2)

        self.assertEqual(self.user.flights[0].start, 'Flight1')

        self.user.sort_flights('Start')
        self.assertEqual(self.user.flights[0].start, 'Flight1')

        self.user.sort_flights('Destination')
        self.assertEqual(self.user.flights[0].start, 'Flight2')

        self.user.sort_flights('Duration')
        self.assertEqual(self.user.flights[0].start, 'Flight1')

        self.user.sort_flights('Date')
        self.assertEqual(self.user.flights[0].start, 'Flight1')

        self.user.sort_flights('Plane')
        self.assertEqual(self.user.flights[0].start, 'Flight2')

        self.user.sort_flights('Added')
        self.assertEqual(self.user.flights[0].start, 'Flight1')

        self.user.sort_flights('Notanoptionmerelya    test')
        self.assertEqual(self.user.flights[0].start, 'Flight1')
