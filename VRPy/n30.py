import networkx as nx
from vrpy import VehicleRoutingProblem
import math
import time

# Lista de nós e suas coordenadas (x, y), com Source e Sink na mesma coordenada
nodes = [
    ("Source", 82, 76, 0),  # Depósito com demanda 0
    ("Cliente1", 96, 44, 19),
    ("Cliente2", 50, 5, 21),
    ("Cliente3", 49, 8, 6),
    ("Cliente4", 13, 7, 19),
    ("Cliente5", 29, 89, 7),
    ("Cliente6", 58, 30, 12),
    ("Cliente7", 84, 39, 16),
    ("Cliente8", 14, 24, 6),
    ("Cliente9", 2, 39, 16),
    ("Cliente10", 3, 82, 8),
    ("Cliente11", 5, 10, 14),
    ("Cliente12", 98, 52, 21),
    ("Cliente13", 84, 25, 16),
    ("Cliente14", 61, 59, 3),
    ("Cliente15", 1, 65, 22),
    ("Cliente16", 88, 51, 18),
    ("Cliente17", 91, 2, 19),
    ("Cliente18", 19, 32, 1),
    ("Cliente19", 93, 3, 24),
    ("Cliente20", 50, 93, 8),
    ("Cliente21", 98, 14, 12),
    ("Cliente22", 5, 42, 4),
    ("Cliente23", 42, 9, 8),
    ("Cliente24", 61, 62, 24),
    ("Cliente25", 9, 97, 24),
    ("Cliente26", 80, 55, 2),
    ("Cliente27", 57, 69, 20),
    ("Cliente28", 23, 15, 15),
    ("Cliente29", 20, 70, 2),
    ("Cliente30", 85, 60, 14),
    ("Cliente31", 98, 5, 9),
    ("Sink", 82, 76, 0)  # Depósito de retorno com demanda 0
]

# Função para calcular a distância euclidiana entre dois pontos
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Criando o grafo e adicionando nós com suas demandas
G = nx.DiGraph()
for node, x, y, demand in nodes:
    G.add_node(node, demand=demand)

# Adicionando arestas e custos como listas para mixed_fleet
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i != j:
            # Calcular a distância como custo base
            distance = euclidean_distance((nodes[i][1], nodes[i][2]), (nodes[j][1], nodes[j][2]))
            # Criar uma lista de custos onde cada veículo tem o mesmo custo (distance)
            cost_list = [distance] * 5

            # Adiciona aresta com lista de custos
            if nodes[i][0] == "Source":
                G.add_edge("Source", nodes[j][0], cost=cost_list)
            elif nodes[j][0] == "Sink":
                G.add_edge(nodes[i][0], "Sink", cost=cost_list)
            elif nodes[i][0] != "Sink" and nodes[j][0] != "Source":
                G.add_edge(nodes[i][0], nodes[j][0], cost=cost_list)

# Configurando o problema VRP com frota mista
prob = VehicleRoutingProblem(G, mixed_fleet=True, load_capacity=[90, 90, 100, 100, 120], use_all_vehicles=True)
# Solução do problema
start = time.time()
prob.solve(greedy=True, time_limit=36000)
end = time.time()
#prob.solve()


# Exibindo a solução
print(prob.best_value)
print("-----------------------------------------------")
print(prob.best_routes_type)
print("-----------------------------------------------")
print(prob.best_routes)
print(end-start)