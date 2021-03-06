import agregate
import hbc
import sim

import grid

import lokalny_uklad
import main
import matrixC
import matrixH
import vectorp

PUNKTY_CALKOWANIA = 3
K = 25
alfa = 300
t_amb = 1200
C = 700
ro = 7800
starting_temp = 100
dt = 1
end_time = 100


if __name__ == '__main__':
    greed = grid.Grid(0.1, 0.1, 31, 31)
    # kt = 30
    if greed.nN != 16 or main.PUNKTY_CALKOWANIA != 2:
        print("symulacja dla reakcji egzotermicznej z chłodzeniem rdzenia")


    print(greed)
    # calkowanie.calka(PUNKTY_CALKOWANIA)
    # print(lokalny_uklad.ksztaltKsi(greed.elements.__getitem__(0)))
    # print()
    # lokalny_uklad.printList(lokalny_uklad.ksztaltKsi(greed.elements.__getitem__(0)))
    # print()
    # lokalny_uklad.printList(lokalny_uklad.ksztaltEta(greed.elements.__getitem__(0)))
    lokalny_uklad.liczDet(greed)
    # print('.')
    matrixH.matrixpc(greed)
    # print('boundary ndoes')
    # for node in greed.nodes:
    #     if node.boundary == True:
    #         print(node)

    # vectorp.uni_node()

    vectorp.count_vetor_p(greed)
    hbc.c_hbc(greed)
    agregate.agregat(greed)
    matrixC.countc(greed)
    sim.run_sim(main.starting_temp, main.dt, main.end_time, greed)