from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import AircraftSerializer
from .services import Aircraft


class AircraftAPIView(APIView):
    """
    A simple APIView
    """
    def get(self, request: 'Request', aircraft_id: int,
        passenger_count: int) -> 'Response':
        aircraft = Aircraft(int(aircraft_id), int(passenger_count))
        serializer = AircraftSerializer(aircraft)
        return Response(serializer.data, status=status.HTTP_200_OK)
