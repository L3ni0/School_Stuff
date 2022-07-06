import networkx as nx
import matplotlib.pyplot as plt
import random
random.seed(1000)


class Node:

    def __init__(self, data, colour='grey'):
        self.data = data
        self.l_son = None
        self.r_son = None
        self.father = None
        self.colour = colour

    def add_l_son(self, son):
        son.father = self
        self.l_son = son

    def add_r_son(self, son):
        son.father = self
        self.r_son = son

    def change_colour(self, colour):
        self.colour = colour

    def gib_col(self):
        return self.colour


class Graph:

    def __init__(self, node=None, color_map=[]):
        self.node = node
        self.color_map = color_map

    def check_BST(self):

        def checking(who,min,max):
            if who == None:
                return True

            elif not min <= who.data <= max:
                return False

            return checking(who.l_son,min-1,who.data) and checking(who.r_son,who.data,max+1)

        return checking(self.node,self.find_min(),self.find_max()) # pierwsze min i max to najwieksze wartosci drzewa

    def correct_BST(self):

        def checking(who, min, max):
            if not who:
                return True

            elif not min <= who.data <= max:
                new = random.randint(min,max)
                print(f'changing {who.data} to {new}')
                who.data = new
                return False

            return checking(who.l_son,min,who.data-1) and checking(who.r_son,who.data+1,max)

        return checking(self.node,self.find_min(),self.find_max())

    def create_BST(self,nodes:list):
        nodes.sort()

        def spliting(nodes):

            if not nodes:
                return

            s = len(nodes) // 2
            nod = Node(nodes[s])

            l = spliting(nodes[:s])
            if l:
                nod.add_l_son(l)

            r = spliting(nodes[s+1:])
            if r:
                nod.add_r_son(r)

            return nod

        self.node = spliting(nodes)

    def find_min(self):

        def find(nod):

            if not nod.l_son:
                return nod.data

            return find(nod.l_son)

        return find(self.node)

    def find_max(self):

        def find(nod):

            if not nod.r_son:
                return nod.data

            return find(nod.r_son)

        return find(self.node)

    def add_color(self, color):
        self.color_map.append(color)

    def show(self):
        G = nx.Graph()
        color_map = self.color_map
        print(color_map)

        def connect(node):
            if node == None:
                return

            G.add_node(node.data)
            if node.father != None:
                G.add_edge(node.data, node.father.data)

            connect(node.r_son)
            connect(node.l_son)

        connect(self.node)

        nx.draw(G,  with_labels=True, arrows=True)
        plt.show()

    def check_color(self, current):
        cols = []

        def check_path(who):
            if who.l_son:
                cols.append(who.l_son.gib_col())
                check_path(who.l_son)

            elif who.r_son:
                cols.append(who.r_son.gib_col())
                check_path(who.r_son)

            else:
                if len(cols) > 2 and cols.count('red') != 0 and cols.count('grey') != 0:
                    if cols.count('grey') == cols.count('red'):
                        return True
                else:
                    return cols

        def check(node):
            color = node.gib_col()
            # print(color)
            # czarny korzen
            if node.data == nodes[0].data and color != 'grey':
                print(f'wierzcholek {node.data} NIE spelnia wymagania czarnego korzenia')
                return False

            # czarne liscie
            if not node.l_son and not node.r_son:
                if color == 'grey':
                    print(f'wierzcholek {node.data} spelnia wymagania')
                    return True
                else:
                    print(f'wierzcholek {node.data} NIE spelnia wymagania czarnych lisci')
                    return False
            if not node:
                return True

            # rownomierna sciezka
            if check_path(node):
                print(f'wierzcholek {node.data} NIE spelnia wymagania rownomiernej sciezki')
                # print(check_path(node))
                return False

            # rodzic czerwony - dzieci czarne
            if color == 'red':
                if node.l_son.gib_col() == 'grey' and node.r_son.gib_col() == 'grey':
                    print(f'wierzcholek {node.data} spelnia wymagania')
                    return True
                else:
                    print(f'wierzcholek {node.data} NIE spelnia wymagania rodzic-dziecko')
                    return False
            else:
                print(f'wierzcholek {node.data} spelnia wymagania')
                return True

        return check(current)


nodes = []
t1 = Node(1)
nodes.append(t1)
t2 = Node(2)
nodes.append(t2)
t3 = Node(3)
nodes.append(t3)
t4 = Node(4)
nodes.append(t4)
t5 = Node(5)
nodes.append(t5)
t6 = Node(6)
nodes.append(t6)
t7 = Node(7)
nodes.append(t7)
t8 = Node(8)
nodes.append(t8)


t1.add_l_son(t2)
t1.add_r_son(t3)
t2.add_l_son(t4)
t2.add_r_son(t5)
t3.add_l_son(t6)
t3.add_r_son(t7)
t4.add_l_son(t8)
# t4.add_l_son(t8)

t1.change_colour('red')
t8.change_colour('red')
# t7.change_colour('red')

g1 = Graph(t1)

for i in nodes:
    print(i.data, i.gib_col())
    g1.add_color(i.gib_col())
    g1.check_color(i)

g1.show()
