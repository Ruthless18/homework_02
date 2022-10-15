"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    def __init__(self, volume = 1, pistons = 10):
        self.volume = volume
        self.pistons = pistons