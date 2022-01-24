import math

import calkowanie
import lokalny_uklad
import main

def countshape(el):
    ret = list()
    points = calkowanie.Punkty(main.PUNKTY_CALKOWANIA)
    tru_points = list(points.nodes)
    if 2 == main.PUNKTY_CALKOWANIA:
        eta = list(tru_points)
        eta.append(tru_points[1])
        eta.append(tru_points[0])
        ksi = list()
        ksi.append(tru_points[0])
        ksi.append(tru_points[0])
        ksi.append(tru_points[1])
        ksi.append(tru_points[1])
    if 3 == main.PUNKTY_CALKOWANIA:
        eta = list(tru_points)
        eta.append(tru_points[2])
        eta.append(tru_points[1])
        eta.append(tru_points[0])
        eta.append(tru_points[0])
        eta.append(tru_points[1])
        eta.append(tru_points[2])

        ksi = list()
        ksi.append(tru_points[0])
        ksi.append(tru_points[0])
        ksi.append(tru_points[0])
        ksi.append(tru_points[1])
        ksi.append(tru_points[1])
        ksi.append(tru_points[1])
        ksi.append(tru_points[2])
        ksi.append(tru_points[2])
        ksi.append(tru_points[2])

    # print(tru_points)
    for i in range(int(math.pow(main.PUNKTY_CALKOWANIA, 2))):
        pc_n1 = 0.25 * (1 - eta[i]) * (1 - ksi[i])
        pc_n2 = 0.25 * (1 + eta[i]) * (1 - ksi[i])
        pc_n3 = 0.25 * (1 + eta[i]) * (1 + ksi[i])
        pc_n4 = 0.25 * (1 - eta[i]) * (1 + ksi[i])
        ret.append(pc_n1)
        ret.append(pc_n2)
        ret.append(pc_n3)
        ret.append(pc_n4)
    return ret


def countc(grid):
    c_atr = main.C
    ro_atr = main.ro
    for el in grid.elements:
        det = 0.0
        det_tmp = list()
        hld = [0, 0]
        uni = calkowanie.Punkty(main.PUNKTY_CALKOWANIA).weight
        det_tmp.append(list(hld))
        det_tmp.append(list(hld))
        nodes = list()
        for i in el.node:
            nodes.append(grid.nodes[i])

        for i in range(4):
            det_tmp[0][0] += el.ksi[i] * nodes[i].x
            det_tmp[0][1] += el.ksi[i] * nodes[i].y
            det_tmp[1][0] += el.eta[i] * nodes[i].x
            det_tmp[1][1] += el.eta[i] * nodes[i].y
        det = det_tmp[0][0] * det_tmp[1][1] - det_tmp[0][1] * det_tmp[1][0]

        shape_val = list(countshape(el))
        cp = list()
        holder = list()
        tmp = list()
        row = 0
        counter = 0
        for i in range(int(math.pow(main.PUNKTY_CALKOWANIA, 2))):
            holder = shape_val[(i * 4):(i * 4) + 4]
            tmp = list()
            for j in range(4):
                for x in range(4):
                    if 2 == main.PUNKTY_CALKOWANIA:
                        weight = 1
                    else:
                        weight = uni[i % 3] * uni[row]
                    tmp.append((shape_val[(i * 4) + j] * shape_val[(i * 4) + x]) * c_atr * ro_atr * det * weight)
            if 0 == i:
                el.c_local = list(tmp)
            else:
                for index in range(len(el.c_local)):
                    el.c_local[index] += tmp[index]
            counter += 1
            if counter == 3:
                row += 1
                counter = 0

        tmp = list()
        for i in el.node:
            tmp.append(i)
        for i in range(4):
            for j in range(4):
                grid.c_global[(tmp[i] * grid.nN) + tmp[j]] += el.c_local[(i * 4) + j]
    print("Matrix C : ")
    for i in range(grid.nN):
        print('[ ', end='')
        for j in range(grid.nN):
            print(f'{"%.2f" % grid.c_global[(i*grid.nN) + j]} , ', end='')
        print(']')
