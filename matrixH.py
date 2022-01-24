import math

import numpy as np

import calkowanie
import element
import lokalny_uklad
import node
import main


def matrixpc(grid):
    for el in grid.elements:
        node1 = el.node[0]
        node2 = el.node[1]
        node3 = el.node[2]
        node4 = el.node[3]
        if main.PUNKTY_CALKOWANIA == 3:
            weights = list(calkowanie.Punkty(main.PUNKTY_CALKOWANIA).weight)
            for i in range(3):
                weights.append(weights[2-i])
            weights.append(weights[0])
            weights.append(weights[1])
            weights.append(weights[2])
            weightsy = list()
            for i in range(3):
                for j in range(3):
                    weightsy.append(weights[i])
        detJ = el.detJupside
        tmp = list()

        pcx = list()
        pcy = list()
        tmp = list()
        for i in range(4):
            tmp.append(0)
        for i in range(int(math.pow(main.PUNKTY_CALKOWANIA, 2))):
            pcx.append(list(tmp))
            pcy.append(list(tmp))

        # print(el.jakobi)

        for i in range(int(math.pow(main.PUNKTY_CALKOWANIA, 2))):
            for j in range(4):
                if 2 == main.PUNKTY_CALKOWANIA:
                    pcx[i][j] = (el.jakobi[0][0] * el.detJupside) * el.ksi[(i * 4) + j] + (el.jakobi[0][1] * el.detJupside) * el.eta[(i * 4) + j]
                    # if el.element_number == 0:
                        # print(f'finder\n{pcx[i][j]} = {el.jakobi[0][0] * el.detJupside} * {el.ksi[(i * 4) + j]} + {el.jakobi[0][1] * el.detJupside} * {el.eta[(i * 4) + j]}')
                    pcy[i][j] = el.jakobi[1][0] * el.detJupside * el.ksi[(i * 4) + j] + el.jakobi[1][1] * el.detJupside * el.eta[(i * 4) + j]
                if 3 == main.PUNKTY_CALKOWANIA:
                    pcx[i][j] = (el.jakobi[0][0] * el.detJupside) * el.ksi[(i * 4) + j] + (
                               el.jakobi[0][1] * el.detJupside) * el.eta[(i * 4) + j] * weights[i]
                    pcy[i][j] = el.jakobi[1][0] * el.detJupside * el.ksi[(i * 4) + j] + \
                               el.jakobi[1][1] * el.detJupside * el.eta[(i * 4) + j] * weights[j]

        tmp_zero = list()
        for i in range(4):
            tmp_zero.append(0.0)
        dv = list()
        for i in range(4):
            dv.append(list(tmp_zero))
        # print(f'start h len : {len(el.h)}')
        for i in range(4):
            el.h.append(list(tmp_zero))
        # print('startowa h')
        # for i in el.h:
        #     print(i)
        # check = 0
        for k in range(int(math.pow(main.PUNKTY_CALKOWANIA, 2))):
            # print(f'pc {k+1}')
            for i in range(4):
                for j in range(4):
                    # print(f'dv = {pcx[k][i]} * {pcx[k][j]} + {pcy[k][i]} * {pcy[k][j]} * {main.K} * {el.detJ}')
                    dv[i][j] = ((pcx[k][i] * pcx[k][j]) + (pcy[k][i] * pcy[k][j])) * main.K * el.detJ
                    if 3 == main.PUNKTY_CALKOWANIA:
                        dv[i][j] *= weights[k]# * weights[k]                    # print(f'{dv[i][j]} ', end='')
                    # if i == 0 and j == 0:
                    #     check += dv[i][j]
                    # print(f'appenduje h {dv[i][j]}')
                    el.h[i][j] += dv[i][j]
                # print()
            # print()
        # print('h lokalna')
        # print(f'check {check}')
        # for i in el.h:
        #     print(i)

       #comment start
        # hxs = list()
        # hys = list()
        # print('hx counting')
        # for pc in range(int(pow(main.PUNKTY_CALKOWANIA, 2))):
        #     for i in range(4):
        #         for j in range(4):
        #             hxs.append(pcx[pc][i] * pcx[pc][j])
        #             print(f'{pcx[pc][i]} * {pcx[pc][j]}')
        #             hys.append(pcy[pc][i] * pcy[pc][j])
        #     li = list()
        #     for num in range(len(hxs)):
        #         # print(f'sum hpc to local sum h\n{main.K} * {el.detJ} * ({hxs[num]} + {hys[num]})')
        #         li.append(main.K * el.detJ * (hxs[num] + hys[num]))
        #     if el.element_number == 0:
        #         print('lokal li')
        #         lokalny_uklad.printList(li)
        #     el.hpc.append(list(li))
        # if el.element_number == 0:
        #     print('el 0 hbibis\n')
        #     for i in range(4):
        #         lokalny_uklad.printList(el.hpc[i])
        #         print('\n')
        # h = list(el.h[0])
        # # if el.element_number == 0:
        # #     print(f'el 0 matrix H PC1 :\n')
        # #     lokalny_uklad.printList(el.hpc[0])
        # #     print('hpc matrixes')
        # #     for i in range(len(el.hpc)):
        # #         lokalny_uklad.printList(el.hpc[i])
        # #         print('\n')
        #
        # print('eye debug')
        # for i in range(4):
        #     print('\n')
        #     lokalny_uklad.printList(el.hpc[i])
        #
        # for i in range(1,len(el.h)):
        #     for j in range(4):
        #         h[(i* 16) + j] += el.hpc[i][j]
        # el.h = h
        # if el.element_number == 0:
        #     print(f'el 0 matrix H :\n')
        #     lokalny_uklad.printList(el.h)
