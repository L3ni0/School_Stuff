import json

states = ['q0', 'q1', 'qa', 'qr']
epsilon = [0, 1, 2]
gamma = [0, 1, 2, 3]
sigma = {('q0', 0): ('q0', 2, 'L'),
         ('q0', 1): ('q1', 3, 'R'),
         ('q0', 2): ('q1', 3, 'R'),
         ('q0', 3): ('q1', 3, 'R'),
         ('q1', 0): ('q1', 2, 'R'),
         ('q1', 1): ('q0', 0, 'R'),
         ('q1', 2): ('q0', 2, 'R'),
         ('q1', 3): ('qa', 2, 'L')}

sigma = {str(key): value for key,value in sigma.items()}

dictionary = {'states': states, 'epsilon': epsilon, 'gamma': gamma, 'sigma': sigma}
with open('turing.json','w') as file:
    json.dump(dictionary,file)