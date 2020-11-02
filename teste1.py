from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp



def definir_modelo():
    d_ij = {}
    d_ij['distancia entre as galaxias'] = [
        [0.0, 725.01, 154.25, 166.65, 388.61],
        [154.36, 0.0, 262.45, 357.92, 652.41],
        [366.29, 125.74, 0.0, 221.24, 245.46],
        [634.55, 189.78, 694.64, 0.0, 699.39],
        [364.45, 100.23, 154.44, 137.46, 0.0],
    ]
    d_ij['num_telescopios'] = 1

    print("Sabendo que pode-se passar pelas galaxias:\n 0-Andromeda \n 1-Olho Negro \n 2-Girassol \n 3-Cata Vento \n 4-Grande Nuvem de Magalhaes")
    inicio = input("Digite um numero de 0 a 4 e escolha por qual deseja iniciar o percurso: ")
    d_ij['galaxia_inicial'] = int(inicio)
    return d_ij


def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print('\nDistancia observada: {} Mly'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = '\nGalaxias Percorridas:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Route distance: {}miles\n'.format(route_distance)


def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    d_ij = definir_modelo()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(d_ij['distancia entre as galaxias']), d_ij['num_telescopios'], d_ij['galaxia_inicial'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return d_ij['distancia entre as galaxias'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(manager, routing, solution)


if __name__ == '__main__':
    main()
