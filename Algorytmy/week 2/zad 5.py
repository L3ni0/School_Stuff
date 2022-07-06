import json
import time
from ast import literal_eval


class Turnig:

    def __init__(self, obj):
        self.states = obj['states']
        self.epsilon = obj['epsilon']
        self.gamma = obj['gamma']
        self.sigma = obj['sigma']
        if ((set(self.gamma) & set(self.epsilon)) == set(self.gamma)):
            raise ValueError('gamma should be subset of sigma')

    def run(self, tape):
        tape = list(tape)
        tape = [int(i) if i.isdigit() else i for i in tape]

        point = 0
        state = 'q0'
        while state != 'qr' and state != 'qa':
            new_state, change, move = self.sigma[(state, tape[point])]

            tape[point] = change
            point += -1 if move == 'L' else 1  # moving tape
            if point < 0:
                point = 0
            if point > len(tape):
                tape.append('_')
            state = new_state

            # print(tape)
            tape_s = self.sss(tape)
            print("".join(tape_s[:point]) + f'"{state}"' + "".join(tape_s[point:]))
            time.sleep(1)

        return 'Accepted' if state == 'qa' else 'Not Accepted'
    def sss(self, lista):
        lista = [str(i) for i in lista]
        return lista


with open('turing.json', 'r') as file:
    obj = json.load(file)
    obj['sigma'] = {literal_eval(key): value for key, value in obj['sigma'].items()}
    print(obj['sigma'])

t1 = Turnig(obj)
print(t1.run('21003'))
