import math
import string
from dataclasses import dataclass
from array import *
from typing import List

import element
import main
import node

# @dataclass
from element import element


class Grid:
    elements: list[element]

    def __init__(self, _H, _B, _nh, _nb):
        self.elements = list()
        self.nodes = list()
        self.nodesNumber = list()
        self.H = _H
        self.B = _B
        self.nh = _nh
        self.nb = _nb
        self.nN = self.nh * self.nb
        self.matrix_h = list()
        self.vector_p = list()
        self.c_global = list()
        for i in range(int(math.pow(self.nh, 2))):
            for j in range(int(math.pow(self.nh, 2))):
                self.c_global.append(0)
        self.nE = (self.nh - 1) * (self.nb - 1)
        for i in range(self.nN):
            self.vector_p.append(0)
        for i in range(self.nN * self.nN):
            self.matrix_h.append(0)
        # self.nodes = node.Node(2, 10)
        dh = _H / (_nh - 1)
        db = _B / (_nb - 1)
        iterator = 0
        for x in range(0, self.nb):
            for y in range(0, self.nh):
                if x == 0 or x == self.nb-1 or y == 0 or y == self.nh-1:
                    bound = True
                else: bound = False
                self.nodes.append(node.Node(x * db, y * dh, bound, main.starting_temp))
                self.nodesNumber.append(iterator)
                iterator += 1

        for i in range(0, self.nb - 1):
            for j in range(0, self.nh - 1):
                self.elements.append(
                    element((i * (self.nh - 1)) + j,
                            j + ((self.nh) * i),
                            j + self.nh + ((self.nh) * i),
                            j + self.nh + 1 + ((self.nh) * i),
                            j + 1 + ((self.nh) * i)))

    def nodes_str(self) -> string:
        str = ''
        counter = 0
        for node in range(0, len(self.nodes)):
            str += f'node {counter} \t'
            str += self.nodes.__getitem__(node).__str__()
            str += '\n'
            counter += 1
        return str

    def el_str(self) -> string:
        str = ''
        for el in self.elements:
            str += el.__str__()
            str += '\n'
        return str

    def __str__(self):
        return str(
            f'H={self.H}, B={self.B}, nh={self.nh}, nb={self.nb}, nN={self.nN}, nE={self.nE},'
            f' nodes=\n' + self.nodes_str() + '\n' + self.el_str())
