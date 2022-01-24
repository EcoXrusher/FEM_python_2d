import math

import numpy

import calkowanie
import lokalny_uklad
import main
import node
import vectorp

node_test = 0


def print_global_h(grid):
    for i in range(grid.nN):
        print('[', end='')
        for j in range(grid.nN):
            print("%.2f" % (numpy.around(grid.matrix_h[i * 4] + j, 2)), '  ', end='')
        # print(grid.matrix_h[(i * 4):(i * 4) + grid.nN])
        print(']')


class uni_node:

    def __init__(self):
        self.x0 = -1
        self.x1 = 1
        self.y0 = -1
        self.y1 = 1
        self.boundries = list()
        # self.wboundries = list()

        for i in calkowanie.Punkty(main.PUNKTY_CALKOWANIA).nodes:
            self.boundries.append(0.5 * (1 - i))
            # self.wboundries.app
        # print(f'pc : : : : : : : : : : {self.boundries}')

        # if main.PUNKTY_CALKOWANIA == 2:



def count_hbc(grid):
    uni = uni_node()
    for i in range(grid.nN):
        grid.vector_p[i]=0
    for el in grid.elements:
        node0 = grid.nodes[el.node[0]]
        node1 = grid.nodes[el.node[1]]
        node2 = grid.nodes[el.node[2]]
        node3 = grid.nodes[el.node[3]]
        nodes = list()
        nodes.append(node0)
        nodes.append(node1)
        nodes.append(node2)
        nodes.append(node3)
        tmp = list()
        wall0 = list()
        wall1 = list()
        wall2 = list()
        wall3 = list()

        if 3 == main.PUNKTY_CALKOWANIA:
            weight = calkowanie.Punkty(main.PUNKTY_CALKOWANIA).weight
            # weight.append(weight[2])
            # weight.append(weight[1])
            # weight.append(weight[0])
            # weight.append(weight[0])
            # weight.append(weight[1])
            # weight.append(weight[2])


        det = list()
        det.append(math.sqrt(math.pow(node1.x - node0.x, 2) + math.pow(node1.y - node0.y, 2)) / 2)
        det.append(math.sqrt(math.pow(node2.x - node1.x, 2) + math.pow(node2.y - node1.y, 2)) / 2)
        det.append(math.sqrt(math.pow(node3.x - node2.x, 2) + math.pow(node3.y - node2.y, 2)) / 2)
        det.append(math.sqrt(math.pow(node0.x - node3.x, 2) + math.pow(node0.y - node3.y, 2)) / 2)
        el.hbc=list()
        for i in range(4):
            el.hbc.append(list())
        for i in range(4 * main.PUNKTY_CALKOWANIA):
            el.hbc[0].append(0)
            el.hbc[1].append(0)
            el.hbc[2].append(0)
            el.hbc[3].append(0)
        tmp = list()
        # print('hbc before assigning')
        # print(el.hbc)
        if node0.boundary == True:
            if node1.boundary == True:
                tmp = el.hbc[0]
                # print(len(tmp))
                if 2 == main.PUNKTY_CALKOWANIA:
                    tmp[0] = uni.boundries[0]
                    tmp[1] = uni.boundries[1]
                    #backway
                    tmp[4] = uni.boundries[1]
                    tmp[5] = uni.boundries[0]
                    el.hbc[0] = list(tmp)
                if 3 == main.PUNKTY_CALKOWANIA:
                    tmp[0] = uni.boundries[0]
                    tmp[1] = uni.boundries[2]
                    #mid
                    tmp[4] = uni.boundries[1]
                    tmp[5] = uni.boundries[1]
                    #top
                    tmp[8] = uni.boundries[2]
                    tmp[9] = uni.boundries[0]
                    el.hbc[0] = list(tmp)
                    # print(f'wall 0 el 0 {tmp}')
                wall0 = list(tmp)

                # print(f'wall0 == {wall0}')
                # print(el.hbc)
                # print(f'if 1 :{tmp}')
                tmp = list()
            if node3.boundary == True:
                tmp = el.hbc[3]
                if 2 == main.PUNKTY_CALKOWANIA:
                    tmp[0] = uni.boundries[0]
                    tmp[3] = uni.boundries[1]
                    #backway
                    tmp[4] = uni.boundries[1]
                    tmp[7] = uni.boundries[0]
                if 3 == main.PUNKTY_CALKOWANIA:
                    # print(uni.boundries)
                    tmp[0] = uni.boundries[0]
                    tmp[3] = uni.boundries[2]
                    #mid
                    tmp[4] = uni.boundries[1]
                    tmp[7] = uni.boundries[1]
                    #top
                    tmp[8] = uni.boundries[2]
                    tmp[11] = uni.boundries[0]
                el.hbc[3] = list(tmp)
                wall3 = list(tmp)
                # print(f'if 2 :{tmp}')
                tmp = list()
        if node2.boundary == True:
            if node3.boundary == True:
                tmp = el.hbc[2]
                if 2 == main.PUNKTY_CALKOWANIA:
                    tmp[2] = uni.boundries[1]
                    tmp[3] = uni.boundries[0]
                    #backway
                    tmp[6] = uni.boundries[0]
                    tmp[7] = uni.boundries[1]
                if 3 == main.PUNKTY_CALKOWANIA:
                    # print(uni.boundries)
                    tmp[2] = uni.boundries[0]
                    tmp[3] = uni.boundries[2]
                    #mid
                    tmp[6] = uni.boundries[1]
                    tmp[7] = uni.boundries[1]
                    #top
                    tmp[10] = uni.boundries[2]
                    tmp[11] = uni.boundries[0]
                el.hbc[2] = list(tmp)
                wall2 = list(tmp)
                # print(f'if 3 :{tmp}')
                tmp = list()
            if node1.boundary == True:
                tmp = el.hbc[1]
                if 2 == main.PUNKTY_CALKOWANIA:
                    tmp[1] = uni.boundries[1]
                    tmp[2] = uni.boundries[0]
                    #backway
                    tmp[5] = uni.boundries[0]
                    tmp[6] = uni.boundries[1]
                if 3 == main.PUNKTY_CALKOWANIA:
                    # print(uni.boundries)
                    tmp[1] = uni.boundries[0]
                    tmp[2] = uni.boundries[2]
                    #mid
                    tmp[5] = uni.boundries[1]
                    tmp[6] = uni.boundries[1]
                    #top
                    tmp[9] = uni.boundries[2]
                    tmp[10] = uni.boundries[0]
                el.hbc[1] = list(tmp)
                wall1 = list(tmp)
                # print(f'if 4 :{tmp}')
                tmp = list()

        # print(f'local hbc {el.element_number}')
        # for d in el.hbc:
        #     print(d)

        if 2 == main.PUNKTY_CALKOWANIA:
            eg_sin = [0, 0, 0, 0, 0, 0, 0, 0]
        if 3 == main.PUNKTY_CALKOWANIA:
            eg_sin = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        eg = list()
        for i in range(4):
            eg.append(list(eg_sin))

        tmp1 = list()
        tmp2 = list()
        # print('hbc')
        # print(el.hbc)
        holder = list()
        if el.hbc != eg:
            # print(f'det : {det}')
            c = 0
            # matrix = list()
            # for f in range(4):
            #     matrix.append(list())
            # for e in range(4):
            #     matrix[e] = list(el.hbc[e])
            # print(f'matrix in hbc {matrix}')


            for tab in el.hbc:
                tmp3 = list()
                tmp1 = []
                tmp2 = []
                tmpc = []
                # print("p1", tmp3)
                # print(type(uni.boundries[0]))
                check = uni.boundries[0]
                check1 = uni.boundries[1]
                check2 = uni.boundries[0]
                if 3 == main.PUNKTY_CALKOWANIA:
                    check2 = uni.boundries[2] * weight[1]
                    check *= weight[0]
                    check1 *= weight[0]
                # print(f'if tab{tab}')
                # if (check in tab) or (check1 in tab) or (check2 in tab):
                # if eg != x for x in el.hbc:
                for i in range(4):
                    for j in range(4):
                        if 2 == main.PUNKTY_CALKOWANIA:
                            tmp1.append(tab[i]*tab[j])
                            tmp2.append(tab[i+4]*tab[j+4])
                        if 3 == main.PUNKTY_CALKOWANIA:
                            tmp1.append(tab[i] * tab[j] * weight[0])
                            tmp2.append(tab[i + 4] * tab[j + 4] * weight[1])
                            tmpc.append(tab[i + 8] * tab[j + 8] * weight[0])

                    if len(tmp3) > 0:
                        tmp3 = []
                    for i in range(len(tmp2)):
                        if 2 == main.PUNKTY_CALKOWANIA:
                            tmp3.append((tmp1[i]+tmp2[i])*float(main.alfa)*float(det[c]))
                        if 3 == main.PUNKTY_CALKOWANIA:
                            # print(f' tmp3 append ({tmp1[i]} + {tmp2[i]} + {tmpc[i]}) *{main.alfa} * {det[c]}')
                            tmp3.append((tmp1[i] + tmp2[i] + tmpc[i]) *
                                        float(main.alfa) * float(det[c]))
                    # print(f'tmp3 in local hbc = {tmp3}')
                #dodaj te macierze do siebie i dopisz do elementu
            if len(holder) == 0:
                # for i in range(16):
                for i in range(grid.nN):
                    holder.append(0)
            index = 0
            # print(tmp3)
            # lokalny_uklad.printList(tmp3)
            # print('\n')
            for i in tmp3:
                # print(index)
                holder[index] += i
                index += 1
            c += 1
            el.hbc = list()
            print(f'el {el.element_number}\n holder : {holder}')
            el.hbc = list(holder)
            # print('hbc matrix :')
            # lokalny_uklad.printList(el.hbc)

            # x = list()
            # for i in range(main.PUNKTY_CALKOWANIA):
            #     x.append(list())
            #     for j in range(4):
            #         x.append(0)
            #
            # for i in range(main.PUNKTY_CALKOWANIA):
            #     for j in range(4):
            #         k = # TODO fix this fokin shit

        #SECTION Vector P
            hld3 =list
            tmp0 = list()
            tmp1 = list()
            if len(wall0) > 0:
                tmp0 = wall0[0:4]
                # print(tmp0)
                tmp1 = wall0[4:8]
                if 3 == main.PUNKTY_CALKOWANIA:
                    tmpd = wall0[8:12]
                # print(tmp1)
                for i in range(4):
                    hld = tmp1[i] * main.t_amb
                    # print(f'{tmp1[i]} * {main.t_amb}')
                    hld2 = tmp0[i] * main.t_amb

                    # print(f'{tmp0[i]} * {main.t_amb}')
                    tmp0[i] = hld
                    tmp1[i] = hld2
                    if 3 == main.PUNKTY_CALKOWANIA:
                        hld3 = tmpd[i] * main.t_amb * weight[0]
                        tmpd[i] = hld3
                        tmp0[i] *=weight[0]
                        tmp1[i] *= weight[1]

                # print(f'tmp0 = {tmp0}')
                for i in range(4):
                    tmp0[i] += tmp1[i]
                    if 3 == main.PUNKTY_CALKOWANIA:
                        tmp0[i] += tmpd[i]
                    # print(f'{tmp0[i]} + {tmp1[i]}')
                    tmp0[i] *= det[0] * main.alfa
                    # print(f'{tmp0[i]} *= {det[0]} * {main.alfa}')
                wall0 = list(tmp0)

            tmp0 = list()
            tmp1 = list()
            if len(wall1) > 0:
                if 3 == main.PUNKTY_CALKOWANIA:
                    tmpd = wall1[8:12]
                    hld3=0
                tmp0 = wall1[0:4]
                # print(tmp0)
                tmp1 = wall1[4:8]
                # print(tmp1)

                for i in range(4):
                    hld = tmp1[i] * (main.t_amb)
                    hld2 = tmp0[i] * (main.t_amb)
                    tmp0[i] = hld
                    tmp1[i] = hld2
                    if 3 == main.PUNKTY_CALKOWANIA:
                        hld3 = tmpd[i] * main.t_amb * weight[0]
                        tmpd[i] = hld3
                        tmp0[i] *= weight[0]
                        tmp1[i] *= weight[1]
                for i in range(4):
                    tmp0[i] += tmp1[i]
                    if 3 == main.PUNKTY_CALKOWANIA:
                        tmp0[i] += tmpd[i]
                    tmp0[i] *= det[1] * main.alfa
                wall1 = list(tmp0)

            tmp0 = list()
            tmp1 = list()
            if len(wall2) > 0:
                if 3 == main.PUNKTY_CALKOWANIA:
                    tmpd = wall2[8:12]
                    hld3=0
                tmp0 = wall2[0:4]
                # print(tmp0)
                tmp1 = wall2[4:8]
                # print(tmp1)
                for i in range(4):
                    hld = tmp1[i] * (main.t_amb)
                    hld2 = tmp0[i] * (main.t_amb)
                    tmp0[i] = hld
                    tmp1[i] = hld2
                    if 3 == main.PUNKTY_CALKOWANIA:
                        hld3 = tmpd[i] * main.t_amb * weight[0]
                        tmpd[i] = hld3
                        tmp0[i] *=weight[0]
                        tmp1[i] *= weight[1]
                for i in range(4):
                    tmp0[i] += tmp1[i]
                    if 3 == main.PUNKTY_CALKOWANIA:
                        tmp0[i] += tmpd[i]
                    tmp0[i] *= det[2] * main.alfa
                wall2 = list(tmp0)

            tmp0 = list()
            tmp1 = list()
            if len(wall3) > 0:
                if 3 == main.PUNKTY_CALKOWANIA:
                    tmpd = wall3[8:12]
                    hld3 = 0
                # print(f'wall3 = {wall3}')
                tmp0 = wall3[0:4]
                # print(tmp0)
                tmp1 = wall3[4:8]
                # print(tmp1)
                for i in range(4):
                    hld = tmp1[i] * main.t_amb
                    # print(f'{tmp1[i]} * {main.t_amb}')
                    hld2 = tmp0[i] * main.t_amb
                    # print(f'{tmp0[i]} * {main.t_amb}')
                    tmp0[i] = hld
                    tmp1[i] = hld2
                    if 3 == main.PUNKTY_CALKOWANIA:
                        hld3 = tmpd[i] * main.t_amb * weight[0]
                        tmpd[i] = hld3
                        tmp0[i] *= weight[0]
                        tmp1[i] *= weight[1]

                # print(f'tmp0 = {tmp0}')
                for i in range(4):
                    tmp0[i] += tmp1[i]
                    # print(f'{tmp0[i]} + {tmp1[i]}')
                    if 3 == main.PUNKTY_CALKOWANIA:
                        tmp0[i] += tmpd[i]
                    tmp0[i] *= det[3] * main.alfa
                    # print(f'{tmp0[i]} *= {det[3]} * {main.alfa}')
                # if el.element_number == 0:
                    # tmp0[0], tmp0[3] = tmp0[3], tmp0[0]
                wall3 = list(tmp0)
            tmp = list()
            tmp = [0,0,0,0]
            # print(f'det j = {el.detJ}')
            # print(f'p local for el {el.element_number}:\n'
            #       f'tmp = {tmp}\n'
            #       f'wall0 = {wall0}\n'
            #       f'wall1 = {wall1}\n'
            #       f'wall2 = {wall2}\n'
            #       f'wall3 = {wall3}')
            for i in range(4):
                if(len(wall0) != 0):
                    tmp[i] += wall0[i]
                if (len(wall1) != 0):
                    tmp[i] += wall1[i]
                if(len(wall2) != 0):
                    tmp[i] += wall2[i]
                if(len(wall3) != 0):
                    tmp[i] += wall3[i]
            # print(f'element {el.element_number}\n{wall0}\n{wall1}\n{wall2}\n{wall3}')

            el.vec_p = list(tmp)
            # print('vector p')
            # print(el.vec_p)
            node0_num = el.node[0]
            node1_num = el.node[1]
            node2_num = el.node[2]
            node3_num = el.node[3]
            # print(f'addin {el.vec_p[0]} to global vec_p at index{node0_num} at element {el.element_number}')
            grid.vector_p[node0_num] += el.vec_p[0]
            # print(f'addin {el.vec_p[1]} to global vec_p at index{node1_num}')
            grid.vector_p[node1_num] += el.vec_p[1]
            # print(f'addin {el.vec_p[2]} to global vec_p at index{node2_num}')
            grid.vector_p[node2_num] += el.vec_p[2]
            # print(f'addin {el.vec_p[3]} to global vec_p at index{node3_num}')
            grid.vector_p[node3_num] += el.vec_p[3]
        else:
            el.hbc = list()
            for g in range(grid.nN):
                el.hbc.append(0)
        tmp = list()
        tmp.append(node0_num)
        tmp.append(node1_num)
        tmp.append(node2_num)
        tmp.append(node3_num)
            # print('global h len',len(grid.matrix_h))
            # print(f'local el.h len : {len(el.h)}')
            # max = 0
        # print(f'lokal hbc bef agreg {el.element_number}')
        # print(el.hbc)
        print(el.element_number)
        # array1 = list()
        # for d in range(4):
        #     array1.append(list())
        # array1[0] = list(el.hbc[0:4])
        # array1[1] = list(el.hbc[4:8])
        # array1[2] = list(el.hbc[8:12])
        # array1[3] = list(el.hbc[12:16])

        # print(f'array : {array1}')
        print(f'el hbc : {el.hbc}')
        for i in range(4):
            for j in range(4):
                # grid.matrix_h[(tmp[i] * grid.nN) + tmp[j]] += el.h[i][j]
                # print(f'adding to H {el.hbc[(i*4) + j]}')
                grid.matrix_h[(tmp[i] * grid.nN) + tmp[j]] += el.hbc[(i * 4) + j] #array1[i][j]
            # print('end of element')

    print(f'global p vector :\n {grid.vector_p}')
    print(f'global h matrix :\n')
    counter = 0
    for i in grid.matrix_h:
        if counter == grid.nN:
            print(']')
            counter = 0
        if counter == 0:
            print('[', end='')
        print("%.2f" % (numpy.around(i, 2)), "  ", end='')
        counter += 1
    print(']')
    print()

