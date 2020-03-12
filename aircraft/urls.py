from django.urls import path
from .views import AircraftAPIView

# Wire up API using automatic URL routing.
urlpatterns = [
    path(
        'aircraft/<int:aircraft_id>/<int:passenger_count>/',
        AircraftAPIView.as_view(),
        name='aircraft'
    ),
]
