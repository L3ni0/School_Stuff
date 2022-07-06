# %%init+
import random
from pyvis.network import Network
import copy


net = Network()
net.add_node(1, label='1')
net.add_node(2)
net.add_node(3)
net.add_edge(1, 2, value=4, title=4)
net.add_edge(1, 1, title=1)
net.add_edge(3, 1, value=7, title=3)


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

    def delete_connection(self,el1 , el2):
        if not el1.is_alredy_conected(el2) and not el1.is_alredy_conected(el2):
            del el1.conected_to[el2]
            del el2.conected_to[el1]
            print('ege was deleted')


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



    def kruskal_algorytm(self):
        print(self)
        if len(self.show_connected_component()) != 1:
            return "this is not correct type of graph"

        new_graph = Graph('new_guy')
        in_graph = set()
        connect_list = []
        for i in range(len(self.vertList)):
            new_graph.add_vertex(i)
        for vert in self.vertList:
            for con in vert.conected_to:
                connect_list.append([vert.conected_to[con], [con.numb, vert.numb]])

        connect_list.sort()
        for connection in connect_list:
            if not(connection[1][0] in in_graph and connection[1][1] in in_graph):
                new_graph.addEdge(connection[1][0], connection[1][1], connection[0])
                in_graph.add(connection[1][0])
                in_graph.add(connection[1][1])

        while len(new_graph.show_connected_component()) != 1:
            components = list(new_graph.show_connected_component())
            for connection in connect_list:
                if connection[1][0] in list(components[0]) and not(connection[1][1] in list(components[0])):
                    new_graph.addEdge(connection[1][0], connection[1][1], connection[0])
                    in_graph.add(connection[1][0])
                    in_graph.add(connection[1][1])
                    break

        new_graph.show()
        return new_graph


    def show(self):
        net = Network('1000px','1000px')
        for vert in self.vertList:
            net.add_node(vert.numb)
        for vert in self.vertList:
            for con in vert.conected_to:
                net.add_edge(vert.numb, con.numb, label=vert.conected_to[con])
        net.show('graph.html')
        print('picture has been generated')

#%% generate

g1 = Graph('hqy')
for i in range(8):
    g1.add_vertex(i)

for i in range(20):
    a = random.randint(0,7)
    b = random.randint(0,7)
    if a != b:
        g1.addEdge(a,b, random.randint(1,10))




g1.show()

#%% dijkstra_algorytm
print(g1.dijkstra_algorytm(7,5))
#%% kruskal

