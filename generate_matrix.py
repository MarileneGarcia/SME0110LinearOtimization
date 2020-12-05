import math
from pandas import DataFrame


d_maxima = 100
d_infinita = 100000 * d_maxima

def generate_matrix(file_name):
    arq = open('files/%s' %file_name, 'r')

    while True:
        linha = arq.readline()
        if linha[0] == '1':
            break
    
    nomes = []
    coordenadas = []
    while True:
        if linha == '' or linha == 'EOF\n' or linha == 'EOF' or linha == 'EOF ':
            break

        linha = linha.split(' ')
        nomes.append(str(int(linha[0]) - 1))
        lista_aux = [float(linha[1]),float(linha[2])]
        coordenadas.append(lista_aux)
        linha = arq.readline()

    size = len(coordenadas)
    matriz_distancias = []

    for i in range(0,size):
        lista = []
        for j in range(0, size):
            if(i == j):
                euclidiana = d_infinita
            else:
                x1 = coordenadas[i][0]
                y1 = coordenadas[i][1]
                x2 = coordenadas[j][0]
                y2 = coordenadas[j][1]
                euclidiana = math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))

            lista.append(euclidiana)

        matriz_distancias.append(lista)

    return matriz_distancias, nomes, coordenadas



