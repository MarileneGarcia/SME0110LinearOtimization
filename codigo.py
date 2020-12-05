from __future__ import print_function
from ortools.linear_solver import pywraplp
import random
from igraph import *
from itertools import combinations 
import math

galaxias = []
d_maxima = 100
d_infinita = 100000 * d_maxima

def main():
    ########################### [START solver]
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    ###########################  [END solver]

    print("ENIGMA DAS GALÁXIAS\n")
    
    begin = int(input("---> Digite 0 para o caso exemplo e 1 para personalizar: "))

    infinity = solver.infinity()
    while True: 
        if begin == 0:
            G = 5
            d = [[d_infinita, 100, 1, 1, 1],[100, d_infinita, 1, 100, 1],[1, 1, d_infinita, 1, 100],[1, 100, 1, d_infinita, 1],[1, 1, 100, 1, d_infinita]]
            break

        elif begin == 1:
            G = int(input("---> Digite o número de galáxias: "))
            d = gerar_aleatorio(G, galaxias)
            break

        else:
            begin = int(input("---> Entrada inválida, digite o ou 1! "))

    print("\n")

    for i in range(0, G):
        print(i, galaxias[i], sep=": ")

    print("\n")

    '''for i in range(0, G):
        for j in range(0, G):
            print(int(d[i][j]), end='   ')
        print("\n")
    print("\n")'''

    inicio = int(
        input("---> De que galáxia você quer partir, senhor astrônomo? "))
    
    print("\n")

    print("Saindo de: ", galaxias[inicio])

    print("\n")

    ###########################  [START variables]
    x = [[0 for i in range(G)] for j in range(G)]
    for i in range(0, G):
        for j in range(0, G):
            name_x = 'x' + str(i) + str(j)
            #print (name_x)
            x[i][j] = solver.BoolVar(name_x)

    print('Número de variáveis =', solver.NumVariables())
    ###########################  [END variables]

    print("\n")

    ###########################  [START constraints]
    for g in range(0, G):
        name_ct = 'ct' + str(g) + 'k'
        name_ct = solver.Constraint(1, 1)
        for i in range(0, G):
            for j in range(0, G):
                if g == i:
                    name_ct.SetCoefficient(x[i][j], 1)
                else:
                    name_ct.SetCoefficient(x[i][j], 0)

    for g in range(0, G):
        name_ct = 'ct' + 'k' + str(g)
        name_ct = solver.Constraint(1, 1)
        for j in range(0, G):
            for i in range(0, G):
                if g == j:
                    name_ct.SetCoefficient(x[i][j], 1)
                else:
                    name_ct.SetCoefficient(x[i][j], 0)

    c_max = G - 1
    for c in range(2, c_max):
        S = combinations(galaxias,c)
        g_in = []
        g_out = []

        i_tpl = 0
        for tpl in S:
            name_ct = 'ct_tpl' + str(i_tpl)
            name_ct = solver.Constraint(1, solver.infinity())
            print(name_ct)
            #print(tpl)

            for i in range(0,c):
                g_in.append(int(tpl[i]))
            
            print(g_in)

            for i in range(0, G):
                for j in range(0, G):
                    if (i in g_in) and (j not in g_in):
                        #print('Dentro: ' + str(i) + ' ' + str(j))
                        name_ct.SetCoefficient(x[i][j], 1)
                    else:
                        name_ct.SetCoefficient(x[i][j], 0)

            g_in.clear()
            i_tpl +=1


    print('Número de restrições =', solver.NumConstraints())
    ###########################  [END constraints]


    ###########################  [START objective]
    objective = solver.Objective()

    for i in range(0, G):
        for j in range(0, G):
            objective.SetCoefficient(x[i][j], d[i][j])
    objective.SetMinimization()
    ###########################  [END objective]

    print("\n")

    ###########################  [START solve]
    solver.Solve()
    ###########################  [END solve]


    ###########################  [START print_solution]
    print('Solução - Valor objetivo =', objective.Value())

    # print(x)

    solucao = []
    for i in range(0, G):
        lista = []
        for j in range(0, G):
            #print(int(x[i][j].solution_value()), end='   ')
            lista.append(int(x[i][j].solution_value()))
        solucao.append(lista)
        #print("\n")

    modelagem_visual(d, solucao)

    print("\n")
    ###########################  [END print_solution]

def gerar_aleatorio(G, galaxias):
    for i in range(0, G):
        nome = f"{i}"
        #print (nome)
        galaxias.append(nome)

    d = [[0 for i in range(G)] for j in range(G)]
    for i in range(0, G):
        for j in range(i, G):
            if i == j:
                d[i][j] = d_infinita
            else:
                d[i][j] = random.randint(1, d_maxima)

    for i in range(1, G):
        for j in range(0, i):
            d[i][j] = d[j][i]

    return d

def modelagem_visual(matriz, solucao):
    g = Graph().Weighted_Adjacency(matriz, mode=ADJ_DIRECTED, attr="label", loops=False)
    g1 = Graph().Weighted_Adjacency(matriz, mode=ADJ_UPPER, attr="label", loops=False)

    g.vs()["galaxias"] = galaxias
    for vertice in g.vs():
        vertice["color"] = str('#') + ('%06X' % random.randint(0, 0xFFFFFF))

    for col in range(len(solucao)):
        for lin in range(len(solucao[col])):
            if(col != lin and solucao[col][lin] == 1):
                g.es[g.get_eid(col,lin)]["color"] = (139,0,0)
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
    visual_style["vertex_label_color"] = "blue"
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
    #visual_style1["edge_curved"] = 0
    visual_style1["margin"] = 40
    visual_style1["vertex_label"] = galaxias
    visual_style["vertex_label_dist"] = 2
    
    
    p = Plot(background=(255,255,255), bbox=(1250, 600), target=None)
    p.add(g, **visual_style, bbox=(650,1,1250, 600), target=None)
    p.add(g1, **visual_style1, bbox=(1,1,600,600), target=None)
    p.show()


if __name__ == '__main__':
    main()