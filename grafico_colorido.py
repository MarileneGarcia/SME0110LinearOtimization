from __future__ import print_function
from ortools.linear_solver import pywraplp
from igraph import *
from random import randint

numero_vertices = 5

def main():
  solver = pywraplp.Solver('SolveStigler', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

  ''' COLOCAR NO RELATORIO: unidades em Mly, maga ano luz '''

  # Criando o variavel d_ij com as galaxias e a distancia entre elas # 
  d_ij = [['Andromeda', 'OlhoNegro', 'Girassol ', 'CataVento', 'Magalhaes'], 
                        ['Andromeda', 0.0, 725.01, 154.25, 166.65, 388.61],
                        ['OlhoNegro', 154.36, 0.0, 262.45, 357.92, 652.41],
                        ['Girassol ', 366.29, 125.74, 0.0, 221.24, 245.46],
                        ['CataVento', 634.55, 189.78, 694.64, 0.0, 699.39],
                        ['Magalhaes', 364.45, 100.23, 154.44, 137.46, 0.0]]
  
  # Imprimir as distancia entre as galaxias, lembrando que elas estao em Mly #
  print('           ', end = ' ')
  for i in range(0, 5):
    print(d_ij[0][i], end = ' | ')
  print()
  for n in range(1, 6):
    for m in range(0, 6):
      print(d_ij[n][m], end = '      ')
    print( '\n')

  # criando a variavel binaria x_ij
  x = solver.NumVar(0, 1, 'x')

  matriz = []
  for n in range(1, 6):
    lista = []
    for m in range(1, 6):
      lista.append(d_ij[n][m])
    matriz.append(lista)

  g = Graph().Weighted_Adjacency(matriz, mode=ADJ_UPPER, attr="label", loops=True)
  
  for vertice in g.vs():
    vertice["color"] = str('#') +('%06X' % randint(0, 0xFFFFFF))

  layout = g.layout("kk")
  visual_style = {}
  visual_style["layout"] = layout
  visual_style["edge_color"] = "lightgray"
  
  visual_style["vertex_label"] = d_ij[0]
  visual_style["vertex_color"] = g.vs["color"]
  visual_style["vertex_size"] = 30
  visual_style["vertex_label_color"] = "darkblue"
  visual_style["vertex_label_dist"] = 2

  visual_style["bbox"] = (1024, 916)
  visual_style["margin"] = 40
  plot(g, **visual_style)
  
  '''for z in range(0, numero_vertices):
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
   
  
  #g.vs[3]["color"] = (0,0,0)
  plot(g, layout = layout)'''
  

  '''
  
  # [START variables]
  # Create the variables d_ij and x_ij
  d_ij = [[]]
  x_ij = [[]]
  x = solver.NumVar(0, 1, 'x')
  y = solver.NumVar(0, 2, 'y')

  print('Number of variables =', solver.NumVariables())
  # [END variables]

  # [START constraints]
  # Create a linear constraint, 0 <= x + y <= 2.
  ct = solver.Constraint(0, 2, 'ct')
  ct.SetCoefficient(x, 1)
  ct.SetCoefficient(y, 1)

  print('Number of constraints =', solver.NumConstraints())
  # [END constraints]

  # [START objective]
  # Create the objective function, 3 * x + y.
  objective = solver.Objective()
  objective.SetCoefficient(x, 3)
  objective.SetCoefficient(y, 1)
  objective.SetMaximization()
  # [END objective]

  # [START solve]
  solver.Solve()
  # [END solve]

  # [START print_solution]
  print('Solution:')
  print('Objective value =', objective.Value())
  print('x =', x.solution_value())
  print('y =', y.solution_value())
  # [END print_solution]
  # 
  # https://stackoverflow.com/questions/23184306/draw-network-and-grouped-vertices-of-the-same-community-or-partition'''

main()