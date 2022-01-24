import math

import numpy as np

import calkowanie
import element
import lokalny_uklad
import node
import main


def matrixpc(grid):
    # for el in grid.elements:
    #     weights = calkowanie.Punkty(main.PUNKTY_CALKOWANIA).weight
    #     detjUpside = el.detJupside
    #
    #     dx = list()
    #     dy = list()
    #     for i in range (int(math.pow(main.PUNKTY_CALKOWANIA, 2))):
    #         dx.append(list())
    #         dy.append(list())
    #     for i in range(int(math.pow(main.PUNKTY_CALKOWANIA, 2))):
    #         for j in range(4):
    #             dx[i].append(0)
    #             dy[i].append(0)
    #     for i in range(int(math.pow(main.PUNKTY_CALKOWANIA, 2))):
    #         for j in range(4):
    #             dx[i][j] += el.jakobi[0][0] * detjUpside * el.ksi[(i * 4) + j] + el.jakobi[0][1] * detjUpside * el.eta[(i * 4) + j]
    #             dy[i][j] += el.jakobi[1][0] * detjUpside * el.ksi[(i * 4) + j] + el.jakobi[1][1] * detjUpside * el.eta[(i * 4) + j]
    #     tmp1 = list()
    #     tmp2 = list()
    #     e = 0
    #     k = 0
    #     for i in range(int(math.pow(main.PUNKTY_CALKOWANIA,  2))):
    #         for j in range(4):
    #             for x in range(4):
    #                 tmp1.append(dx[i][j] * dx[i][x])
    #                 tmp2.append(dy[i][j] * dy[i][x])
    #     loc_h=list()
    #
    #     for i in range (int(math.pow(main.PUNKTY_CALKOWANIA, 2))):
    #         for j in range(16):
    #             loc_h.append(tmp1[(i*16) + j] + tmp2[(i * 16) + j] * el.detJ * main.K)
    #
    #     for j in range(main.PUNKTY_CALKOWANIA):
    #         weighty = weights[j]
    #         w = 0
    #         for i in range(main.PUNKTY_CALKOWANIA):
    #             for x in range(16):
    #                 loc_h[((j+i) * 16) + x] *= weighty * weights[w]
    #             w += 1
    #
    #     for i in range(int(len(loc_h)/16)):
    #         for j in range(4):
    #             for x in range(4):
    #                 el.h[j][x] += loc_h[(i * 16) +j+x]



    for el in grid.elements:
        weights = calkowanie.Punkty(main.PUNKTY_CALKOWANIA).weight
        # weights.append(weights[0])
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
        if 3 == main.PUNKTY_CALKOWANIA:
            wx = 0
            wy = 0
        for i in range(int(math.pow(main.PUNKTY_CALKOWANIA, 2))):
            for j in range(4):
                if 2 == main.PUNKTY_CALKOWANIA:
                    pcx[i][j] = (el.jakobi[0][0] * el.detJupside) * el.ksi[(i * 4) + j] +\
                                (el.jakobi[0][1] * el.detJupside) * el.eta[(i * 4) + j]
                    pcy[i][j] = el.jakobi[1][0] * el.detJupside * el.ksi[(i * 4) + j] +\
                                el.jakobi[1][1] * el.detJupside * el.eta[(i * 4) + j]
                if 3 == main.PUNKTY_CALKOWANIA:
                    pcx[i][j] = ((el.jakobi[0][0] * el.detJupside) * el.ksi[(i * 4) + j] +\
                                 (el.jakobi[0][1] * el.detJupside) * el.eta[(i * 4) + j]) * math.pow(5/9,2)#weights[wx] * weights[wx]
                    pcy[i][j] = (el.jakobi[1][0] * el.detJupside * el.ksi[(i * 4) + j] + \
                               el.jakobi[1][1] * el.detJupside * el.eta[(i * 4) + j]) * math.pow(5/9,2)#weights[wy] * weights[wy]

            wx += 1
            if i % 3 == 0 and i != 0:
                wy += 1
            if wx == 3:
                wx = 0

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
                    dv[i][j] = ((pcx[k][i] * pcx[k][j]) + (pcy[k][i] * pcy[k][j])) * main.K * el.detJ
                    # if 3 == main.PUNKTY_CALKOWANIA:
                    #     dv[i][j] *= weights[k]
                    el.h[i][j] += dv[i][j]
