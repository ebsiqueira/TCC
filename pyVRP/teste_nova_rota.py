import matplotlib.pyplot as plt

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

# Tour fornecido
tour = [29, 49, 21, 8, 81, 61, 80, 70, 45, 76, 62, 51, 1, 52, 27, 13, 91, 74, 71, 84, 98, 30, 55, 4, 97, 34, 17, 90, 83, 85, 7, 100, 73, 99, 33, 89, 68, 69, 54, 86, 93, 11, 53, 75, 36, 9, 16, 12, 66, 18, 87, 92, 58, 40, 2, 6, 64, 56, 19, 50, 79, 95, 60, 43, 94, 44, 10, 42, 46, 65, 24, 20, 41, 39, 25, 3, 5, 23, 15, 26, 72, 32, 22, 0, 31, 63, 35, 0, 96, 57, 48, 59, 0, 38, 88, 82, 47, 28, 67, 14, 78, 77, 0, 0, 0, 37, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Veículos usados
veiculos = [6, 6, 0, 1, 0, 0, 1, 2, 6, 2, 2, 2, 1, 2, 1, 6, 0, 6, 0, 6, 0, 0, 6, 6, 1, 1, 1, 0, 2, 2, 0, 1, 1, 2, 1, 2, 6, 6, 6, 6, 6, 1, 6, 1, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 2, 5, 5, 6, 6, 6, 5, 5, 4, 5, 5, 5, 4, 5, 4, 3, 3, 3, 3, 3, 3, 5, 5, 1, 4, 3, 3, 3, 2, 2, 2, 3, 0, 0, 4, 4, 2, 6, 0, 6, 6, 3, 6, 0, 0, 6, 0, 1, 4, 2, 4, 5, 6, 0, 0, 3, 4, 0, 0, 0, 0]

# Função para identificar sequências de clientes atendidos pelo mesmo veículo
def identificar_sequencias(tour, veiculos):
    rotas = []
    rota_atual = []
    veiculo_atual = veiculos[0]
    
    for i, cliente in enumerate(tour):
        if veiculos[i] == veiculo_atual:
            rota_atual.append(cliente)
        else:
            if rota_atual:
                rotas.append((veiculo_atual, rota_atual))
            veiculo_atual = veiculos[i]
            rota_atual = [cliente]
    
    if rota_atual:
        rotas.append((veiculo_atual, rota_atual))
    
    return rotas

# Obter as sequências de rotas
rotas_sequenciais = identificar_sequencias(tour, veiculos)

# Função para alternar a visibilidade das rotas ao clicar na legenda
def toggle_visibility(event):
    legend = event.artist
    is_visible = not legend.get_visible()  # Alternar visibilidade
    
    # Alterar visibilidade para todas as linhas associadas
    for legline, origline in zip(ax.get_legend().get_lines(), ax.lines):
        if legline == legend:
            origline.set_visible(is_visible)
            legline.set_visible(is_visible)
    
    plt.draw()

# Plotar as rotas no gráfico
fig, ax = plt.subplots()

# Cores para os veículos
cores = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
legendas = []

# Plotar cada rota completa (Depósito -> Rota -> Depósito)
for i, (veiculo, rota) in enumerate(rotas_sequenciais):
    cor = cores[i % len(cores)]  # Escolher a cor para o veículo
    
    # Desenhar a ida do depósito para o primeiro cliente
    x_coords = [coordenadas[0][0], coordenadas[rota[0]][0]]
    y_coords = [coordenadas[0][1], coordenadas[rota[0]][1]]
    linha, = ax.plot(x_coords, y_coords, cor, marker='o', label=f"Veículo {veiculo} - Rota {i+1}")
    
    # Desenhar a rota entre os clientes
    for j in range(len(rota) - 1):
        x_coords = [coordenadas[rota[j]][0], coordenadas[rota[j + 1]][0]]
        y_coords = [coordenadas[rota[j]][1], coordenadas[rota[j + 1]][1]]
        ax.plot(x_coords, y_coords, cor, marker='o')
        
    # Desenhar a volta do último cliente para o depósito
    x_coords = [coordenadas[rota[-1]][0], coordenadas[0][0]]
    y_coords = [coordenadas[rota[-1]][1], coordenadas[0][1]]
    ax.plot(x_coords, y_coords, cor, marker='o')
    
    legendas.append(linha)

# Plotar o depósito
ax.scatter(coordenadas[0][0], coordenadas[0][1], color='r', marker='*', s=200, label='Depósito')

# Configurar a legenda
legenda = ax.legend(loc='upper left', title="Rotas")
for legline in legenda.get_lines():
    legline.set_picker(True)  # Habilitar clique na legenda

# Conectar evento de clique à função toggle_visibility
fig.canvas.mpl_connect('pick_event', toggle_visibility)

# Melhorar visualização
ax.set_title('Rotas dos veículos')
ax.set_xlabel('Coordenada X')
ax.set_ylabel('Coordenada Y')

plt.show()
