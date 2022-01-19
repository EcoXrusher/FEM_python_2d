from dataclasses import dataclass


# @dataclass
class Node:
    # x: float
    # y: float


    def __init__(self, _x, _y, bound,_temp):
        self.x = _x
        self.y = _y
        self.boundary = bound
        self.temp = _temp


    def __str__(self):
        return str(f'x={self.x}, y={self.y}, boundary = {self.boundary}')

