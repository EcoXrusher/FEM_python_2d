import numpy
import numpy as np
import scipy

import node
import sim
import vectorp


def run_sim(t0, dt, f_time, grid):
    temp_start = list()
    for i in grid.nodes:
        temp_start.append(t0)
    iterations = int(f_time/dt)
    # for t in range(iterations):
    #     # vectorp.count_hbc(grid)
    #     val = list(grid.vector_p)
    #     for i in range(grid.nN):
    #         for j in range(grid.nN):
    #             node_tmp = grid.nodes[j]
    #             # print(type(node_tmp))
    #             val[i] += (grid.c_global[(i*grid.nN) + j] * node_tmp.temp / dt)
    #
    #     from scipy import linalg
    #     mat_x = list()
    #     for i in range(grid.nN):
    #         mat_x.append(list())
    #         for j in range(grid.nN):
    #             mat_x[i].append(grid.matrix_h[(i * grid.nN) + j])
    #
    #     tempVec = linalg.solve(mat_x, val)
    t = list()
    for tmp in range(grid.nN):
        t.append(grid.nodes[tmp].temp)

    for i in range(iterations):
        print(f'******** iteration {i+1} **************')
        # print(f'******** Matrix H+C/dt ************')
        matrix_h_cdt = list(grid.matrix_h)
        for j in range(len(matrix_h_cdt)):
            matrix_h_cdt[j] += grid.c_global[j]/dt
        # for j in range(grid.nN):
        #     print('[ ', end='')
        #     for k in range(grid.nN):
        #         print("% .2f" % matrix_h_cdt[(j * grid.nN) + k], end='')
        #     print(' ]')

        arr_c_dt = list(grid.c_global)
        for pos in range(len(arr_c_dt)):
            arr_c_dt[pos] = arr_c_dt[pos]/dt

        vec_t = list()
        for x in range(grid.nN):
            vec_t.append(0)

        for j in range(grid.nN):
            for k in range(grid.nN):
                vec_t[j] += arr_c_dt[(j * grid.nN) + k] * t[k]

        vec_p_cdt = list(grid.vector_p)

        for j in range(len(vec_p_cdt)):
            vec_p_cdt[j] += vec_t[j]
        # print('********* vector P C/dt * t0 *********')
        # print(vec_p_cdt, format("% .2f"))
        # grid.vector_p = list(vec_p_cdt)
        from scipy import linalg
        calculate = list()
        tmp = list()
        for x in range(grid.nN):
            for y in range(grid.nN):
                tmp.append(matrix_h_cdt[(x * grid.nN) + y])
            calculate.append(tmp)
            tmp = list()
        cal1 = np.mat(calculate)

        # for x in range(grid.nN):
        #     print('[ ',end='')
        #     for j in range(grid.nN):
        #         print("% .2f" % calculate[x][j], end='')
        #     print(' ]')
        # print(f'vec pcdt t {vec_p_cdt}')
        # if i == 0:
        #     print('h+cdt')
        #     for j in range(grid.nN):
        #         print('[ ',end='')
        #         for x in range(grid.nN):
        #             print("% .2f" % cal1[j, x],end='')
        #         print(' ]')

        tempvec = scipy.linalg.solve(cal1, vec_p_cdt)
        # print(f'vec t \n{tempvec}')
        for x in range(grid.nN):
            t[x] = tempvec[x]
        # print(f'temp vec = {t}')
        print(f'temp max = {max(tempvec)} temp min = {min(tempvec)}')

##############################

        # for i in range(grid.nN):
        #
        #     grid.nodes[i].temp = tempVec[i]
        # print(f'{t*dt}\t max = {max(tempVec)}\t min = {min(tempVec)}')
