from homework_02.exceptions import (
    LowFuelError,
    NotEnoughFuel,
    )

class Vehicle:
    def __init__(self, weight = 1000, fuel = 45, fuel_consumption = 11, started = False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started
        self.vehicle = (weight, fuel, fuel_consumption, self.start())
        print("vehicle", self.vehicle)

    def start(self):
        if self.fuel > 0:
            self.started = True
            return self.started
        else:
            raise NotEnoughFuel


    def move(self):
        for self.fuel_consumption in range(self.weight):
            self.fuel = self.fuel - self.fuel_consumption
            return self.fuel
        else:
            raise NotEnoughFuel

Vehicle()
# Vehicle = Vehicle(40, 23, 14)
# print(Vehicle.__dict__)
