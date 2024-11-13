import networkx as nx
from vrpy import VehicleRoutingProblem
import math

# Lista de nós e suas coordenadas (x, y), com Source e Sink na mesma coordenada
nodes = [
    ("Source", 365, 689, 0),  # Depósito com demanda 0
    ("Cliente2", 146, 180, 38),
    ("Cliente3", 792, 5, 51),
    ("Cliente4", 658, 510, 73),
    ("Cliente5", 461, 270, 70),
    ("Cliente6", 299, 531, 58),
    ("Cliente7", 812, 228, 54),
    ("Cliente8", 643, 90, 1),
    ("Cliente9", 615, 630, 98),
    ("Cliente10", 258, 42, 62),
    ("Cliente11", 616, 299, 98),
    ("Cliente12", 475, 957, 25),
    ("Cliente13", 425, 473, 86),
    ("Cliente14", 406, 64, 46),
    ("Cliente15", 656, 369, 27),
    ("Cliente16", 202, 467, 17),
    ("Cliente17", 318, 21, 97),
    ("Cliente18", 579, 587, 74),
    ("Cliente19", 458, 354, 81),
    ("Cliente20", 575, 871, 62),
    ("Cliente21", 47, 512, 59),
    ("Cliente22", 568, 742, 23),
    ("Cliente23", 128, 436, 62),
    ("Cliente24", 546, 806, 66),
    ("Cliente25", 197, 696, 35),
    ("Cliente26", 615, 300, 53),
    ("Cliente27", 852, 563, 18),
    ("Cliente28", 772, 803, 87),
    ("Cliente29", 678, 342, 32),
    ("Cliente30", 916, 176, 4),
    ("Cliente31", 390, 949, 61),
    ("Cliente32", 113, 782, 95),
    ("Cliente33", 226, 736, 23),
    ("Cliente34", 119, 923, 15),
    ("Cliente35", 584, 572, 5),
    ("Cliente36", 134, 554, 53),
    ("Cliente37", 912, 173, 97),
    ("Cliente38", 827, 233, 70),
    ("Cliente39", 851, 677, 32),
    ("Cliente40", 598, 322, 27),
    ("Cliente41", 627, 472, 42),
    ("Cliente42", 94, 442, 67),
    ("Cliente43", 688, 274, 76),
    ("Cliente44", 977, 176, 15),
    ("Cliente45", 597, 461, 39),
    ("Cliente46", 931, 23, 14),
    ("Cliente47", 170, 640, 43),
    ("Cliente48", 941, 601, 11),
    ("Cliente49", 873, 487, 93),
    ("Cliente50", 797, 95, 53),
    ("Cliente51", 451, 816, 44),
    ("Cliente52", 866, 970, 80),
    ("Cliente53", 833, 912, 87),
    ("Cliente54", 106, 913, 97),
    ("Cliente55", 260, 107, 67),
    ("Cliente56", 332, 45, 72),
    ("Cliente57", 685, 613, 50),
    ("Cliente58", 728, 372, 8),
    ("Cliente59", 487, 497, 58),
    ("Cliente60", 702, 440, 55),
    ("Cliente61", 717, 412, 67),
    ("Cliente62", 635, 794, 89),
    ("Cliente63", 927, 972, 38),
    ("Cliente64", 635, 356, 65),
    ("Cliente65", 634, 540, 3),
    ("Cliente66", 658, 261, 5),
    ("Cliente67", 303, 168, 46),
    ("Cliente68", 707, 410, 100),
    ("Cliente69", 254, 135, 52),
    ("Cliente70", 346, 29, 28),
    ("Cliente71", 75, 79, 96),
    ("Cliente72", 893, 987, 18),
    ("Cliente73", 729, 372, 16),
    ("Cliente74", 29, 910, 7),
    ("Cliente75", 356, 39, 73),
    ("Cliente76", 274, 943, 76),
    ("Cliente77", 322, 96, 6),
    ("Cliente78", 664, 396, 64),
    ("Cliente79", 704, 236, 39),
    ("Cliente80", 415, 837, 86),
    ("Cliente81", 576, 587, 70),
    ("Cliente82", 750, 977, 14),
    ("Cliente83", 726, 363, 83),
    ("Cliente84", 861, 948, 96),
    ("Cliente85", 302, 129, 43),
    ("Cliente86", 415, 989, 12),
    ("Cliente87", 199, 135, 73),
    ("Cliente88", 801, 405, 2),
    ("Cliente89", 679, 426, 21),
    ("Cliente90", 994, 804, 18),
    ("Cliente91", 311, 116, 55),
    ("Cliente92", 739, 898, 75),
    ("Cliente93", 268, 97, 68),
    ("Cliente94", 176, 991, 100),
    ("Cliente95", 688, 588, 61),
    ("Cliente96", 107, 836, 24),
    ("Cliente97", 708, 522, 40),
    ("Cliente98", 679, 864, 48),
    ("Cliente99", 985, 877, 51),
    ("Cliente100", 954, 950, 78),
    ("Cliente101", 615, 750, 35),
    ("Sink", 365, 689, 0)  # Depósito de retorno com demanda 0
]

# Função para calcular a distância euclidiana entre dois pontos
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Criando o grafo e adicionando nós com suas demandas
G = nx.DiGraph()
for node, x, y, demand in nodes:
    G.add_node(node, demand=demand)

# Número de veículos e lista de capacidades
vehicle_capacities = [400, 600, 600, 800, 800, 1000, 1000]
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
prob = VehicleRoutingProblem(G, mixed_fleet=True, load_capacity=[400, 600, 600, 800, 800, 1000, 1000], use_all_vehicles=True)
# Solução do problema
prob.solve(greedy=True, time_limit=36000)
#prob.solve()


# Exibindo a solução
print(prob.best_value)
print("-----------------------------------------------")
print(prob.best_routes_type)
print("-----------------------------------------------")
print(prob.best_routes)