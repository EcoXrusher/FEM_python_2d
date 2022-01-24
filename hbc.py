import math

import calkowanie
import main
import vectorp


def c_hbc(grid):
    for el in grid.elements:
        nodes = list()
        nodes.append(grid.nodes[el.node[0]])
        nodes.append(grid.nodes[el.node[1]])
        nodes.append(grid.nodes[el.node[2]])
        nodes.append(grid.nodes[el.node[3]])
        det = list()
        det.append((math.sqrt(math.pow(nodes[1].x-nodes[0].x, 2) + math.pow(nodes[1].y-nodes[0].y, 2))/2))
        det.append((math.sqrt(math.pow(nodes[2].x-nodes[1].x, 2) + math.pow(nodes[2].y-nodes[1].y, 2))/2))
        det.append((math.sqrt(math.pow(nodes[3].x-nodes[2].x, 2) + math.pow(nodes[3].y-nodes[2].y, 2))/2))
        det.append((math.sqrt(math.pow(nodes[3].x-nodes[0].x, 2) + math.pow(nodes[3].y-nodes[0].y, 2))/2))

        uni = vectorp.uni_node()
        uni = uni.boundries
        # print(f'uni : {uni}')
        weights = calkowanie.Punkty(main.PUNKTY_CALKOWANIA).weight
        hbc = list()
        for i in range(4):
            hbc.append(list())
        for i in range(4):
            hbc[0].append(0)
            hbc[1].append(0)
            hbc[2].append(0)
            hbc[3].append(0)
        for i in range(int(math.pow(main.PUNKTY_CALKOWANIA, 2))):
            if nodes[0].boundary == True and nodes[1].boundary == True:
                tmp = list()
                for j in range(4 * main.PUNKTY_CALKOWANIA):
                    tmp.append(0)
                if 2 == main.PUNKTY_CALKOWANIA:
                    tmp[0] = uni[0]
                    tmp[1] = uni[1]
                    tmp[4] = uni[1]
                    tmp[5] = uni[0]
                if 3 == main.PUNKTY_CALKOWANIA:
                    tmp[0] = uni[0]
                    tmp[1] = uni[2]
                    tmp[4] = uni[1]
                    tmp[5] = uni[1]
                    tmp[8] = uni[2]
                    tmp[9] = uni[0]
                arr1 = list()
                arr2 = list()
                if 3 == main.PUNKTY_CALKOWANIA:
                    arr3 = list()
                for x in range(4):
                    arr1.append(list())
                    arr2.append(list())
                    if 3 == main.PUNKTY_CALKOWANIA:
                        arr3.append(list())
                for j in range(4):
                    for k in range(4):
                        arr1[j].append((tmp[j] * tmp[k]) * weights[0])
                        arr2[j].append((tmp[j + 4] * tmp[k + 4]) * weights[1])
                        if 3 == main.PUNKTY_CALKOWANIA:
                            arr3[j].append((tmp[j + 8] * tmp[k] + 8) * weights[2])
                for j in range(4):
                    for k in range(4):
                        tmp = arr1[j][k] + arr2[j][k]
                        if 3 == main.PUNKTY_CALKOWANIA:
                            tmp += arr3[j][k]
                        hbc[j][k] += tmp * main.alfa * det[0]
            if nodes[1].boundary == True and nodes[2].boundary == True:
                tmp = list()
                for j in range(4 * main.PUNKTY_CALKOWANIA):
                    tmp.append(0)
                if 2 == main.PUNKTY_CALKOWANIA:
                    tmp[1] = uni[0]
                    tmp[2] = uni[1]
                    tmp[5] = uni[1]
                    tmp[6] = uni[0]
                if 3 == main.PUNKTY_CALKOWANIA:
                    tmp[1] = uni[0]
                    tmp[2] = uni[2]
                    tmp[5] = uni[1]
                    tmp[6] = uni[1]
                    tmp[9] = uni[2]
                    tmp[10] = uni[0]
                arr1 = list()
                arr2 = list()
                if 3 == main.PUNKTY_CALKOWANIA:
                    arr3 = list()
                for x in range(4):
                    arr1.append(list())
                    arr2.append(list())
                    if 3 == main.PUNKTY_CALKOWANIA:
                        arr3.append(list())
                for j in range(4):
                    for k in range(4):
                        arr1[j].append((tmp[j] * tmp[k])* weights[0])
                        arr2[j].append((tmp[j +4 ] * tmp[k + 4]) * weights[1])
                        if 3 == main.PUNKTY_CALKOWANIA:
                            arr3[j].append((tmp[j + 8] * tmp[k] + 8) * weights[2])
                for j in range(4):
                    for k in range(4):
                        tmp = arr1[j][k] + arr2[j][k]
                        if 3 == main.PUNKTY_CALKOWANIA:
                            tmp += arr3[j][k]
                        hbc[j][k] += tmp * main.alfa * det[1]
            if nodes[2].boundary == True and nodes[3].boundary == True:
                tmp = list()
                for j in range(4 * main.PUNKTY_CALKOWANIA):
                    tmp.append(0)
                if 2 == main.PUNKTY_CALKOWANIA:
                    tmp[2] = uni[0]
                    tmp[3] = uni[1]
                    tmp[6] = uni[1]
                    tmp[7] = uni[0]
                if 3 == main.PUNKTY_CALKOWANIA:
                    tmp[2] = uni[0]
                    tmp[3] = uni[2]
                    tmp[6] = uni[1]
                    tmp[7] = uni[1]
                    tmp[10] = uni[2]
                    tmp[11] = uni[0]
                arr1 = list()
                arr2 = list()
                if 3 == main.PUNKTY_CALKOWANIA:
                    arr3 = list()
                for x in range(4):
                    arr1.append(list())
                    arr2.append(list())
                    if 3 == main.PUNKTY_CALKOWANIA:
                        arr3.append(list())
                for j in range(4):
                    for k in range(4):
                        arr1[j].append((tmp[j] * tmp[k])* weights[0])
                        arr2[j].append((tmp[j + 4] * tmp[k + 4]) * weights[1])
                        if 3 == main.PUNKTY_CALKOWANIA:
                            arr3[j].append((tmp[j + 8] * tmp[k] + 8) * weights[2])
                for j in range(4):
                    for k in range(4):
                        tmp = arr1[j][k] + arr2[j][k]
                        if 3 == main.PUNKTY_CALKOWANIA:
                            tmp += arr3[j][k]
                        hbc[j][k] += tmp * main.alfa * det[2]

            if nodes[0].boundary == True and nodes[3].boundary == True:
                tmp = list()
                for j in range(4 * main.PUNKTY_CALKOWANIA):
                    tmp.append(0)
                if 2 == main.PUNKTY_CALKOWANIA:
                    tmp[3] = uni[0]
                    tmp[0] = uni[1]
                    tmp[7] = uni[1]
                    tmp[4] = uni[0]
                if 3 == main.PUNKTY_CALKOWANIA:
                    tmp[3] = uni[0]
                    tmp[0] = uni[2]
                    tmp[7] = uni[1]
                    tmp[4] = uni[1]
                    tmp[11] = uni[2]
                    tmp[8] = uni[0]
                arr1 = list()
                arr2 = list()
                if 3 == main.PUNKTY_CALKOWANIA:
                    arr3 = list()
                for x in range(4):
                    arr1.append(list())
                    arr2.append(list())
                    if 3 == main.PUNKTY_CALKOWANIA:
                        arr3.append(list())
                hld = list()
                hld.append(list(tmp[0:4]))
                hld.append(list(tmp[4:8]))
                if 3 == main.PUNKTY_CALKOWANIA:
                    hld.append(list(tmp[8:12]))
                for j in range(4):
                    for k in range(4):
                        arr1[j].append(hld[0][j] * hld[0][k] * weights[0])
                        arr2[j].append((hld[1][j] * hld[1][k]) * weights[1])
                        if 3 == main.PUNKTY_CALKOWANIA:
                            arr3[j].append((hld[2][j] * hld[2][k]) * weights[2])
                for j in range(4):
                    for k in range(4):
                        tmp = arr1[j][k] + arr2[j][k]
                        if 3 == main.PUNKTY_CALKOWANIA:
                            tmp += arr3[j][k]
                        hbc[j][k] += tmp * main.alfa * det[3]
        el.hbc = list(hbc)
        print(f'new hbc calculus el{el.element_number}\n{el.hbc}')
