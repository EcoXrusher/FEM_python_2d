import math

import numpy


class Punkty:

    def __init__(self, points):
        self.weight = list()
        self.nodes = list()
        if points == 2:
            self.nodes.append(-(1/math.sqrt(3)))
            self.weight.append(1)
            self.nodes.append(1/math.sqrt(3))
            self.weight.append(1)
        if points == 3:
            self.nodes.append(-(math.sqrt(3/5)))
            self.weight.append(5/9)
            self.nodes.append(0)
            self.weight.append(8/9)
            self.nodes.append(math.sqrt(3/5))
            self.weight.append(5/9)


def funkcja(x,y) -> float:
    return 5*x*x*y*y + 3*x*y + 6

def calka(Points):
    calkowanie = Punkty(Points)
    suma = 0
    for i in range(len(calkowanie.nodes)):
        for j in range(len(calkowanie.nodes)):
            val = funkcja(calkowanie.nodes.__getitem__(i), calkowanie.nodes.__getitem__(j)) * \
                  calkowanie.weight.__getitem__(i) * calkowanie.weight.__getitem__(j)
            suma += val
    print(suma)
