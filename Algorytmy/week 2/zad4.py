"""
ALFABET:
a, b, c
model: a(b*x)a(c*x)a
pozycja głowicy == poz
"""



def poz_check(p, array):
    if p < 0:
        raise AssertionError("(pozycja glowicy max w lewo)")
    if p > len(array):
        raise AssertionError("(pozycja glowicy max w prawo)")


class StateMachine:

    def __init__(self, states):
        print(self.q0(states))

    def q0(self, states):
        poz = 0
        b_count = 0
        c_count = 0
        poz_check(poz, states)
        print('q0', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'a':
            poz += 1
            return self.q1(states, poz, b_count, c_count)
        elif states[poz] == 'b' or states[poz] == 'c':
            poz += 1
            return "not accepted"
        else:
            raise AssertionError("Algorytm zapetla sie!")

    def q1(self, states, poz, b_count, c_count):
        poz_check(poz, states)
        print('q1', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'b':
            poz += 1
            b_count += 1
            return self.q1(states, poz, b_count, c_count)
        elif states[poz] == 'a':
            poz += 1
            return self.q2(states, poz, b_count, c_count)
        elif states[poz] == 'c':
            return 'not accepted'
        else:
            raise AssertionError("Algorytm zapetla sie!")

    def q2(self, states, poz, b_count, c_count):
        poz_check(poz, states)
        print('q2', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'c':
            poz += 1
            c_count += 1
            return self.q2(states, poz, b_count, c_count)
        elif states[poz] == 'a':
            poz -= 1
            return 'accepted'
        elif states[poz] == 'b':
            return 'not accepted'
        else:
            raise AssertionError("Algorytm zapetla sie!")


tasma = 'abbbaccaca'
StateMachine(list(tasma))
