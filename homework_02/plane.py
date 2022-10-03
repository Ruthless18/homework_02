"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Plane(Vehicle):
    cargo = None
    max_cargo = None

    def load_cargo(self):
        pass