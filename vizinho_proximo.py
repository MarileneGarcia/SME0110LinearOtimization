from __future__ import print_function
from ortools.linear_solver import pywraplp
import random
from igraph import *
from itertools import combinations 
import math
import generate_matrix
import matplotlib.pyplot as plt
import numpy as np

galaxias = []
coordenadas = []
d_maxima = 100
d_infinita = 100000 * d_maxima

def main():
    global galaxias
    global coordenadas

    print("ENIGMA DAS GALÁXIAS\n")
    
    begin = int(input("---> Digite 0 para Djibouti, 1 para Qatar, 2 para Uruguay e 3 para Western Sahara: "))

    while True: 
        if begin == 0:
            d, galaxias, coordenadas = generate_matrix.generate_matrix('dj38.tsp')
            G = len(galaxias)
            break

        elif begin == 1:
            d, galaxias, coordenadas = generate_matrix.generate_matrix('qa194.tsp')
            G = len(galaxias)
            break

        elif begin == 2:
            d, galaxias, coordenadas = generate_matrix.generate_matrix('uy734.tsp')
            G = len(galaxias)
            break

        elif begin == 3:
            d, galaxias, coordenadas = generate_matrix.generate_matrix('wi29.tsp')
            G = len(galaxias)
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

    dist_total = d_infinita
    for inicio in range(G):
        dist = []
        visitados = []
        visitados.append(inicio)

        for j in range(len(galaxias)-1) :
            min_dist = d_infinita
            prox_viz = inicio

            for i in range(len(d[inicio])):
                dist_atual = d[inicio][i]

                if (dist_atual < min_dist and i not in visitados) :
                    min_dist = dist_atual
                    prox_viz = i
            
            inicio = prox_viz
            dist.append(min_dist)
            visitados.append(prox_viz)

        comeco = int(visitados[0])
        visitados.append(comeco)
        dist.append(d[inicio][comeco])
        if sum(dist) < dist_total:
            dist_total = sum(dist)
            pos_inicial = comeco
            caminho_final = visitados
    
    #modelagem_visual(d, solucao)

    print("\n")


    # Reorder the cities matrix by route order in a new matrix for plotting.
    route = np.array(caminho_final)
    cities = np.array(coordenadas)

    new_cities_order = np.concatenate((np.array([coordenadas[route[i]] for i in range(len(route))]),np.array([coordenadas[route[0]]])))
    
    # Plot the cities.
    
    plt.scatter(cities[:,0],cities[:,1])
    plt.scatter(cities[pos_inicial][0], cities[pos_inicial][1], color='red')
    for i in range(len(coordenadas)):
        plt.text(coordenadas[i][0],coordenadas[i][1], str(i), fontsize=9)

    # Plot the path.
    plt.plot(new_cities_order[:,0],new_cities_order[:,1])
    plt.show()
    # Print the route as row numbers and the total distance travelled by the path.
    print("Galáxias Visitadas: " + str(route) + "\n\nDistancias Total: " + str(dist_total))

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