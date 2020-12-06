import time
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

    start_time = time.time()
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
    print("--- %s seconds ---" % (time.time() - start_time))

    route = np.array(caminho_final)
    cities = np.array(coordenadas)

    new_cities_order = np.concatenate((np.array([coordenadas[route[i]] for i in range(len(route))]),np.array([coordenadas[route[0]]])))
    
    # Plota as galáxias.
    plt.scatter(cities[:,0],cities[:,1])
    # Coloca a galáxia inicial como vermelha no gráfico
    plt.scatter(cities[pos_inicial][0], cities[pos_inicial][1], color='red')
    for i in range(len(coordenadas)):
        plt.text(coordenadas[i][0],coordenadas[i][1], str(i), fontsize=9)

    # Plota o caminho.
    plt.plot(new_cities_order[:,0],new_cities_order[:,1])
    plt.show()
    # Printa o menor caminho encontrado e a distância total para ele.
    print("Galáxias Visitadas: " + str(route) + "\n\nDistancias Total: " + str(dist_total))

if __name__ == '__main__':
    main()