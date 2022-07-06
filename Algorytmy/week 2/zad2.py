"""
ALFABET:
a, b(przekreślone), c(z kropką), _(symbol pusty)
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
        # self.draw_machine('q0')

        poz = 0
        poz_check(poz, states)
        print('q0', states)
        if states[poz] == '_':
            return "not accepted"

        elif states[poz] == 'a':
            states[poz] = 'c'
            poz += 1
            return self.q1(states[:], poz)

        else:
            raise AssertionError("Algorytm zapetla sie!")

    def q1(self, states, poz):
        poz_check(poz, states)
        print('q1', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'b':
            poz += 1
            return self.q1(states, poz)

        elif states[poz] == '_':
            poz -= 1 if poz != 0 else 0
            return "accepted"

        elif states[poz] == 'a':
            poz += 1
            return self.q2(states, poz)

        else:
            raise AssertionError("Algorytm zapetla sie!")

    def q2(self, states, poz):
        poz_check(poz, states)
        print('q2', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'b':
            poz -= 1 if poz != 0 else 0
            return self.q2(states, poz)
        elif states[poz] == 'c':
            poz -= 1 if poz != 0 else 0
            return self.q3(states, poz)
        else:
            raise AssertionError("Algorytm zapetla sie!")

    def q3(self, states, poz):
        poz_check(poz, states)
        print('q3', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'b':
            poz += 1
            return self.q3(states, poz)
        elif states[poz] == 'a' or states[poz] == 'c':
            poz += 1
            return self.q4(states, poz)
        elif states[poz] == '_':
            poz -= 1 if poz != 0 else 0
            return self.q6(states, poz)
        else:
            raise AssertionError("Algorytm zapetla sie!")

    def q4(self, states, poz):
        poz_check(poz, states)
        print('q4', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == '_':
            poz -= 1 if poz != 0 else 0
            return "not accepted"
        elif states[poz] == 'b':
            poz += 1
            return self.q4(states, poz)
        elif states[poz] == 'a':
            states[poz] = 'b'
            poz += 1
            return self.q5(states, poz)
        else:
            raise AssertionError("Algorytm zapetla sie!")

    def q5(self, states, poz):
        poz_check(poz, states)
        print('q5', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == '_':
            poz -= 1 if poz != 0 else 0
            return "not accepted"
        elif states[poz] == 'b':
            poz += 1
            return self.q5(states, poz)
        elif states[poz] == 'a':
            states[poz] = 'b'
            poz += 1
            return self.q3(states, poz)
        else:
            raise AssertionError("Algorytm zapetla sie!")

    def q6(self, states, poz):
        poz_check(poz, states)
        print('q6', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'a' or states[poz] == 'b':
            poz -= 1 if poz != 0 else 0
            return self.q6(states, poz)
        elif states[poz] == 'c':
            poz += 1
            return self.q1(states, poz)
        else:
            raise AssertionError("Algorytm zapetla sie!")


tasma = 'aaa'
StateMachine(list(tasma))
