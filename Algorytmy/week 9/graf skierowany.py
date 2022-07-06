import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class Vertex:

    def __init__(self, numb):
        self.numb = numb
        self.conected_to = {}

    def connect(self, to, wage):
        self.conected_to[to] = wage

    def is_alredy_conected(self, who):
        if who in self.conected_to:
            return True
        else:
            return False

    def __str__(self):
        return str(self.numb)

class Graph_not:

    def __init__(self,name):
        self.name = name
        self.vertList = []
        self.nm_vert = 0

    def add_vertex(self, name):
        self.vertList.append(Vertex(name))

    def addEdge(self, dr, to, wage):
        dr = self.vertList[dr]
        to = self.vertList[to]

        dr.connect(to, wage)

    def show(self):
        G = nx.DiGraph()
        for vert in self.vertList:
            G.add_node(vert.numb, label=vert.numb, title=str(vert.numb))
        for vert in self.vertList:
            for con in vert.conected_to:
                G.add_edge(vert.numb, con.numb)
        nx.draw(G, with_labels=True, arrows=True)
        plt.show()

    def adjacency_matrix(self):
        mat = [[0 for _ in range(len(self.vertList))] for _ in range(len(self.vertList))]
        for vert in self.vertList:
            for con in vert.conected_to:
                mat[vert.numb][con.numb] = 1
        return np.matrix(mat)

    def incidence_matrix(self):
        e = 0
        for vert in self.vertList:
            for con in vert.conected_to:
                e += 1

        k = 0
        mat = [[0 for _ in range(e)] for _ in range(len(self.vertList))]
        for vert in self.vertList:
            for con in vert.conected_to:
                mat[vert.numb][k] = 1
                mat[con.numb][k] = -1
                k+= 1

        return np.matrix(mat)

    def find_path(self,fr,to):
        m = self.adjacency_matrix()
        if m[fr][to].tolist() == 1:
            return 1

        temp = m
        for i in range(2,len(self.vertList)):
            temp = temp * m
            if m[fr][to].tolist() >= 1:
                return i

        return 0


g1 = Graph_not('graph')
for i in range(8):
    g1.add_vertex(i)

for i in range(8):
    for j in range(8):
        if i != j:
            g1.addEdge(i,j,1)
            g1.addEdge(j, i, 1)


g1.show()
print(g1.adjacency_matrix())
print(g1.incidence_matrix())
print(g1.is_fully_connected())