import networkx as nx
import matplotlib.pyplot as plt
import random

random.seed(1000)

V = nx.Graph()
l_wierz = 30
lista_poz = [(random.randint(0,100),random.randint(0,100),0) for _ in range(l_wierz)]


def funkcja(nodes):
    A = nodes[:len(nodes)//2]
    B = nodes[len(nodes)//2:]
    C = funkcja(A)
    D = funkcja(B)
