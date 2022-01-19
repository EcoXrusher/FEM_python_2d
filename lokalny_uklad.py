import math

import calkowanie
import main


def ksztaltKsi(element) -> list():
    ret = list()
    data = list(calkowanie.Punkty(main.PUNKTY_CALKOWANIA).nodes)
    if main.PUNKTY_CALKOWANIA == 3:
        data.append(data[2])
        data.append(data[1])
        data.append(data[0])
        data += calkowanie.Punkty(main.PUNKTY_CALKOWANIA).nodes

        for i in range(main.PUNKTY_CALKOWANIA):
            for j in range(main.PUNKTY_CALKOWANIA):
                ret.append(count1(data.__getitem__((i*3)+j)))
                ret.append(count2(data.__getitem__((i*3)+j)))
                ret.append(count3(data.__getitem__((i*3)+j)))
                ret.append(count4(data.__getitem__((i*3)+j)))
        return ret

    for i in range(len(data)):
        for j in range(len(data)):
            ret.append(count1(data.__getitem__(i)))
            ret.append(count2(data.__getitem__(i)))
            ret.append(count3(data.__getitem__(i)))
            ret.append(count4(data.__getitem__(i)))

    return ret


def ksztaltEta(element) -> list():
    ret = list()
    data = list
    data = calkowanie.Punkty(main.PUNKTY_CALKOWANIA)
    for i in range(len(data.nodes)):
        for j in range(len(data.nodes)):
            # print(data.nodes.__getitem__(j))
            ret.append(count1(data.nodes.__getitem__(j)))
            ret.append(count4(data.nodes.__getitem__(j)))
            ret.append(count3(data.nodes.__getitem__(j)))
            ret.append(count2(data.nodes.__getitem__(j)))
            # print('.')

    # for i in range(int(len(ret)/2)):

    return ret


#wiersz razy realna wspolrzedna/długość. pamietaj o pitagolasie elementu :D
#wtedy mosz macierz [j] i z niej liczy sie det


def count1(val) -> float:
    return -1/4 * (1-val)


def count2(val) -> float:
    return 1/4 * (1-val)


def count3(val) -> float:
    return 1/4 * (1 + val)


def count4(val) -> float:
    return -1/4 * (1 + val)


def printList (list):
    iterations = int(math.pow(len(calkowanie.Punkty(main.PUNKTY_CALKOWANIA).nodes),2))
    for i in range(iterations):
        print(list[i*4:(i*4)+4])

# def f_to_det(node)


def liczDet(grid):
    print('\n\n')
    for el in grid.elements:
        node0 = grid.nodes.__getitem__(el.node[0])
        node1 = grid.nodes.__getitem__(el.node[1])
        node2 = grid.nodes.__getitem__(el.node[2])
        node3 = grid.nodes.__getitem__(el.node[3])
        tmpksi = ksztaltKsi(el)
        tmpeta = ksztaltEta(el)
        el.ksi = list(tmpksi)
        el.eta = list(tmpeta)

        if main.PUNKTY_CALKOWANIA == 2:
            for i in range(4):
                # tmp1 = el.ksi[(2 * 4) + i]
                # el.ksi[(2 * 4) + i] = el.ksi[(3 * 4) + i]
                # el.ksi[(3 * 4) + i] = tmp1
                el.ksi[(2 * 4) + i], el.ksi[(3 * 4) + i] = el.ksi[(3 * 4) + i], el.ksi[(2 * 4) + i]
                el.eta[(2 * 4) + i], el.eta[(3 * 4) + i] = el.eta[(3 * 4) + i], el.eta[(2 * 4) + i]
            # print(f'after swap')
            # printList(el.eta)

        value = list()
        value.append(list())
        value.append(list())
        value[0].append(0)
        value[0].append(0)
        value[1].append(0)
        value[1].append(0)
        for i in range(int(math.pow(main.PUNKTY_CALKOWANIA, 2))):
            for j in range(4):
                value[0][0] += el.ksi[(i * 4) + j] * grid.nodes[el.node[j]].x
                value[0][1] += el.ksi[(i * 4) + j] * grid.nodes[el.node[j]].y
                value[1][0] += el.eta[(i * 4) + j] * grid.nodes[el.node[j]].x
                value[1][1] += el.eta[(i * 4) + j] * grid.nodes[el.node[j]].y


        tmp_det = value[0][0] * value[1][1] - value[0][1] * value[1][0]
        # print(f'det array {tmp_det}')
        el.detJ = tmp_det
        el.jakobi = list(value)
        # print(f' jakobian : {el.detJ}')
        # print(f'jakobi list {el.jakobi}')


        # for i in range(int(math.pow(main.PUNKTY_CALKOWANIA,2))):
        #     print(f'detksi : \n{tmpksi[0+ i*4]} * {node0.x} + {tmpksi[1+ i*4]} * {node1.x} + {tmpksi[2+ i*4]} * {node2.x} + {tmpksi[3+ i*4]} * {node3.x} = {tmpksi[0+ i*4]*node0.x + tmpksi[1+ i*4]*node1.x + tmpksi[2+ i*4]*node2.x + tmpksi[3+ i*4]*node3.x}')
        #     detksi = el.ksi[0+ i*4]*node0.x + el.ksi[1+ i*4]*node1.x + el.ksi[2+ i*4]*node2.x + el.ksi[3+ i*4]*node3.x
        #     detyksi = el.ksi[0 + i * 4] * node0.y + el.ksi[1 + i * 4] * node1.y + el.ksi[2 + i * 4] * node2.y + el.ksi[
        #         3 + i * 4] * node3.y
        #     print(f'detksi = {detksi}')
        #     detxeta = el.eta[0 + i * 4] * node0.x + el.eta[1 + i * 4] * node1.x + el.eta[2 + i * 4] * node2.x + el.eta[
        #         3 + i * 4] * node3.x
        #     deteta = el.eta[0+ i*4]*node0.y + el.eta[1+ i*4]*node1.y + el.eta[2+ i*4]*node2.y + el.eta[3+ i*4]*node3.y
        #     print(f'deteta = {deteta}')
        #
        #     el.pcMatrix.append(detksi)
        #     el.pcMatrix.append(detyksi)
        #     el.pcMatrix.append(detxeta)
        #     el.pcMatrix.append(deteta)
        #
        #     el.detJ.append((detksi * deteta) - (detyksi * detxeta))
        #     print(f'counte det\n{el.detJ[0]} = {detksi} * {deteta}  -  {detyksi} * {detxeta}')
        # detJupside = 0
        # for det in el.detJ:
        detJupside = (1/tmp_det)
        el.detJupside = detJupside
        # print(f'det j upside : {el.detJupside}')

        # if el.element_number == 0:
        #     print('ksi after swap. el 0')
        #     printList(el.ksi)
        # print(el.detJ)
