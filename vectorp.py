import math
import calkowanie
import main


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


def count_vetor_p(grid):
    for el in grid.elements:
        uni = uni_node().boundries
        nodes = list()
        nodes.append(el.node[0])
        nodes.append(el.node[1])
        nodes.append(el.node[2])
        nodes.append(el.node[3])
        det = list()
        det.append((math.sqrt(math.pow(grid.nodes[nodes[1]].x - grid.nodes[nodes[0]].x, 2) +
                              math.pow(grid.nodes[nodes[1]].y - grid.nodes[nodes[0]].y, 2)) / 2))
        det.append((math.sqrt(math.pow(grid.nodes[nodes[2]].x - grid.nodes[nodes[1]].x, 2) +
                              math.pow(grid.nodes[nodes[2]].y - grid.nodes[nodes[1]].y, 2)) / 2))
        det.append((math.sqrt(math.pow(grid.nodes[nodes[3]].x - grid.nodes[nodes[2]].x, 2) +
                              math.pow(grid.nodes[nodes[3]].y - grid.nodes[nodes[2]].y, 2)) / 2))
        det.append((math.sqrt(math.pow(grid.nodes[nodes[3]].x - grid.nodes[nodes[0]].x, 2) +
                              math.pow(grid.nodes[nodes[3]].y - grid.nodes[nodes[0]].y, 2)) / 2))

        weights = calkowanie.Punkty(main.PUNKTY_CALKOWANIA).weight
        loc_p = list()
        loc_p.append(0)
        loc_p.append(0)
        loc_p.append(0)
        loc_p.append(0)
        vec = list()
        vec2 = list()
        if 3 == main.PUNKTY_CALKOWANIA:
            vec3 = list()
        if grid.nodes[nodes[0]].boundary and grid.nodes[nodes[1]].boundary:
            if 2 == main.PUNKTY_CALKOWANIA:
                vec.append(uni[0])
                vec.append(uni[1])
                vec.append(0)
                vec.append(0)
                vec2.append(uni[1])
                vec2.append(uni[0])
                vec2.append(0)
                vec2.append(0)
            if 3 == main.PUNKTY_CALKOWANIA:
                vec.append(uni[0])
                vec.append(uni[2])
                vec.append(0)
                vec.append(0)
                vec2.append(uni[1])
                vec2.append(uni[1])
                vec2.append(0)
                vec2.append(0)
                vec3.append(uni[2])
                vec3.append(uni[0])
                vec3.append(0)
                vec3.append(0)
            tmp = list()
            for x in range(main.PUNKTY_CALKOWANIA):
                tmp.append(list())
            tmp[0] = vec
            tmp[1] = vec2
            if 3 == main.PUNKTY_CALKOWANIA:
                tmp[2] = vec3
            for i in range(4):
                loc_p[i] += (tmp[0][i] * main.t_amb) * weights[0] + (tmp[1][i] * main.t_amb) * weights[1]
                if 3 == main.PUNKTY_CALKOWANIA:
                    loc_p[i] += (tmp[2][i] * main.t_amb) * weights[2]

        vec = list()
        vec2 = list()
        if 3 == main.PUNKTY_CALKOWANIA:
            vec3 = list()
        if grid.nodes[nodes[1]].boundary and grid.nodes[nodes[2]].boundary:
            if 2 == main.PUNKTY_CALKOWANIA:
                vec.append(0)
                vec.append(uni[0])
                vec.append(uni[1])
                vec.append(0)
                vec2.append(0)
                vec2.append(uni[1])
                vec2.append(uni[0])
                vec2.append(0)
            if 3 == main.PUNKTY_CALKOWANIA:
                vec.append(0)
                vec.append(uni[2])
                vec.append(uni[0])
                vec.append(0)
                vec2.append(0)
                vec2.append(uni[1])
                vec2.append(uni[1])
                vec2.append(0)
                vec3.append(0)
                vec3.append(uni[0])
                vec3.append(uni[2])
                vec3.append(0)
            tmp = list()
            for x in range(main.PUNKTY_CALKOWANIA):
                tmp.append(list())
            tmp[0] = vec
            tmp[1] = vec2
            if 3 == main.PUNKTY_CALKOWANIA:
                tmp[2] = vec3
            for i in range(4):
                loc_p[i] += (tmp[0][i] * main.t_amb) * weights[0] + (tmp[1][i] * main.t_amb) * weights[1]
                if 3 == main.PUNKTY_CALKOWANIA:
                    loc_p[i] += tmp[2][i] * weights[2] * main.t_amb
        vec = list()
        vec2 = list()
        if 3 == main.PUNKTY_CALKOWANIA:
            vec3 = list()
        if grid.nodes[nodes[2]].boundary and grid.nodes[nodes[3]].boundary:
            if 2 == main.PUNKTY_CALKOWANIA:
                vec.append(0)
                vec.append(0)
                vec.append(uni[0])
                vec.append(uni[1])
                vec2.append(0)
                vec2.append(0)
                vec2.append(uni[1])
                vec2.append(uni[0])
            if 3 == main.PUNKTY_CALKOWANIA:
                vec.append(0)
                vec.append(0)
                vec.append(uni[2])
                vec.append(uni[0])
                vec2.append(0)
                vec2.append(0)
                vec2.append(uni[1])
                vec2.append(uni[1])
                vec3.append(0)
                vec3.append(0)
                vec3.append(uni[0])
                vec3.append(uni[2])
            tmp = list()
            for x in range(main.PUNKTY_CALKOWANIA):
                tmp.append(list())
            tmp[0] = vec
            tmp[1] = vec2
            if 3 == main.PUNKTY_CALKOWANIA:
                tmp[2] = vec3
            for i in range(4):
                loc_p[i] += (tmp[0][i] * main.t_amb) * weights[0] + (tmp[1][i] * main.t_amb) * weights[1]
                if 3 == main.PUNKTY_CALKOWANIA:
                    loc_p[i] += (tmp[2][i] * main.t_amb) * weights[2]

        vec = list()
        vec2 = list()
        if 3 == main.PUNKTY_CALKOWANIA:
            vec3 = list()
        if grid.nodes[nodes[0]].boundary and grid.nodes[nodes[3]].boundary:
            if 2 == main.PUNKTY_CALKOWANIA:
                vec.append(uni[0])
                vec.append(0)
                vec.append(0)
                vec.append(uni[1])
                vec2.append(uni[1])
                vec2.append(0)
                vec2.append(0)
                vec2.append(uni[0])
            if 3 == main.PUNKTY_CALKOWANIA:
                vec.append(uni[0])
                vec.append(0)
                vec.append(0)
                vec.append(uni[2])
                vec2.append(uni[1])
                vec2.append(0)
                vec2.append(0)
                vec2.append(uni[1])
                vec3.append(uni[2])
                vec3.append(0)
                vec3.append(0)
                vec3.append(uni[0])
            tmp = list()
            for x in range(main.PUNKTY_CALKOWANIA):
                tmp.append(list())
            tmp[0] = vec
            tmp[1] = vec2
            if 3 == main.PUNKTY_CALKOWANIA:
                tmp[2] = vec3
            for i in range(4):
                loc_p[i] += (tmp[0][i] * main.t_amb) * weights[0] + (tmp[1][i] * main.t_amb) * weights[1]
                if 3 == main.PUNKTY_CALKOWANIA:
                    loc_p[i] += (tmp[2][i] * main.t_amb) * weights[2]
        p =list()
        for i in range(4):
            p.append(0)
        for i in range(4):
            p[i] += loc_p[i]*det[i]*main.alfa

        print(f'local p of element {el.element_number}\n{p}')
        for i in range(len(loc_p)):
            grid.vector_p[nodes[i]] += p[i]

    print(f'global vector p = \n{grid.vector_p}')
