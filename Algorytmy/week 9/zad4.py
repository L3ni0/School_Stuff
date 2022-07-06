import networkx as nx
import time
import random
import matplotlib.pyplot as plt
random.seed(100)


class Node:

    def __init__(self, data, color='blue'):
        self.data = data
        self.color = color
        self.connections = {}

    def add_connection(self, who):
        wage = random.randint(0, 100)
        self.connections[who.data] = wage
        who.connections[self.data] = wage

    def get_color(self):
        return self.color

    def get_wage(self, n2):
        return self.connections[n2]


class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.n = len(nodes)

    def search_nodes(self, d):
        for n in self.nodes:
            if n.data == d:
                return n

    def make_connections(self, limit):
        for i in range(limit):
            for node in self.nodes:
                # make sure not to connect 1 to 1
                node.add_connection(random.choice([n for n in self.nodes if n != node and n.data not in n.connections]))

        # do not connect same elements twice (making a set)
        # for node in self.nodes:
            # node.connections = dict(set(node.connections))

    def show(self, limit=2):
        self.make_connections(limit)
        for n in self.nodes:
            print(n.data, n.connections)

    def better_show(self, E=None, gpos=None):
        if not E:
            E = nx.Graph()

        # need a better way for color map
        data_nodes = []
        for n in self.nodes:
            data_nodes.append(n.data)
        E.add_nodes_from(data_nodes)

        # setting connections and color map
        color_map = []
        for n in self.nodes:
            for connection in n.connections:
                n2 = self.search_nodes(connection)
                E.add_edge(n.data, n2.data, weight=n.get_wage(n2.data))
            color_map.append(n.color)

        # print(color_map)
        # g_pos = gpos
        nx.draw(E, with_labels=True, node_color=color_map, pos=gpos)
        labels = nx.get_edge_attributes(E, 'weight')
        nx.draw_networkx_edge_labels(G, gpos, edge_labels=labels)
        plt.show()

    # color a single node
    def color_node(self, n, new_color='red'):
        self.search_nodes(n).color = new_color

    def kruskal(self, animate=False, gpos=None, E=None):
        conns = []

        def delete_same(arr1, arr2):
            if arr1[0] == arr2[1] and arr2[0] == arr1[1]:
                return True

        # add all connections
        for n in self.nodes:
            for cons in n.connections:
                conns.append([n.data, cons, n.connections[cons]])

        # remove duplicateses
        for i in conns:
            for j in conns:
                if delete_same(i, j):
                    conns.remove(j)
        print(conns)

        # sort connections
        conns = sorted(conns, key=lambda x: x[2])
        print(conns)

        result = []
        res_cons = []
        for con in conns:
            if con[0] or con[1] not in result:
                # result.append(con[0])
                result.append(con[1])
                self.color_node(con[0])
                self.color_node(con[1])
                res_cons.append(con)
                if animate:
                    self.better_show(E=E, gpos=gpos)
                    time.sleep(0.5)
            # result = list(set(result))

        for con in conns:
            if con not in result:
                E.remove_edge(con[0], con[1])

        print(result)
        print(res_cons)
        self.better_show(E=E, gpos=gpos)
        time.sleep(2)
        return res_cons

    def prim(self, animate=False, gpos=None, E=None):
        start = random.choice(self.nodes)
        result = [start.data]

        def mini_prim(current, parent):
            if not current:
                return None
            conns = []
            for cons in current.connections:
                conns.append([current.data, cons, current.connections[cons]])

            conns = sorted(conns, key=lambda x: x[2])

            for i in conns:
                if i[1] != parent.data and i[1] not in result:
                    result.append(i[1])
                    self.color_node(current.data)
                    self.color_node(parent.data)
                    self.color_node(i[1])
                    if animate:
                        self.better_show(E=E, gpos=gpos)
                        time.sleep(1)
                        print(i[1])
                    mini_prim(self.search_nodes(i[1]), current)
            return None

        mini_prim(start, start)
        print(result)
        return result


num = 10
nodes_list = []
n_l_d = []
for i in range(num):
    nodes_list.append(Node(i))
    n_l_d.append(nodes_list[i].data)

G = Graph(nodes_list)
# G.color_node(5)
G.show(1)
E = nx.Graph()
F = nx.Graph()
E.add_nodes_from(n_l_d)
F.add_nodes_from(n_l_d)
g_pos = nx.spring_layout(E)
# g_pos = nx.random_layout(E)
G.better_show(E=E, gpos=g_pos)
# G.prim(E=E, gpos=g_pos, animate=True)
new_cons = G.kruskal(E=E, gpos=g_pos, animate=False)
G.better_show(E=E, gpos=g_pos)
plt.clf()
plt.show()
T = nx.Graph()
exist = []
for fr,to,wage in new_cons:
    if not fr in exist:
        exist.append(fr)
        T.add_node(fr)

    if not
