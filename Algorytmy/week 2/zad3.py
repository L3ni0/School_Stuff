import networkx as nx
import matplotlib.pyplot as plt
import time

class StateMachine():

    def __init__(self,states):
        print(self.q0(states))

    def q0(self,states):

        print('q0', states)
        if not states:
            return ('not accepted')

        if states[0] in ('a'):
            return self.q1(states[1:])
        else:
            return self.q6(states[1:])

    def q1(self,states):

        print('q1', states)
        if not states:
            return 'not accepted'

        if states[0] == 'b':
            return self.q2(states[1:])
        elif states[0] == 'a':
            return self.q3(states[1:])
        else:
            return self.q6(states[1:])

    def q2(self,states):

        print('q2', states)
        if not states:
            return 'not accepted'

        if states[0] == 'a':
            return self.q3(states[1:])
        elif states[0] == 'b':
            return self.q2(states[1:])
        else:
            return self.q6(states[1:])

    def q3(self,states):
        print('q3', states)

        if not states:
            return 'not accepted'

        if states[0] == 'c':
            return self.q4(states[1:])
        elif states[0] == 'a':
            return self.q5(states[1:])
        else:
            return self.q6(states[1:])

    def q4(self,states):
        print('q4', states)

        if not states:
            return 'not accepted'

        if states[0] == 'c':
            return self.q4(states[1:])
        elif states[0] == 'a':
            return self.q5(states[1:])
        else:
            return self.q6(states[1:])

    def q5(self,states):
        print('q5', states)

        if not states:
            return 'accepted'

        if states[0] in ('a','b','c'):
            return self.q6(states[1:])

    def q6(self, states):
        print('q6', states)

        if not states:
            return 'not accepted'

        if states[0] in ('a','b','c'):
            return self.q6(states[1:])

StateMachine('aaca')
