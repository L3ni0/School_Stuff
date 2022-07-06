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
        G = nx.DiGraph()
        for vert in self.vertList:
            G.add_node(vert.numb, label=vert.numb, title=str(vert.numb))
        self.pos = nx.spiral_layout(G)


    def addEdge(self, dr, to, wage=1):
        dr = self.vertList[dr]
        to = self.vertList[to]

        dr.connect(to, wage)

    def show(self):
        G = nx.DiGraph()
        for vert in self.vertList:
            G.add_node(vert.numb, label=vert.numb, title=str(vert.numb))
        for vert in self.vertList:
            for con in vert.conected_to:
                print(str(vert),str(con))
                G.add_edge(vert.numb, con.numb)
        nx.draw(G, with_labels=True, arrows=True,pos=self.pos)
        plt.show()

    def adjacency_matrix(self):
        mat = [[0 for _ in range(len(self.vertList))] for _ in range(len(self.vertList))]
        for vert in self.vertList:
            for con in vert.conected_to:
                mat[vert.numb][con.numb] = 1

        return mat

    def sortowanie_topologiczne(self):
        mat = self.adjacency_matrix() # i use adjacency_matrix because is easier for me to find conections
        sort_list = []

        dic = {} # dictionary: node : wage = len(list of nodes)
        for i in range(len(self.vertList)):
            dic[i] = []

        #starting values
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[j][i] > 0 :
                    dic[i].append(j)


        while dic:
            test = 1
            for key, list in dic.items():

                if len(list) == 0: #if we find 0 we need to del it in other keys

                    self.show_color(key,sort_list)

                    test = 0
                    for k in dic:
                        if key in dic[k]:
                            dic[k].remove(key)

                    sort_list.append(key)
                    del dic[key]
                    break

            if test:
                raise AssertionError('graf nie jest acykliczny')

        return sort_list



    def show_color(self,check,grey=[]):
        G = nx.DiGraph()
        color_map = []
        for vert in self.vertList:
            G.add_node(vert.numb, label=vert.numb, title=str(vert.numb))
            if vert.numb == check:
                color_map.append('yellow')
            elif vert.numb in grey:
                color_map.append('grey')
            else:
                color_map.append('green')

        for vert in self.vertList:
            for con in vert.conected_to:
                print(str(vert),str(con))
                G.add_edge(vert.numb, con.numb)
        nx.draw(G, with_labels=True, arrows=True, node_color=color_map,pos=self.pos)
        plt.show()

g1 = Graph_not('graph')
for i in range(6):
    g1.add_vertex(i)

g1.addEdge(0,2)
g1.addEdge(1,0)
g1.addEdge(1,2)
g1.addEdge(3,1)
g1.addEdge(3,0)
g1.addEdge(3,4)
g1.addEdge(4,1)
g1.addEdge(4,2)
g1.addEdge(5,0)
g1.addEdge(5,4)


g1.show()
print(np.matrix(g1.adjacency_matrix()))
print(g1.sortowanie_topologiczne())