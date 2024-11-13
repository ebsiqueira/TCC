from pyvrp import Model
import matplotlib.pyplot as plt
from pyvrp.stop import MaxRuntime
import math

from pyvrp.plotting import plot_coordinates, plot_solution

#(Augerat et al, No of trucks: 5, Optimal value: 784)
#CAPACITY : 100

# fmt: off
COORDS = [
    (30, 40),
    (37 , 52),
    (49 , 49),
    (52 , 64),
    (20 , 26),
    (40 , 30),
    (21 , 47),
    (17 , 63),
    (31 , 62),
    (52 , 33),
    (51 , 21),
    (42 , 41),
    (31 , 32),
    (5 , 25),
    (12 , 42),
    (36 , 16),
    (52 , 41),
    (27 , 23),
    (17 , 33),
    (13 , 13),
    (57 , 58),
    (62 , 42),
    (42, 57),
    (16 , 57),
    (8 , 52),
    (7 , 38),
    (27 , 68),
    (30 , 48),
    (43 , 67),
    (58 , 48),
    (58 , 27),
    (37 , 69),
    (38 , 46),
    (46 , 10),
    (61 , 33),
    (62 , 63),
    (63 , 69),
    (32 , 22),
    (45 , 35),
    (59 , 15),
    (5 , 6),
    (10 , 17),
    (21 , 10),
    (5 , 64),
    (30 , 15),
    (39 , 10),
    (32 , 39),
    (25 , 32),
    (25 , 55),
    (48 , 28),
    (56 , 37)
]
DEMANDS = [0, 7, 30, 16, 9, 21, 15, 19, 23, 11, 5, 19, 29, 23, 21, 10, 15, 3, 41, 9, 28, 8, 8, 16, 10,28, 7, 15, 14, 6, 19, 11, 12, 23, 26, 17, 6, 9, 15, 14, 7, 27, 13, 11, 16, 10, 5, 25, 17, 18, 10]
# fmt: on

m = Model()
m.add_vehicle_type(2, capacity=250)
m.add_vehicle_type(1, capacity=200)
m.add_vehicle_type(1, capacity=150)

depot = m.add_depot(x=COORDS[0][0], y=COORDS[0][1])
clients = [
    m.add_client(x=COORDS[idx][0], y=COORDS[idx][1], delivery=DEMANDS[idx])
    for idx in range(1, len(COORDS))
]

locations = [depot] + clients
for frm in locations:
    for to in locations:
        distance = math.sqrt((frm.x - to.x) ** 2 + (frm.y - to.y) ** 2) # Euclidiana
        #distance = abs(frm.x - to.x) + abs(frm.y - to.y)  # Manhattan
        m.add_edge(frm, to, distance=distance)

# _, ax = plt.subplots(figsize=(8, 8))
# plot_coordinates(m.data(), ax=ax)

res = m.solve(stop=MaxRuntime(10), display=True)  # one second
print(res)

_, ax = plt.subplots(figsize=(8, 8))
plot_solution(res.best, m.data(), ax=ax)
plt.show()