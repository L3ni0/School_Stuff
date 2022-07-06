import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.Graph()
numb_of_edg = 100
xrange = 10
yrange = 10
i = 0
positions = {}
err = 0
while i < numb_of_edg:

    x = random.randint(0,xrange)
    y = random.randint(0, yrange)
    if [x,y] not in positions.values():
        G.add_node(i)
        positions[i] = [x,y]
        i += 1
        err = 0
    else:
        print(x,y)
        err += 1
        if err == 100:
            raise AssertionError('we tried draw 100 times ')


nx.draw(G, pos=positions)
plt.show()