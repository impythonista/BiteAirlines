from django.urls import include, path
from rest_framework import routers
from .views import AircraftViewSet

router = routers.DefaultRouter()
router.register(
    r'aircraft/(?P<aircraft_id>\d+)/(?P<passenger_count>\d+)',
    AircraftViewSet,
    basename='aircraft'
)


# Wire up API using automatic URL routing.
urlpatterns = [
    path('api/', include(router.urls)),
]
