# https://developers.google.com/optimization/lp/glop

"""Minimal example to call the GLOP solver."""
from __future__ import print_function
from ortools.linear_solver import pywraplp
import random
from igraph import *

galaxias = ['Andromeda', 'OlhoNegro', 'Girassol ', 'CataVento', 'Magalhaes']


def main():
    # [START solver]
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    # [END solver]

    print("ENIGMA DAS GALÁXIAS\n")

    G = int(input("---> Digite o número de galáxias: "))

    for i in range(0, G):
        print(i, galaxias[i], sep=": ")

    print("\n")

    inicio = int(
        input("---> De que galáxia você quer partir, senhor astrônomo? "))
    print("Saindo de: ", galaxias[inicio])

    print("\n")

    d = [[0 for i in range(G)] for j in range(G)]
    for i in range(0, G):
        for j in range(i, G):
            if i == j:
                d[i][j] = 0
            else:
                d[i][j] = random.randint(0, 100)

    for i in range(1, G):
        for j in range(0, i):
            d[i][j] = d[j][i]

    print(d)

    print("\n")

    # [START variables]

    x = [[0 for i in range(G)] for j in range(G)]
    for i in range(0, G):
        for j in range(0, G):
            name_x = 'x' + str(i) + str(j)
            #print (name_x)
            x[i][j] = solver.BoolVar(name_x)

    print('Number of variables =', solver.NumVariables())

    # [END variables]

    print("\n")

    # [START constraints]

    for g in range(0, G):
        name_ct = 'ct' + str(g) + 'k'
        name_ct = solver.Constraint(1, 1)
        for i in range(0, G):
            for j in range(0, G):
                if g == i:
                    name_ct.SetCoefficient(x[i][j], 1)
                else:
                    name_ct.SetCoefficient(x[i][j], 0)

    # for j in range(0,G):
    #    name_ct = 'ct' +  'k' + str(j)
    #    name_ct = solver.Constraint(1,1)
    #    for i in range(0,G):
    #        name_x = 'x' + str(i) + str(j)
    #        name_ct.SetCoefficient(name_x, 1)

    for g in range(0, G):
        name_ct = 'ct' + str(g) + 'k'
        name_ct = solver.Constraint(1, 1)
        for j in range(0, G):
            for i in range(0, G):
                if g == j:
                    name_ct.SetCoefficient(x[i][j], 1)
                else:
                    name_ct.SetCoefficient(x[i][j], 0)

    print('Number of constraints =', solver.NumConstraints())
    # [END constraints]

    print("\n")

    # [START objective]

    objective = solver.Objective()

    for i in range(0, G):
        for j in range(0, G):
            objective.SetCoefficient(x[i][j], d[i][j])
    objective.SetMinimization()

    # [END objective]

    print("\n")

    # [START solve]
    solver.Solve()
    # [END solve]

    # [START print_solution]
    print('Solution:')
    print('Objective value =', objective.Value())

    # print(x)

    solucao = []
    for i in range(0, G):
        lista = []
        for j in range(0, G):
            print(int(x[i][j].solution_value()), end='   ')
            lista.append(int(x[i][j].solution_value()))
        solucao.append(lista)
        print("\n")

    modelagem_visual(d, solucao)
    # [END print_solution]


def modelagem_visual(matriz, solucao):
    g = Graph().Weighted_Adjacency(matriz, mode=ADJ_DIRECTED, attr="label", loops=True)
    g1 = Graph().Weighted_Adjacency(matriz, mode=ADJ_UPPER, attr="label", loops=True)

    g.vs()["galaxias"] = galaxias
    for vertice in g.vs():
        vertice["color"] = str('#') + ('%06X' % random.randint(0, 0xFFFFFF))

    for col in range(len(solucao)):
        for lin in range(len(solucao[col])):
            if(col != lin and solucao[col][lin] == 1):
                g.es[g.get_eid(col,lin)]["color"] = "darkred"
                g.es[g.get_eid(col,lin)]["label"] = g.es[g.get_eid(col,lin)]["label"]
            elif(col != lin and solucao[col][lin] == 0):
                g.es[g.get_eid(col,lin)]["color"] = (255, 255, 255, 0)
                g.es[g.get_eid(col,lin)]["label"] = ' '


    layout = g.layout("kk")
    visual_style = {}
    visual_style["layout"] = layout
    visual_style["edge_color"] = g.es["color"]
    visual_style["autocurve"] = False
    visual_style["vertex_label"] = g.vs()["galaxias"]
    visual_style["vertex_color"] = g.vs["color"]
    visual_style["vertex_size"] = 30
    visual_style["vertex_label_color"] = "darkblue"
    visual_style["vertex_label_dist"] = 2
    visual_style["edge_label_dist"] = -1
    visual_style["edge_curved"] = 0
    visual_style["margin"] = 40

    layout1 = g1.layout("kk")
    visual_style1 = {}
    visual_style1["layout"] = layout1
    visual_style1["vertex_color"] = (220,220,220)
    visual_style1["edge_color"] = (220,220,220)
    visual_style1["vertex_size"] = 30
    visual_style1["edge_curved"] = 0
    visual_style1["margin"] = 40
    visual_style1["vertex_label"] = galaxias
    visual_style["vertex_label_dist"] = 2
    
    
    p = Plot(background="white", bbox=(1250, 600))
    p.add(g, **visual_style, bbox=(650,1,1250, 600))
    p.add(g1, **visual_style1, bbox=(1,1,600,600))
    p.show()





if __name__ == '__main__':
    main()
