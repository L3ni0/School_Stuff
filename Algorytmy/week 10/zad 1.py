import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from collections import deque

from itertools import tee

from copy import deepcopy

from typing import List, Set, Tuple, Any, Optional, Type

links_to = lambda nei, start: [i for i, cell in enumerate(nei[start]) if cell > 0]

class Graph:
    def __init__(self, V,labels, directed=False):
        self.neighbour = list_to_neighbour(V, directed)
        self.labels = labels
        self.default = V
        self.directed = directed
        self.pos = None

    @classmethod
    def from_file(cls: Type["Graph"], path: str, directed=False):
        with open(path, "r") as file:
            content = file.read().split("\n")

        labels = content[0].split(" ")
        if len(labels) != len(set(labels)):
            raise KeyError("labels cannot repeat")

        tr = {name: node_id for node_id, name in enumerate(labels)}

        edges = []
        weights = []
        for i in range(1, len(content)):
            start, *conns = content[i].split(" ")
            for connection in conns:
                end, weight = connection.split(":")
                edges.append((tr[start], tr[end]))
                weights.append(int(weight))

        return cls((list(tr.values()), edges, weights), labels, directed=directed)


    def draw(self, add_edges = [[], []], draw_args=None):
        graph = (nx.DiGraph if self.directed else nx.Graph)()
        for name, _id in zip(self.labels, range(len(self.neighbour))):
            graph.add_node(_id, label=name)

        for i, row in enumerate(self.neighbour):
            for j, weight in enumerate(row):
                if weight:
                    graph.add_edge(i, j, weight=weight, color="#000000")

        if add_edges:
            for (start, end), weight in zip(add_edges[0], add_edges[1]):
                graph.add_edge(start, end, weight=weight, color="#FF0000")

        if not self.pos:
            self.pos = nx.spring_layout(graph)

        normal = [(i, j) for i in range(len(self.neighbour)) for j in links_to(self.neighbour, i)]
        new = add_edges[0]

        edge_colors_normal = [d["color"] for u, v, d in graph.edges(data=True) if (u, v) in normal]
        edge_colors_new = [d["color"] for u, v, d in graph.edges(data=True) if (u, v) in new]

        edge_weights_normal = {node: weight for node, weight in
                               [((u, v), d["weight"]) for u, v, d in graph.edges(data=True) if (u, v) in normal]}
        edge_weights_new = {node: weight for node, weight in zip(add_edges[0], add_edges[1])}

        color = {1: "blue", -1: "red", 2: "pink", -2: "teal"}

        colors = [color[draw_args["color"][i]] for i in range(len(draw_args["color"]))] if draw_args and type(
            draw_args["color"]) is np.ndarray else "#1f78b4"
        pos = draw_args["pos"] if draw_args and "pos" in draw_args else self.pos

        nx.draw_networkx_nodes(graph, pos, node_color=colors)
        nx.draw_networkx_labels(graph, pos, nx.get_node_attributes(graph, "label"))
        nx.draw_networkx_edges(graph, pos, normal, edge_color=edge_colors_normal, connectionstyle='arc3, rad = 0.1')
        nx.draw_networkx_edge_labels(graph, pos, edge_weights_normal, font_color=edge_colors_normal[0], label_pos=1 / 3)
        if new:
            nx.draw_networkx_edges(graph, pos, new, edge_color=edge_colors_new, connectionstyle='arc3, rad = 0.3')
            nx.draw_networkx_edge_labels(graph, pos, edge_weights_new,
                                         font_color=edge_colors_new[0] if edge_colors_new else "black", label_pos=1 / 3)
        plt.show()

def list_to_neighbour(V, directed=False):
    if len(V) == 3:
        assert len(V[2]) == len(V[1])
        weights = V[2]
    else:
        weights = [1] * max(len(V[1]), len(V[0]))
    arr = np.zeros(shape=(len(V[0]), len(V[0])), dtype=int)
    for i, (x, y) in enumerate(V[1]):
        arr[x, y] = weights[i]
        if not directed:
            arr[y, x] = weights[i]
    return arr


def get_all_paths(neighbour, start, end):
    all_paths = []

    def inner():
        path = []
        path.append(start)
        dfs(neighbour, start, path)
        return all_paths

    def dfs(neighbour: np.ndarray, src: int, path: list):
        if src == end:
            all_paths.append(deepcopy(path))
        else:
            for adjnode in links_to(neighbour, src):
                path.append(adjnode)
                dfs(neighbour, adjnode, path)
                path.pop()

    return inner()





def pair_nodes(iterable):# ('ABCDEFG') will be AB BC CD DE EF FG

    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)





def split_new(neighbour):
    edges = []
    weights = []
    for x, row in enumerate((neighbour < 0) * neighbour):
        for y, value in enumerate(row):
            if value:
                edges.append((x, y))
                weights.append(abs(value))
    return edges, weights


def edmondskarp(neighbour, start, end, g, draw=False, draw_args=None):
    fmax = 0
    cp = 0  # przepustowosc residualna
    CFP = np.full(len(neighbour), np.infty)  # tablica przepustowosci residualnych
    F = np.zeros_like(neighbour)  # macierz przeplywow

    while True:
        P = np.full(len(neighbour), -1) #macierz z "-1"
        P[start] = -2
        CFP[start] = np.infty
        Q = deque([start])
        esc = False
        while Q:
            x = Q.pop()
            for y in range(len(neighbour)):
                cp = neighbour[x, y] - F[x, y]
                if cp and P[y] == -1:
                    P[y] = x
                    CFP[y] = min(CFP[x], cp)
                    if y == end:
                        fmax += CFP[end]
                        i = y
                        while i != start:
                            x = P[i]
                            F[x, i] += CFP[end]
                            F[i, x] -= CFP[end]
                            i = x
                            if draw:
                                plt.figure(figsize=(12, 6))
                                g.draw(split_new(F), draw_args=draw_args)
                        esc = True
                        break
                    Q.appendleft(y)
            if esc:
                break
        if not esc:
            break

    return F, fmax

g = Graph.from_file("graph1.flow", True)
g.pos = {0: (0, 0), 1: (15, 10), 2: (25, 10), 3: (20, 0), 4: (15, -10), 5: (25, -10), 6: (40, 0)}
g.draw()

f, fmax = edmondskarp(g.neighbour, 0, 6, g, True)

print(f,fmax)
