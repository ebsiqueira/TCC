from pyvrp import Model
import matplotlib.pyplot as plt
from pyvrp.stop import MaxRuntime
import math

from pyvrp.plotting import plot_coordinates, plot_solution

#(Augerat et al, No of trucks: 8, Optimal value: 450)
#CAPACITY : 35


# fmt: off
COORDS = [
    (30, 40),
    (35, 52),
    (49, 49),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 48),
    (58, 27),
    (37, 69)
]
DEMANDS = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
# fmt: on

m = Model()
m.add_vehicle_type(4, capacity=30)
m.add_vehicle_type(4, capacity=40)
# m.add_vehicle_type(8, capacity=35)

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

res = m.solve(stop=MaxRuntime(1000), display=True)  # one second
print(res)

_, ax = plt.subplots(figsize=(8, 8))
plot_solution(res.best, m.data(), ax=ax)
plt.show()