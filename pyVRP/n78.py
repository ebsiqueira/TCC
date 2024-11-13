from pyvrp import Model
import matplotlib.pyplot as plt
from pyvrp.stop import MaxRuntime

from pyvrp.plotting import plot_coordinates, plot_solution

# fmt: off
COORDS = [
    (46, 12), 
    (51, 4), 
    (52, 30), 
    (80, 70), 
    (18, 90), 
    (59, 39), 
    (23, 59), 
    (77, 48), 
    (82, 30), 
    (18, 82), 
    (11, 41), 
    (7, 9), 
    (88, 33), 
    (23, 88), 
    (0, 76), 
    (85, 34), 
    (17, 46), 
    (52, 10), 
    (13, 45), 
    (19, 85), 
    (86, 77), 
    (54, 6), 
    (83, 32), 
    (15, 10), 
    (53, 5), 
    (14, 42), 
    (13, 10), 
    (57, 32), 
    (20, 85), 
    (65, 46), 
    (61, 42), 
    (87, 52), 
    (79, 51), 
    (25, 91), 
    (89, 34), 
    (26, 100), 
    (0, 88), 
    (63, 43), 
    (55, 10), 
    (23, 86), 
    (8, 18), 
    (0, 74), 
    (20, 44), 
    (56, 7), 
    (14, 10), 
    (88, 40), 
    (96, 38), 
    (59, 31), 
    (22, 87), 
    (59, 36), 
    (24, 83), 
    (83, 37), 
    (53, 5), 
    (0, 37), 
    (84, 78), 
    (27, 93), 
    (61, 12), 
    (69, 43), 
    (54, 9), 
    (20, 98), 
    (18, 50), 
    (25, 84), 
    (31, 69), 
    (58, 36), 
    (0, 11), 
    (61, 36), 
    (18, 49), 
    (57, 8), 
    (0, 49), 
    (56, 8), 
    (62, 45), 
    (83, 32), 
    (53, 10), 
    (82, 53), 
    (21, 85), 
    (64, 41), 
    (80, 50), 
    (16, 10)
]
DEMANDS = [0, 14, 17, 17, 16, 19, 17, 5, 12, 4, 2, 2, 26, 2, 7, 18, 6, 6, 18, 2, 14, 5, 9, 4, 3, 15, 4, 23, 7, 21, 4, 1, 6, 16, 4, 20, 5, 14, 14, 26, 5, 2, 14, 11, 21, 20, 18, 2, 19, 12, 22, 14, 23, 25, 8, 3, 9, 21, 3, 22, 6, 2, 22, 20, 5, 13, 6, 14, 16, 12, 23, 5, 12, 15, 21, 4, 23, 19]
# fmt: on

m = Model()
m.add_vehicle_type(3, capacity=60)
m.add_vehicle_type(2, capacity=80)
m.add_vehicle_type(3, capacity=120)
m.add_vehicle_type(2, capacity=140)

depot = m.add_depot(x=COORDS[0][0], y=COORDS[0][1])
clients = [
    m.add_client(x=COORDS[idx][0], y=COORDS[idx][1], delivery=DEMANDS[idx])
    for idx in range(1, len(COORDS))
]

locations = [depot] + clients
for frm in locations:
    for to in locations:
        distance = abs(frm.x - to.x) + abs(frm.y - to.y)  # Manhattan
        m.add_edge(frm, to, distance=distance)

# _, ax = plt.subplots(figsize=(8, 8))
# plot_coordinates(m.data(), ax=ax)

res = m.solve(stop=MaxRuntime(100), display=True)  # one second
print(res)

_, ax = plt.subplots(figsize=(8, 8))
plot_solution(res.best, m.data(), ax=ax)
plt.show()