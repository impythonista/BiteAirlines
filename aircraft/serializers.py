from rest_framework import serializers


class AircraftSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
    pax = serializers.IntegerField(min_value=0)
    total_fuel_consumption = serializers.DecimalField(
        max_digits=100, decimal_places=2)
    maximum_minutes_able_to_fly = serializers.DecimalField(
        max_digits=100, decimal_places=2)