# def count_p(grid):
#     grid.vector_p = list()
#     for i in range(grid.nN):
#         grid.vector_p.append(0)
#     vec_p = list()
#     for i in range(grid.nN):
#         vec_p.append(0)
#
#     for el in grid.elements:
#         uni = uni_node()
#         points = list(uni.boundries)
#         wall0 = False
#         wall1 = False
#         wall2 = False
#         wall3 = False
#         if grid.nodes[el.node[0]].boundary == True:
#             if grid.nodes[el.node[1]].boundary == True:
#                 wall0 = True
#             if grid.nodes[el.node[3]].boundary == True:
#                 wall3 = True
#         if grid.nodes[el.node[2]].boundary == True:
#             if grid.nodes[el.node[1]].boundary == True:
#                 wall1 = True
#             if grid.nodes[el.node[3]].boundary == True:
#                 wall2 = True
#         tmp_zero = list()
#         for i in range(4):
#             tmp_zero.append(0)
#         array = list()
#         for i in range(main.PUNKTY_CALKOWANIA):
#             array.append(list(tmp_zero))
#
#
#         val = list(tmp_zero)
#         if wall0 == True:
#             if main.PUNKTY_CALKOWANIA == 2:
#                 array[0][0] = points[0]
#                 array[0][1] = points[1]
#                 array[1][0] = points[1]
#                 array[1][1] = points[0]
#             if main.PUNKTY_CALKOWANIA == 3:
#                 array[0][0] = points[0]
#                 array[0][1] = points[2]
#                 array[1][0] = points[1]
#                 array[1][1] = points[1]
#                 array[2][0] = points[2]
#                 array[2][1] = points[0]
#             for i in range(main.PUNKTY_CALKOWANIA):
#                 for j in len(val):
#                     val[j] += array[i][j]
#
#         if wall1 == True:
#             if main.PUNKTY_CALKOWANIA == 2:
#                 array[0][1] = points[0]
#                 array[0][2] = points[1]
#                 array[1][1] = points[1]
#                 array[1][2] = points[0]
#             if main.PUNKTY_CALKOWANIA == 3:
#                 array[0][1] = points[0]
#                 array[0][2] = points[2]
#                 array[1][1] = points[1]
#                 array[1][2] = points[1]
#                 array[2][1] = points[2]
#                 array[2][2] = points[0]
#             for i in range(main.PUNKTY_CALKOWANIA):
#                 for j in len(val):
#                     val[j] += array[i][j]
#
#         if wall2 == True:
#             if main.PUNKTY_CALKOWANIA == 2:
#                 array[0][2] = points[0]
#                 array[0][3] = points[1]
#                 array[1][2] = points[1]
#                 array[1][3] = points[0]
#             if main.PUNKTY_CALKOWANIA == 3:
#                 array[0][2] = points[0]
#                 array[0][3] = points[2]
#                 array[1][2] = points[1]
#                 array[1][3] = points[1]
#                 array[2][2] = points[2]
#                 array[2][3] = points[0]
#             for i in range(main.PUNKTY_CALKOWANIA):
#                 for j in len(val):
#                     val[j] += array[i][j]
#         if wall3 == True:
#             if main.PUNKTY_CALKOWANIA == 2:
#                 array[0][3] = points[0]
#                 array[0][0] = points[1]
#                 array[1][3] = points[1]
#                 array[1][0] = points[0]
#             if main.PUNKTY_CALKOWANIA == 3:
#                 array[0][3] = points[0]
#                 array[0][0] = points[2]
#                 array[1][3] = points[1]
#                 array[1][0] = points[1]
#                 array[2][3] = points[2]
#                 array[2][0] = points[0]
#             for i in range(main.PUNKTY_CALKOWANIA):
#                 for j in len(val):
#                     val[j] += array[i][j]
#         for i in len(val):
#

