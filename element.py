import threading


class element:

    def __init__(self, el_number, node1, node2, node3, node4):
        self.node = list()
        self.node.append(node1)
        self.node.append(node2)
        self.node.append(node3)
        self.node.append(node4)
        self.element_number = el_number
        self.ksi = list()
        self.eta = list()
        self.detJ = 0.0
        self.val = 0
        self.detJupside = 0.0
        self.jakobi = list()
        self.pcMatrix = list()
        self.hx = list()
        self.hy = list()
        self.hpc = list()
        self.h = list()
        # for i in range(4):
        #     self.h.append(list())
        # for i in range(4):
        #     self.h[0].append(0)
        #     self.h[1].append(0)
        #     self.h[2].append(0)
        #     self.h[3].append(0)

        self.hbc = list()
        self.vec_p = list()
        self.c_local = list()

    def __str__(self):
        return str(
            f'element number {self.element_number} : NODES : {self.node.__getitem__(0)}\t{self.node.__getitem__(1)}\t'
            f'{self.node.__getitem__(2)}\t{self.node.__getitem__(3)}')
