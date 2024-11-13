import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

# Coordenadas dos clientes
coordenadas = {
    0: (365, 689), 1: (146, 180), 2: (792, 5), 3: (658, 510), 4: (461, 270), 5: (299, 531),
    6: (812, 228), 7: (643, 90), 8: (615, 630), 9: (258, 42), 10: (616, 299), 11: (475, 957),
    12: (425, 473), 13: (406, 64), 14: (656, 369), 15: (202, 467), 16: (318, 21), 17: (579, 587),
    18: (458, 354), 19: (575, 871), 20: (47, 512), 21: (568, 742), 22: (128, 436), 23: (546, 806),
    24: (197, 696), 25: (615, 300), 26: (852, 563), 27: (772, 803), 28: (678, 342), 29: (916, 176),
    30: (390, 949), 31: (113, 782), 32: (226, 736), 33: (119, 923), 34: (584, 572), 35: (134, 554),
    36: (912, 173), 37: (827, 233), 38: (851, 677), 39: (598, 322), 40: (627, 472), 41: (94, 442),
    42: (688, 274), 43: (977, 176), 44: (597, 461), 45: (931, 23), 46: (170, 640), 47: (941, 601),
    48: (873, 487), 49: (797, 95), 50: (451, 816), 51: (866, 970), 52: (833, 912), 53: (106, 913),
    54: (260, 107), 55: (332, 45), 56: (685, 613), 57: (728, 372), 58: (487, 497), 59: (702, 440),
    60: (717, 412), 61: (635, 794), 62: (927, 972), 63: (635, 356), 64: (634, 540), 65: (658, 261),
    66: (303, 168), 67: (707, 410), 68: (254, 135), 69: (346, 29), 70: (75, 79), 71: (893, 987),
    72: (729, 372), 73: (29, 910), 74: (356, 39), 75: (274, 943), 76: (322, 96), 77: (664, 396),
    78: (704, 236), 79: (415, 837), 80: (576, 587), 81: (750, 977), 82: (726, 363), 83: (861, 948),
    84: (302, 129), 85: (415, 989), 86: (199, 135), 87: (801, 405), 88: (679, 426), 89: (994, 804),
    90: (311, 116), 91: (739, 898), 92: (268, 97), 93: (176, 991), 94: (688, 588), 95: (107, 836),
    96: (708, 522), 97: (679, 864), 98: (985, 877), 99: (954, 950), 100: (615, 750)
}

# Rotas por veículo
# rotas = {
#     0: [4, 92, 1, 94, 100, 80, 69, 81, 43, 0, 6, 26, 67],
#     1: [71, 93, 70, 55, 86, 16, 9, 39, 66, 0, 48, 23, 38, 87, 10, 46, 77, 0, 36],
#     2: [89, 99, 52, 33, 83, 21, 8, 61, 17, 34, 64, 29],
#     3: [78, 44, 25, 56, 95, 15, 88, 5, 22, 24, 28, 82],
#     4: [37, 35, 41, 20, 72, 57, 59, 3, 63, 0],
#     5: [27, 97, 73, 58, 91, 62, 75, 30, 11, 79, 68, 12, 18, 42, 32, 96, 14, 49, 0],
#     6: [90, 54, 45, 7, 76, 13, 51, 98, 85, 53, 84, 74, 2, 50, 19, 40, 65, 31, 60, 47]
# }

rotas = {
    0: [21, 81, 61, 91, 71, 98, 30, 90, 7, 0, 96, 38, 67, 14, 77, 0, 0, 0, 0, 0, 0],
    1: [8, 80, 1, 27, 97, 34, 17, 100, 73, 33, 11, 75, 15, 0],
    2: [70, 76, 62, 51, 52, 83, 85, 99, 89, 6, 0, 31, 63, 59, 0],
    3: [24, 20, 41, 39, 25, 3, 72, 32, 22, 35, 47, 0],
    4: [87, 92, 58, 40, 2, 43, 42, 65, 26, 57, 48, 0, 37, 0],
    5: [36, 9, 16, 12, 66, 18, 64, 56, 95, 60, 94, 44, 10, 46, 5, 23, 0],
    6: [29, 49, 45, 13, 74, 84, 55, 4, 68, 69, 54, 86, 93, 53, 19, 50, 79, 0, 88, 82, 28, 78, 0],
}

# Rotas por veículo (5000 samples)
# rotas = {
#     0: [43, 56, 94, 40, 3, 63, 26, 37, 0, 48, 0, 0, 0, 0],
#     1: [95, 66, 55, 84, 92, 80, 69, 70, 86, 34, 9, 7, 29, 87, 0, 46, 0],
#     2: [58, 21, 73, 51, 99, 98, 91, 90, 16, 68, 76, 81, 0],
#     3: [19, 36, 77, 2, 32, 31, 96, 38, 47, 10, 88, 82, 67, 0, 59, 60, 0],
#     4: [64, 4, 18, 97, 33, 53, 13, 52, 11, 75, 30, 85, 50, 79, 24, 0],
#     5: [44, 39, 5, 35, 15, 41, 65, 42, 78, 14, 22, 25, 72, 49, 6, 0, 28, 23, 0, 57, 0],
#     6: [20, 93, 89, 71, 83, 62, 27, 74, 54, 1, 12, 17, 61, 8, 100, 45, 0],
# }

# Configurar o gráfico
fig, ax = plt.subplots(figsize=(12, 12))

# Cores diferentes para cada veículo
colors = plt.cm.get_cmap("tab10", len(rotas))

# Desenhar os clientes como bolinhas de mesma cor
for cliente, coord in coordenadas.items():
    ax.scatter(coord[0], coord[1], color='black', s=50)

# Armazenar as linhas de cada veículo para controle de exibição
veiculo_lines = []

# Desenhar as rotas de cada veículo com linhas coloridas e armazená-las
for veiculo, clientes in rotas.items():
    lines = []
    for i in range(len(clientes) - 1):
        cliente_atual = clientes[i]
        cliente_proximo = clientes[i + 1]
        coord_atual = coordenadas[cliente_atual]
        coord_proximo = coordenadas[cliente_proximo]
        line, = ax.plot([coord_atual[0], coord_proximo[0]], [coord_atual[1], coord_proximo[1]], 
                        color=colors(veiculo), alpha=0.8, lw=2)
        lines.append(line)
    veiculo_lines.append(lines)

# Caixa de seleção de veículos
rax = plt.axes([0.02, 0.4, 0.15, 0.35], facecolor='lightgoldenrodyellow')
labels = [f'Veículo {i}' for i in range(len(rotas))]
visibility = [True] * len(rotas)
check = CheckButtons(rax, labels, visibility)

# Função de atualização para exibir/ocultar veículos
def toggle_lines(label):
    index = labels.index(label)
    for line in veiculo_lines[index]:
        line.set_visible(not line.get_visible())
    plt.draw()

check.on_clicked(toggle_lines)

# Definir títulos e rótulos
ax.set_title('Rotas dos Veículos pelos Clientes', fontsize=16)
ax.set_xlabel('Coordenada X', fontsize=12)
ax.set_ylabel('Coordenada Y', fontsize=12)
ax.grid(True)

plt.tight_layout()
plt.show()