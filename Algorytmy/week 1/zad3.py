import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
numb_of_edges = 8
connections = []
G.add_nodes_from([i for i in range(numb_of_edges)])
for i in range(numb_of_edges):
    for j in range(numb_of_edges):
        if (i,j) not in connections and i != j:
            G.add_edge(i,j)
            connections.append((i,j))



pos = nx.circular_layout(G)
nx.draw(G, pos=pos)
plt.show()