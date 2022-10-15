"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo= 1213213, cargo = 0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.remove_all_cargo()
        self.max_cargo = max_cargo


    def load_cargo(self, cargo):
        sum_cargo = self.cargo + cargo
        if sum_cargo <= self.max_cargo:
            self.cargo = sum_cargo
            return self.cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        last_cargo = self.cargo
        self.cargo = 0
        return last_cargo


