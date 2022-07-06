import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import copy

VV = [1, 2, 3, 4, 5, 6]
WW = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (3, 5), (5,6)]
Vx = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5}
Vy = {1:0, 2:1, 3:0, 4:-1, 5:0, 6:3}

g = nx.Graph()
gpos = {}
for v in VV:
    g.add_node(v)
    gpos[v] = [Vx[v], Vy[v]]
for v1 in VV:
    for v2 in VV:
        if (v1, v2) in WW:
            label = str(round(np.sqrt(abs(Vx[v1] - Vx[v2])**2+(abs(Vy[v1] - Vy[v2]))**2),2))
            g.add_weighted_edges_from([(v1, v2, label)])



dict_d_v_s = {n: round(np.sqrt(abs(Vx[n[0]] - Vx[n[1]])**2+(abs(Vy[n[0]] - Vy[n[1]]))**2),2) for n in WW}

def disc(v,w,ww = WW,ppath=[]):
    global dict_d_v_s
    path = copy.deepcopy(ppath) #problem łączenia list
    if (v,w) in ww or (w,v) in ww:
        path.append(v)
        path.append(w)
        return path,round(np.sqrt(abs(Vx[v] - Vx[w])**2+(abs(Vy[v] - Vy[w]))**2),2)
    else:
        path.append(v)
        d_v_s = [n for n in ww if v in n]
        connected = [x if x != v else y for x,y in d_v_s]

    ww = [n for n in ww if v not in n]
    min =  10000

    for s in connected: # szukanie minimum
        sub_path,dl = disc(s, w, ww, path)

        if dl:
            if dl < min:
                min = dl
                min_l = s
                min_path = sub_path


    if not d_v_s:
        return path,1000

    for i in WW:
        if min_l in i and v in i:
            if min_l > v:
                return min_path, min + dict_d_v_s[(v,min_l)]
            else:
                return min_path,min + dict_d_v_s[(min_l,v)]


print(disc(1,6))
nx.draw(g, gpos, with_labels=True, node_color='yellow')
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, gpos, edge_labels=labels)
plt.show()

