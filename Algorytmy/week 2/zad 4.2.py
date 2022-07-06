"""
ALFABET:
a, b, c
model: a(b*x)a(c*x)a
pozycja głowicy == poz
"""
poz = 0


def poz_check(p, array):
    if p < 0:
        raise AssertionError('accepted')
    if p > len(array):
        raise AssertionError('accepted')


class StateMachine:

    def __init__(self, states):
        print(self.q0(states, poz))

    def q0(self, states, poz):
        poz = 0
        poz_check(poz, states)
        print('q0', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'a':
            poz += 1
            return self.q1(states, poz)
        else:
            raise AssertionError("not accepted")

    def q1(self, states, poz):
        poz_check(poz, states)
        print('q1', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'b':
            return self.q2(states, poz)
        elif states[poz] == 'a' or states[poz] == 'c':
            return 'not accepted'
        else:
            raise AssertionError("not accepted")

    def q2(self, states, poz):
        poz_check(poz, states)
        print('q2', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'b':
            poz += 1
            return self.q2(states, poz)
        elif states[poz] == 'a':
            poz -= 1
            return self.q3(states, poz)
        else:
            raise AssertionError("not accepted")

    def q3(self, states, poz):
        poz_check(poz, states)
        print('q3', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'a':
            poz -= 1
            return self.q3(states, poz)
        elif states[poz] == 'b':
            states[poz] = 'a'
            poz += 1
            return self.q4(states, poz)
        else:
            raise AssertionError("not accepted")

    def q4(self, states, poz):
        poz_check(poz, states)
        print('q4', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'a':
            poz += 1
            return self.q4(states, poz)
        elif states[poz] == 'c':
            states[poz] = 'a'
            poz -= 1
            return self.q5(states, poz)
        else:
            raise AssertionError("not accepted")

    def q5(self, states, poz):
        poz_check(poz, states)
        print('q5', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'a':
            poz -= 1
            return self.q5(states, poz)
        elif states[poz] == 'b':
            states[poz] = 'a'
            poz -= 1
            return self.q2(states, poz)
        elif states[poz] == 'c':
            return 'accept'
        else:
            raise AssertionError("not accepted")


tasma = 'abaca'
StateMachine(list(tasma))
