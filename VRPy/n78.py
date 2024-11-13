import networkx as nx
from vrpy import VehicleRoutingProblem
import math

# Lista de nós e suas coordenadas (x, y), com Source e Sink na mesma coordenada
nodes = [
    ("Source", 46, 12, 0),  # Depósito com demanda 0
    ("Cliente2", 51, 4, 14),
    ("Cliente3", 52, 30, 17),
    ("Cliente4", 80, 70, 17),
    ("Cliente5", 18, 90, 16),
    ("Cliente6", 59, 39, 19),
    ("Cliente7", 23, 59, 17),
    ("Cliente8", 77, 48, 5),
    ("Cliente9", 82, 30, 12),
    ("Cliente10", 18, 82, 4),
    ("Cliente11", 11, 41, 2),
    ("Cliente12", 7, 9, 2),
    ("Cliente13", 88, 83, 26),
    ("Cliente14", 23, 88, 2),
    ("Cliente15", 0, 76, 7),
    ("Cliente16", 85, 34, 18),
    ("Cliente17", 17, 46, 6),
    ("Cliente18", 52, 10, 6),
    ("Cliente19", 13, 45, 18),
    ("Cliente20", 19, 85, 2),
    ("Cliente21", 86, 77, 14),
    ("Cliente22", 54, 6, 5),
    ("Cliente23", 83, 32, 9),
    ("Cliente24", 15, 10, 4),
    ("Cliente25", 53, 5, 3),
    ("Cliente26", 14, 42, 15),
    ("Cliente27", 13, 10, 4),
    ("Cliente28", 57, 32, 23),
    ("Cliente29", 20, 85, 7),
    ("Cliente30", 65, 46, 21),
    ("Cliente31", 61, 42, 4),
    ("Cliente32", 87, 52, 1),
    ("Cliente33", 79, 51, 6),
    ("Cliente34", 25, 91, 16),
    ("Cliente35", 89, 34, 4),
    ("Cliente36", 26, 100, 20),
    ("Cliente37", 0, 88, 5),
    ("Cliente38", 63, 43, 14),
    ("Cliente39", 55, 10, 14),
    ("Cliente40", 23, 86, 26),
    ("Cliente41", 8, 18, 5),
    ("Cliente42", 0, 74, 2),
    ("Cliente43", 20, 44, 14),
    ("Cliente44", 56, 7, 11),
    ("Cliente45", 14, 10, 21),
    ("Cliente46", 88, 40, 20),
    ("Cliente47", 96, 38, 18),
    ("Cliente48", 59, 31, 2),
    ("Cliente49", 22, 87, 19),
    ("Cliente50", 59, 36, 12),
    ("Cliente51", 24, 83, 22),
    ("Cliente52", 83, 37, 14),
    ("Cliente53", 53, 5, 23),
    ("Cliente54", 0, 37, 25),
    ("Cliente55", 84, 78, 8),
    ("Cliente56", 27, 93, 3),
    ("Cliente57", 61, 12, 9),
    ("Cliente58", 69, 43, 21),
    ("Cliente59", 54, 9, 3),
    ("Cliente60", 20, 98, 22),
    ("Cliente61", 18, 50, 6),
    ("Cliente62", 25, 84, 2),
    ("Cliente63", 31, 69, 22),
    ("Cliente64", 58, 36, 20),
    ("Cliente65", 0, 11, 5),
    ("Cliente66", 61, 36, 13),
    ("Cliente67", 18, 49, 6),
    ("Cliente68", 57, 8, 14),
    ("Cliente69", 0, 49, 16),
    ("Cliente70", 56, 8, 12),
    ("Cliente71", 62, 45, 23),
    ("Cliente72", 83, 32, 5),
    ("Cliente73", 53, 10, 12),
    ("Cliente74", 82, 53, 15),
    ("Cliente75", 21, 85, 21),
    ("Cliente76", 64, 41, 4),
    ("Cliente77", 80, 50, 23),
    ("Cliente78", 16, 10, 19),
    ("Sink", 46, 12, 0)  # Depósito de retorno com demanda 0
]

# Função para calcular a distância euclidiana entre dois pontos
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Criando o grafo e adicionando nós com suas demandas
G = nx.DiGraph()
for node, x, y, demand in nodes:
    G.add_node(node, demand=demand)

# Número de veículos e lista de capacidades
vehicle_capacities = [60, 60, 60, 80, 80, 120, 120, 120, 140, 140]
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
prob = VehicleRoutingProblem(G, mixed_fleet=True, load_capacity=[60, 60, 60, 80, 80, 120, 120, 120, 140, 140], use_all_vehicles=True)
# Solução do problema
prob.solve(greedy=True, time_limit=36000)
#prob.solve()


# Exibindo a solução
print(prob.best_value)
print("-----------------------------------------------")
print(prob.best_routes_type)
print("-----------------------------------------------")
print(prob.best_routes)