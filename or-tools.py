from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import generate_matrix
import numpy as np
import matplotlib.pyplot as plt
import time

def create_data_model(d):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = d
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

def plot_resultado(manager, routing, solution, coordenadas, galaxias, tempo):
    rota = []

    print('Galaxias: ' + str(len(galaxias)))
    index = routing.Start(0)
    plan_output = 'Rota: '
    route_distance = 0

    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        rota.append(int(format(manager.IndexToNode(index))))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}'.format(manager.IndexToNode(index))

    print('Custo: {}'.format(solution.ObjectiveValue()))
    print(plan_output)
    print('Tempo: ' + str(tempo))

    d_plot = np.concatenate((np.array([coordenadas[rota[i]] for i in range(len(rota))]),np.array([coordenadas[rota[0]]])))
    plt.scatter(coordenadas[:,0],coordenadas[:,1])
    plt.plot(d_plot[:,0],d_plot[:,1])
    for i, txt in enumerate(rota):
        plt.annotate(str(rota[i]), coordenadas[rota[i]])
    plt.show()


def main():
    start_time = time.time()

    print("ENIGMA DAS GALÁXIAS - OR-TOOLS PARAMS SOLVERS\n")
    
    begin = int(input("---> Digite 0 para Western Sahara, 1 para Djibouti, 2 para Qatar e 3 para Uruguay: "))

    while True: 
        if begin == 0:
            d, galaxias, coordenadas = generate_matrix.generate_matrix('wi29.tsp')
            G = len(galaxias)
            break

        elif begin == 1:
            d, galaxias, coordenadas = generate_matrix.generate_matrix('dj38.tsp')
            G = len(galaxias)
            break

        elif begin == 2:
            d, galaxias, coordenadas = generate_matrix.generate_matrix('qa194.tsp')
            G = len(galaxias)
            break

        elif begin == 3:
            d, galaxias, coordenadas = generate_matrix.generate_matrix('uy734.tsp')
            G = len(galaxias)
            break

        else:
            begin = int(input("---> Entrada inválida, digite o ou 1! "))

    coordenadas = np.array(coordenadas)

    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(d)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()

    param = int(input("---> Escolha a estratégia\nDigite 0 para PATH_CHEAPEST_ARC, 1 para SAVINGS, 2 para CHRISTOFIDES: "))

    while True: 
        if param == 0:
            search_parameters.first_solution_strategy = (
                routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
            break

        elif param == 1:
            search_parameters.first_solution_strategy = (
                routing_enums_pb2.FirstSolutionStrategy.SAVINGS)
            break

        elif param == 2:
            search_parameters.first_solution_strategy = (
                routing_enums_pb2.FirstSolutionStrategy.CHRISTOFIDES)
            break

        else:
            param = int(input("---> Entrada inválida, digite o ou 1! "))

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    final_time = time.time() - start_time

    plot_resultado(manager, routing, solution, coordenadas, galaxias, final_time)

if __name__ == '__main__':
    main()