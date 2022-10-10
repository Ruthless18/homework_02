"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


# class Plane(Vehicle):
#     def __init__(self, max_cargo):
#         self.cargo = None
#         super().__init__(max_cargo = max_cargo)
#         self.load_cargo(max_cargo)
#         self.remove_all_cargo()
#
#     def load_cargo(self, max_cargo):
#         if self.cargo < max_cargo:
#             return self.cargo
#         else:
#             raise CargoOverload
#
#
#     def remove_all_cargo(self):
#         main_cargo = self.cargo
#         self.cargo = 0
#         return main_cargo
#

