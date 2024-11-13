import networkx as nx
from vrpy import VehicleRoutingProblem
import math

# Lista de nós e suas coordenadas (x, y), com Source e Sink na mesma coordenada
nodes = [
    ("Source", 30, 40, 0),  # Depósito com demanda 0
    ("Cliente1", 37, 52, 7),
    ("Cliente2", 49, 49, 30),
    ("Cliente3", 52, 64, 16),
    ("Cliente4", 20, 26, 9),
    ("Cliente5", 40, 30, 21),
    ("Cliente6", 21, 47, 15),
    ("Cliente7", 17, 63, 19),
    ("Cliente8", 31, 62, 23),
    ("Cliente9", 52, 33, 11),
    ("Cliente10", 51, 21, 5),
    ("Cliente11", 42, 41, 19),
    ("Cliente12", 31, 32, 29),
    ("Cliente13", 5, 25, 23),
    ("Cliente14", 12, 42, 21),
    ("Cliente15", 36, 16, 10),
    ("Cliente16", 52, 41, 15),
    ("Cliente17", 27, 23, 3),
    ("Cliente18", 17, 33, 41),
    ("Cliente19", 13, 13, 9),
    ("Cliente20", 57, 58, 28),
    ("Cliente21", 62, 42, 8),
    ("Cliente22", 42, 57, 8),
    ("Cliente23", 16, 57, 16),
    ("Cliente24", 8, 52, 10),
    ("Cliente25", 7, 38, 28),
    ("Cliente26", 27, 68, 7),
    ("Cliente27", 30, 48, 15),
    ("Cliente28", 43, 67, 14),
    ("Cliente29", 58, 48, 6),
    ("Cliente30", 58, 27, 19),
    ("Cliente31", 37, 69, 11),
    ("Cliente32", 38, 46, 12),
    ("Cliente33", 46, 10, 23),
    ("Cliente34", 61, 33, 26),
    ("Cliente35", 62, 63, 17),
    ("Cliente36", 63, 69, 6),
    ("Cliente37", 32, 22, 9),
    ("Cliente38", 45, 35, 15),
    ("Cliente39", 59, 15, 14),
    ("Cliente40", 5, 6, 7),
    ("Cliente41", 10, 17, 27),
    ("Cliente42", 21, 10, 13),
    ("Cliente43", 5, 64, 11),
    ("Cliente44", 30, 15, 16),
    ("Cliente45", 39, 10, 10),
    ("Cliente46", 32, 39, 5),
    ("Cliente47", 25, 32, 25),
    ("Cliente48", 25, 55, 17),
    ("Cliente49", 48, 28, 18),
    ("Cliente50", 56, 37, 10),
    ("Sink", 30, 40, 0)  # Depósito de retorno com demanda 0
]

# Função para calcular a distância euclidiana entre dois pontos
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Criando o grafo e adicionando nós com suas demandas
G = nx.DiGraph()
for node, x, y, demand in nodes:
    G.add_node(node, demand=demand)

# Número de veículos e lista de capacidades
vehicle_capacities = [150, 200, 250, 250]
num_vehicles = len(vehicle_capacities)

# Adicionando arestas e custos como listas para mixed_fleet
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i != j:
            # Calcular a distância como custo base
            distance = euclidean_distance((nodes[i][1], nodes[i][2]), (nodes[j][1], nodes[j][2]))
            # Criar uma lista de custos onde cada veículo tem o mesmo custo (distance)
            cost_list = [distance] * num_vehicles

            # Adiciona aresta com lista de custos
            if nodes[i][0] == "Source":
                G.add_edge("Source", nodes[j][0], cost=cost_list)
            elif nodes[j][0] == "Sink":
                G.add_edge(nodes[i][0], "Sink", cost=cost_list)
            elif nodes[i][0] != "Sink" and nodes[j][0] != "Source":
                G.add_edge(nodes[i][0], nodes[j][0], cost=cost_list)

# Configurando o problema VRP com frota mista
prob = VehicleRoutingProblem(G, mixed_fleet=True, load_capacity=[150, 200, 250, 250], use_all_vehicles=True)
# Solução do problema
prob.solve(greedy=True, time_limit=36000)
#prob.solve()


# Exibindo a solução
print(prob.best_value)
print("-----------------------------------------------")
print(prob.best_routes_type)
print("-----------------------------------------------")
print(prob.best_routes)