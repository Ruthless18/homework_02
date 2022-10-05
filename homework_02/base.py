from homework_02.exceptions import (
    LowFuelError,
    NotEnoughFuel,
    )

class Vehicle:
    def __init__(self, weight = 1000, fuel = 45, fuel_consumption = 11, started = False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.start()
        self.started = started


    def start(self):
        if self.fuel > 0:
            self.started = True
            return self.started
        else:
            raise LowFuelError


    def move(self):
        max_distance = self.fuel // self.fuel_consumption
        while max_distance > 0:
            for i in range(max_distance):
                self.fuel = self.fuel - self.fuel_consumption
            return self.fuel
        else:
            raise NotEnoughFuel

