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
rotas = {
    0: [86, 50, 93, 55, 68, 16, 94, 49, 6, 2, 40, 0, 23, 78, 42, 46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    1: [31, 9, 92, 70, 7, 84, 4, 12, 36, 0],
    2: [69, 0, 5, 15, 45, 65, 88, 96, 19, 26, 87, 77, 35, 60],
    3: [18, 38, 44, 59, 3, 64, 24, 28, 10, 39, 14, 29, 72, 0],
    4: [48, 1, 25, 66, 89, 99, 54, 90, 33, 80, 8, 11, 85, 75, 30, 32],
    5: [62, 51, 98, 58, 27, 81, 97, 100, 91, 21, 34, 17, 61, 52, 83, 71, 53, 73, 76, 37],
    6: [79, 95, 74, 13, 41, 20, 47, 56, 82, 22, 57, 67, 63, 43, 0]
}

# Configurar o gráfico
fig, ax = plt.subplots(figsize=(12, 12))

# Cores diferentes para cada veículo
colors = plt.cm.get_cmap("tab10", len(rotas))

# Desenhar os clientes como bolinhas de mesma cor, exceto a coordenada 0
for cliente, coord in coordenadas.items():
    if cliente == 0:
        # Destacar a coordenada 0 com um símbolo diferente e maior
        ax.scatter(coord[0], coord[1], color='red', marker='X', s=100, label='Ponto de Partida')
    else:
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
ax.legend()

plt.tight_layout()
plt.show()
