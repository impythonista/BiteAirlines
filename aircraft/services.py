import math


class Aircraft(object):
    base_fuel_consumption_per_pax: float = 0.002
    base_fuel_capacity: int = 200
    base_fuel_consumption_capacity: float = 0.80

    def __init__(self, id: int, pax: int = 0) -> None:
        """
        Here we can change base fuel configs as per future changes.
        base_fuel_consumption_per_pax
        base_fuel_capacity
        base_fuel_consumption_capacity
        """
        self.id = id
        self.pax = pax
        # self.base_fuel_consumption_per_pax = base_fuel_consumption_per_pax
        # self.base_fuel_capacity = base_fuel_capacity
        # self.base_fuel_consumption_capacity = base_fuel_consumption_capacity
        self.__capacity = self.__total_capacity()

    @property
    def total_fuel_consumption(self) -> float:
        """
        Returns total fuel consumption by aircraft per minute
        """
        return self.__fuel_consumption_per_minute() + \
            self.__fuel_consumption_increase_by_pax()

    @property
    def maximum_minutes_able_to_fly(self) -> float:
        """
        Returns maximum minutes able to fly
        """
        return self.__capacity / self.total_fuel_consumption

    def __fuel_consumption_per_minute(self) -> float:
        """
        The airplane fuel consumption per minute is the logarithm of the
        airplane id multiplied by 0.80 liters.
        Return -> fuel consumption in ltr
        """
        return math.log(self.id) * self.base_fuel_consumption_capacity

    def __fuel_consumption_increase_by_pax(self) -> float:
        """
        The airplane fuel consumption increase by passenger is
        0.002 liters per minute.
        Return -> fuel consumption in ltr
        """
        return self.base_fuel_consumption_per_pax * self.pax

    def __total_capacity(self) -> int:
        """
        Returns total fuel capacity of aircraft
        """
        return self.id * self.base_fuel_capacity
