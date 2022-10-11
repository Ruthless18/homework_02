from abc import ABC
from homework_02.exceptions import (
    LowFuelError,
    NotEnoughFuel,
    )


class Vehicle(ABC):
    def __init__(self, weight = 1000, fuel = 45, fuel_consumption = 11, started = False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started


    def start(self):
        if self.fuel > 0:
            self.started = True
            return self.started
        else:
            raise LowFuelError


    def move(self, max_distance):
        if self.fuel and self.fuel_consumption > 0:
            if self.fuel > self.fuel_consumption:
                if max_distance > 0:
                    self.fuel = self.fuel - max_distance * self.fuel_consumption
                    return self.fuel
            else:
                raise NotEnoughFuel
        else:
            raise NotEnoughFuel
