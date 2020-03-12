from django.test import TestCase
from ..services import Aircraft


class AircraftTest(TestCase):
    """ Test module for Aircraft service """

    def setUp(self) -> None:
        self.aircraft = Aircraft(id=45, pax=30)

    def test_aircraft(self) -> None:
        aircraft_fuel_cons = self.aircraft.total_fuel_consumption
        aircraft_max_min = self.aircraft.maximum_minutes_able_to_fly
        self.assertTrue(isinstance(aircraft_fuel_cons, float))
        self.assertTrue(isinstance(aircraft_max_min, float))
