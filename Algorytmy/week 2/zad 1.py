import networkx as nx
import matplotlib.pyplot as plt
import time

class StateMachine():

    def __init__(self,states):
        self.create_graph()
        print(self.q0(states))

    def create_graph(self):
        self.G = nx.DiGraph()
        for i in range(7):
            self.G.add_node(f'q{i}')
        self.G.add_edge('q0','q2')
        self.G.add_edge('q2', 'q1')
        self.G.add_edge('q1', 'q0')

        self.G.add_edge('q1', 'q3')
        self.G.add_edge('q1', 'q4')
        self.G.add_edge('q4', 'q5')
        self.G.add_edge('q4', 'q0')
        self.G.add_edge('q2', 'q6')
        self.G.add_edge('q5', 'q4')
        self.G.add_edge('q6', 'q3')
        self.G.add_edge('q3', 'q3')
        positions = [[0,2],[2,2],[4,2],[6,2],[2,0],[4,0],[6,4]]
        self.pos = {f'q{i}':positions[i] for i in range(7)}
        self.edges_lab= {('q0','q2'):'a,b,c',
                         ('q1','q0'):'b',
                         ('q1','q4'):'a',
                         ('q1','q3'):'c',
                         ('q2','q1'):'a,b',
                         ('q2','q6'):'c',
                         ('q3','q3'):'a,b,c',
                         ('q4','q0'):'a',
                         ('q4','q5'):'b,c',
                         ('q5','q4'):'a,b,c',
                         ('q6','q3'):'a,b,c'}
        nx.draw(self.G,pos=self.pos, with_labels=True, connectionstyle='arc3, rad=0.2', node_size=1000)
        nx.draw_networkx_edge_labels(self.G, pos=self.pos, edge_labels=self.edges_lab, label_pos=0.3)

        plt.show()

    def draw_machine(self,node_name):
        nx.draw(self.G, pos=self.pos, with_labels=True, connectionstyle='arc3, rad=0.2', node_size=1000)
        nx.draw_networkx_edge_labels(self.G, pos=self.pos, edge_labels=self.edges_lab, label_pos=0.3)
        nx.draw_networkx_nodes(self.G, pos=self.pos, nodelist=[node_name], node_size=1000, node_color='red')

        plt.show()

        time.sleep(1)

    def q0(self,states):
        self.draw_machine('q0')

        print('q0', states)
        if not states:
            return ('accepted')

        if states[0] in ('a','b','c'):
            return self.q2(states[1:])

    def q1(self,states):
        self.draw_machine('q1')

        print('q1', states)
        if not states:
            return 'not accepted'

        if states[0] == 'a':
            return  self.q4(states[1:])
        elif states[0] == 'b':
            return  self.q0(states[1:])
        elif states[0] == 'c':
            return  self.q3(states[1:])

    def q2(self,states):
        self.draw_machine('q2')

        print('q2', states)
        if not states:
            return 'not accepted'

        if states[0] in ('a','b'):
            return self.q1(states[1:])
        else:
            return self.q6(states[1:])

    def q3(self,states):
        print('q3', states)

        if not states:
            return 'not accepted'

        if states[0] in ('a','b','c'):
            return  self.q3(states[1:])

    def q4(self,states):
        self.draw_machine('q4')

        print('q4', states)
        if not states:
            return 'accepted'

        if states[0] in ('b','c'):
            return self.q5(states[1:])
        elif states[0] == 'a':
            return self.q0(states[1:])

    def q5(self,states):
        self.draw_machine('q5')

        print('q5', states)
        if not states:
            return 'accepted'

        if states[0] in ('a','b','c'):
            return self.q4(states[1:])

    def q6(self, states):
        self.draw_machine('q6')

        print('q6', states)
        if not states:
            return 'not accepted'

        if states[0] in ('a','b','c'):
            return self.q3(states[1:])

StateMachine('aca')