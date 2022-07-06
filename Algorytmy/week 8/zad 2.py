import networkx as nx
import matplotlib.pyplot as plt
import random


class Robot:

    def __init__(self, id, typ, masa, zasieg, rozdzielczosc):
        self.id = id
        self.typ = typ
        self.masa = masa
        self.zasieg = zasieg
        self.rozdzielczosc = rozdzielczosc

    def show(self):
        return [self.id, self.typ, self.masa, self.zasieg, self.rozdzielczosc]

    def __str__(self):
        return str([self.id, self.typ, self.masa, self.zasieg, self.rozdzielczosc])

class Flota:

    def __init__(self):
        self.wektor= []

    def dodaj_robota(self,id, typ, masa, zasieg, rozdzielczosc):
        self.wektor.append(Robot(id, typ, masa, zasieg, rozdzielczosc))

    def generuj_opis(self, N):
        id = ''.join([chr(random.randint(65,90)) for _ in range(N)])
        typ = random.choice(['AUV','AVF','AGV'])
        masa = random.randint(50,2000)
        zasieg = random.randint(1,1000)
        rozdzielczosc = random.randint(1,30)
        self.dodaj_robota(id, typ, masa, zasieg, rozdzielczosc)

    def generuj_flote(self, M, N):
        for _ in range(M):
            self.generuj_opis(N)

    def wyswietl(self):
        print('|'.join([str(j).ljust(14) for j in ['identyfikator','typ','masa','zasieg','rozdzielczosc']]))
        for info in self.wektor:
            info = info.show()
            print('|'.join([str(j).ljust(14) for j in info]))

    def zapisz_do_pliku(self,plik):
        with open(plik,'w') as plik:
            for info in self.wektor:
                info = info.show()
                plik.write(' '.join(str(j) for j in info)+'\n')

    def odczytaj_plik(self,plik):
        with open(plik, 'r') as plik:
            for linijka in plik.readlines():
                id,t,m,z,r = [int(i) if i.isdigit() else i for i in linijka.strip().split()]
                self.dodaj_robota(id,t,m,z,r)

    def sortowanie_przez_zliczanie(self,look):
        zliczone = [[] for i in range(2000)]
        for rob  in self.wektor:
            zliczone[rob.show()[look]].append(rob)

        wynik = []
        for l in zliczone:
            if l:
                wynik.extend(l)

        self.wektor = wynik

        return wynik

class Node():

    def __init__(self, data):
        self.data = data
        self.l_son = None
        self.r_son = None
        self.father = None

    def add_l_son(self, son):
        son.father = self
        self.l_son = son

    def add_r_son(self, son):
        son.father = self
        self.r_son = son


class Graph:

    def __init__(self, node=None, look = 3):
        self.node = node
        self.look = look

    def check_BST(self):

        def checking(who,min,max):
            if who == None:
                return  True

            elif not min <= who.data <= max:
                return False

            return checking(who.l_son,min-1,who.data) and checking(who.r_son,who.data,max+1)

        return checking(self.node,self.find_min(),self.find_max()) # pierwsze min i max to najwieksze wartosci drzewa

    def correct_BST(self):

        def checking(who,min,max):
            if who == None:
                return True

            elif not min <= who.data <= max:
                new = random.randint(min,max)
                print(f'changing {who.data} to {new}')
                who.data = new
                return False

            return checking(who.l_son,min,who.data-1) and checking(who.r_son,who.data+1,max)

        return checking(self.node,self.find_min(),self.find_max())

    def create_BST_from_flota(self,flota):
        nodes = flota.sortowanie_przez_zliczanie(self.look)

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
                return nod.data.show()[self.look]

            return find(nod.l_son)

        return find(self.node)


    def find_max(self):

        def find(nod):

            if not nod.r_son:
                return nod.data.show()[self.look]

            return find(nod.r_son)

        return find(self.node)


    def show(self):
        G = nx.Graph()
        colors = []
        def connect(node,color='blue'):
            if node == None:
                return

            G.add_node(node.data.show()[self.look])
            colors.append(color)
            if node.father != None:
                G.add_edge(node.data.show()[self.look], node.father.data.show()[self.look])

            connect(node.r_son, color='green')
            connect(node.l_son, color='red')

        connect(self.node)

        nx.draw(G,  with_labels=True, arrows=True,node_color=colors)
        plt.show()

    def pre_order(self):

        def Order(node):
            if not node:
                return

            print(node.data.show())
            Order(node.l_son)
            Order(node.r_son)

        Order(self.node)

    def in_order(self):

        def Order(node):
            if not node:
                return

            Order(node.l_son)
            print(node.data.show())
            Order(node.r_son)

        Order(self.node)

    def post_order(self):

        def Order(node):
            if not node:
                return

            Order(node.l_son)
            Order(node.r_son)
            print(node.data.show())

        Order(self.node)

    def find(self,who):

        def finding(node):
            if not node:
                return

            print(node.data.show()[self.look])
            if node.data.show()[self.look] == who:
                return node
            elif node.data.show()[self.look] < who:
                return finding(node.r_son)
            else:
                return finding(node.l_son)

        return finding(self.node)

    def find_parent_and_child(self,who):

        def finding(node):
            if not node:
                return

            if node.data.show()[self.look] == who:
                return f'poprzednik:{node.father.data.show()}\n' \
                       f'nasepniki: {node.r_son.data}, {node.l_son.data}'

            elif node.data.show()[self.look] < who:
               return finding(node.r_son)
            else:
               return finding(node.l_son)

        return finding(self.node)


f1 = Flota()
f1.odczytaj_plik('roboty.txt')
f1.wyswietl()

g1 = Graph(look=2)
g1.create_BST_from_flota(f1)
g1.show()
print(f'minimum: {g1.find_min()}')
print(f'max: {g1.find_max()}')

print('szukanie 1852')
g1.find(1852)
print('--------------------')

print(g1.find_parent_and_child(1852))

