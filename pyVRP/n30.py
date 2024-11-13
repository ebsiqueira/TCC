from pyvrp import Model
import matplotlib.pyplot as plt
from pyvrp.stop import MaxRuntime
import math

from pyvrp.plotting import plot_coordinates, plot_solution

#(Augerat et al, No of trucks: 5, Optimal value: 784)
#CAPACITY : 100

# fmt: off
COORDS = [
    (82, 76),
    (96 , 44),
    (50 , 5),
    (49 , 8),
    (13 , 7),
    (29 , 89),
    (58 , 30),
    (84 , 39),
    (14 , 24),
    (2 , 39),
    (3 , 82),
    (5 , 10),
    (98 , 52),
    (84 , 25),
    (61 , 59),
    (1 , 65),
    (88 , 51),
    (91 , 2),
    (19 , 32),
    (93 , 3),
    (50 , 93),
    (98 , 14),
    (5 , 42),
    (42 , 9),
    (61 , 62),
    (9 , 97),
    (80 , 55),
    (57 , 69),
    (23 , 15),
    (20 , 70),
    (85 , 60),
    (98 , 5)
]
DEMANDS = [0, 19, 21, 6, 19, 7, 12, 16, 6, 16, 8, 14, 21, 16, 3, 22, 18, 19, 1, 24, 8, 12, 4, 8, 24, 24, 2, 20, 15, 2, 14, 9]
# fmt: on

m = Model()
m.add_vehicle_type(2, capacity=90)
m.add_vehicle_type(2, capacity=100)
m.add_vehicle_type(1, capacity=120)
#m.add_vehicle_type(5, capacity=100)

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