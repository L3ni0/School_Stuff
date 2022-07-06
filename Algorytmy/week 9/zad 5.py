import random
import copy
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time

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


class Graph:

    def __init__(self,name):
        self.name = name
        self.vertList = []
        self.nm_vert = 0

    def add_vertex(self, name):
        self.vertList.append(Vertex(name))

    def addEdge(self, dr, to, wage):
        dr = self.vertList[dr]
        to = self.vertList[to]
        if not dr.is_alredy_conected(to) and not to.is_alredy_conected(dr):  # connecting in tow ways
            dr.connect(to, wage)
            to.connect(dr, wage)

    def show_connected_component(self):
        list_of_comp = []
        for vert in self.vertList:
            comp = set()
            queue = [vert]
            while queue:  # we are checking every connection between vertex
                comp.add(queue[0].numb)
                for el in queue[0].conected_to:
                    if not el.numb in comp:
                        queue.append(el)
                del queue[0]
            if not comp in list_of_comp:  # if component wasn't in list it mean this is new conetrion
                list_of_comp.append(comp)
        return list_of_comp


    def show_conection(self):
        for vert in self.vertList:
            for con in vert.conected_to:
                print(vert.numb, con.numb, vert.conected_to[con])


    def dijkstra_algorytm(self, start, stop): #we are going to each conection and check if next vertex is stop-vertex
        if len(self.show_connected_component()) == 1:
            start = self.vertList[start]
            stop = self.vertList[stop]

            def find_and_calculate(where ,stop, value, steps):
                if where == stop:
                    return value,steps
                else:
                    old_step = copy.deepcopy(steps)
                    old_value = value

                    for el in where.conected_to :
                        if not el.numb in old_step:
                            temp_step = copy.deepcopy(old_step)
                            temp_step.append(el.numb)

                            value_temp, steps_temp = find_and_calculate(el, stop, old_value + el.conected_to[where], temp_step)
                            if (value_temp < value or steps[-1] != stop.numb) and steps_temp[-1] == stop.numb:
                                value = value_temp
                                steps = steps_temp

                    return value,steps

            self.show_conection()
            return find_and_calculate(start,stop,0,[start.numb])



        else:
            return "this is not correct type of graph"

    def show(self):
        G = nx.Graph()
        for vert in self.vertList:
            G.add_node(vert.numb, label=vert.numb, title=str(vert.numb))
        for vert in self.vertList:
            for con in vert.conected_to:
                G.add_edge(vert.numb, con.numb, label=vert.conected_to[con])
        nx.draw(G, with_labels=True, arrows=False)
        plt.show()

    def floyd_warshal(self,fr,to):
        mat = [[10000 for _ in range(len(self.vertList))] for _ in range(len(self.vertList))] #i use 10000 beside inf
        for i in range(len(self.vertList)):
            mat[i][i] = 0

        for vert in self.vertList:
            for con in vert.conected_to:
                mat[vert.numb][con.numb] = vert.conected_to[con]


        for k in range(len(mat)):
            for i in range(len(mat)):
                for j in range(len(mat)):
                    mat[i][j] = min((mat[i][j], mat[i][k] + mat[k][j]))

        print(np.matrix(mat))
        return mat[fr][to]




# g1 = Graph('hqy')
# for i in range(8):
#     g1.add_vertex(i)
#
# for i in range(20):
#     a = random.randint(0,7)
#     b = random.randint(0,7)
#     if a != b:
#         g1.addEdge(a,b, random.randint(1,10))
time_d = []
time_floyd = []

for x in range(5,20):
    g = Graph('test')
    for i in range(x):
        g.add_vertex(i)

    for i in range(x):
        for j in range(x):
            if i != j:
                g.addEdge(i,j,random.randint(1,10))

    start = time.time()
    g.dijkstra_algorytm(0,4)
    time_d.append(time.time()-start)

    start = time.time()
    g.floyd_warshal(0, 4)
    time_floyd.append(time.time() - start)

    print(f'----{x}------')

plt.plot(time_d, label='time dikstra')
plt.plot(time_floyd, label='time floyd')
plt.legend()
plt.show()


