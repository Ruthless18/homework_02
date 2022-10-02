from homework_02.exceptions import (
    LowFuelError,
    NotEnoughFuel,
    )


class Vehicle(NotEnoughFuel):
    def __init__(self, weight: int, started: bool, fuel: int, fuel_consumption: int):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self, started, fuel):
         self.started = started
         self.fuel = fuel
         if started == False or fuel > 0:
            return print(started == True)
         else:
            raise NotEnoughFuel


    def move(self):
        for self.fuel_consumption in range(self.weight):
            self.fuel = self.fuel - self.fuel_consumption
            return self.fuel
        else:
            raise NotEnoughFuel


Vehicle = Vehicle(1000, True, 50, 12)
print(Vehicle)
print(Vehicle.__dict__)
