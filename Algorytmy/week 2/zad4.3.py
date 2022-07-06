"""
ALFABET:
a, b, c
d(przekreślone a), e(przekreślone b), f(przekreślone c)
model: a(b*x)a(c*x)a
pozycja głowicy == poz
"""
poz = 0


def poz_check(p, array):
    if p < 0:
        raise AssertionError('left')
    elif p > len(array):
        raise AssertionError('right')


def security(p, array):
    a = 0
    if p < 0:
        a = 1
    elif p > len(array):
        a = -1
    return a


class StateMachine:

    def __init__(self, states):
        print(self.q0(states, poz))

    def q0(self, states, poz):
        poz = 0
        poz_check(poz, states)
        print('q0', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'a':
            poz += 1
            poz += security(poz, states)
            return self.q1(states, poz)
        elif states[poz] in ('b', 'c', 'e', 'f', 'd'):
            return 'not accepted'

    def q1(self, states, poz):
        poz_check(poz, states)
        print('q1', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'c':
            return 'not accepted'
        elif states[poz] == 'b':
            states[poz] = 'e'
            poz += 1
            poz += security(poz, states)
            return self.q3(states, poz)
        elif states[poz] == 'a':
            poz += 1
            poz += security(poz, states)
            return self.q2(states, poz)

    def q2(self, states, poz):
        poz_check(poz, states)
        print('q2', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak:{states[poz]} ')
        if states[poz] == 'c':
            return 'not accepted'
        elif states[poz] == 'f':
            poz += 1
            poz += security(poz, states)
            return self.q2(states, poz)
        elif states[poz] == 'a':
            poz -= 1
            poz += security(poz, states)
            return self.q6(states, poz)

    def q6(self, states, poz):
        poz_check(poz, states)
        print('q6', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak:{states[poz]} ')
        poz += security(poz, states)
        if states[poz] in ( 'b', 'c'):
            return 'not accepted'
        elif states[poz] in ('a', 'd', 'e', 'f'):
            return 'accepted'

    def q3(self, states, poz):
        poz_check(poz, states)
        print('q3', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'b':
            poz += 1
            poz += security(poz, states)
            return self.q3(states, poz)
        elif states[poz] == 'a':
            poz += 1
            poz += security(poz, states)
            return self.q4(states, poz)

    def q4(self, states, poz):
        poz_check(poz, states)
        print('q4', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] == 'f':
            poz += 1
            poz += security(poz, states)
            return self.q4(states, poz)
        elif states[poz] == 'a':
            return 'not accepted'
        elif states[poz] == 'c':
            states[poz] = 'f'
            poz -= 1
            poz += security(poz, states)
            return self.q5(states, poz)

    def q5(self, states, poz):
        poz_check(poz, states)
        print('q5', states, f'pozycja glowicy: {poz}', f'aktualnie przeptarowany znak: {states[poz]}')
        if states[poz] in ('a', 'b', 'f'):
            poz -= 1
            poz += security(poz, states)
            return self.q5(states, poz)
        elif states[poz] == 'e':
            poz += 1
            poz += security(poz, states)
            return self.q1(states, poz)


tasma = 'abbacca'
StateMachine(list(tasma))
