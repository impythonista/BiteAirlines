from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from ..services import Aircraft
from ..serializers import AircraftSerializer


class GetAircraftDetailTest(TestCase):
    """ Test module for GET aircraft detail API """
    def setUp(self) -> None:
        self.client = Client()

    def test_get_aircraft_detail(self) -> None:
        # get API response
        response = self.client.get(reverse('aircraft', args=[45, 30]))
        # get data from service
        aircraft = Aircraft(id=45, pax=30)
        serializer = AircraftSerializer(aircraft)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
