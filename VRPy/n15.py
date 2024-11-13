import networkx as nx
from vrpy import VehicleRoutingProblem
import math
import time

# Lista de nós e suas coordenadas (x, y), com Source e Sink na mesma coordenada
nodes = [
    ("Source", 30, 40, 0),  # Depósito com demanda 0
    ("Cliente1", 37, 52, 19),
    ("Cliente2", 49, 49, 30),
    ("Cliente3", 52, 64, 16),
    ("Cliente4", 31, 62, 23),
    ("Cliente5", 52, 33, 11),
    ("Cliente6", 42, 41, 31),
    ("Cliente7", 52, 41, 15),
    ("Cliente8", 57, 58, 28),
    ("Cliente9", 62, 42, 8),
    ("Cliente10", 42, 57, 8),
    ("Cliente11", 27, 68, 7),
    ("Cliente12", 43, 67, 14),
    ("Cliente13", 58, 48, 6),
    ("Cliente14", 58, 27, 19),
    ("Cliente15", 37, 69, 11),
    ("Sink", 30, 40, 0)  # Depósito de retorno com demanda 0
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
            cost_list = [distance] * 8

            # Adiciona aresta com lista de custos
            if nodes[i][0] == "Source":
                G.add_edge("Source", nodes[j][0], cost=cost_list)
            elif nodes[j][0] == "Sink":
                G.add_edge(nodes[i][0], "Sink", cost=cost_list)
            elif nodes[i][0] != "Sink" and nodes[j][0] != "Source":
                G.add_edge(nodes[i][0], nodes[j][0], cost=cost_list)

# Configurando o problema VRP com frota mista
prob = VehicleRoutingProblem(G, mixed_fleet=True, load_capacity=[30, 30, 30, 30, 40, 40, 40, 40], use_all_vehicles=True)
# Solução do problema
start = time.time()
prob.solve()
end = time.time()
#prob.solve()


# Exibindo a solução
print(prob.best_value)
print("-----------------------------------------------")
print(prob.best_routes_type)
print("-----------------------------------------------")
print(prob.best_routes)
print(end-start)