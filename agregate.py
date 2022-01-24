def agregat(grid):
    for el in grid.elements:
        nodes = list()
        nodes.append(el.node[0])
        nodes.append(el.node[1])
        nodes.append(el.node[2])
        nodes.append(el.node[3])
        # print(len(el.hbc[0]))
        for i in range(4):
            for j in range(4):
                # print((nodes[i]*grid.nN) + nodes[j])
                grid.matrix_h[(nodes[i] * grid.nN) + nodes[j]] += el.h[i][j]
                grid.matrix_h[(nodes[i] * grid.nN) + nodes[j]] += el.hbc[i][j] #array1[i][j]
            # print('end of element')
    print('global h:')
    for i in range(grid.nN):
        print('[ ',end='')
        for j in range(grid.nN):
            print(f'{"% .2f" % grid.matrix_h[i * grid.nN + j]} , ', end ='')
        print(' ]')
