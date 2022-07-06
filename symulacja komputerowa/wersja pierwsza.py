import simpy
import random
import statistics
import numpy as np
import datetime

patients = {}
timeline = []

service_time = lambda: random.randint(60 * 8, 60 * 20)
# service_time = lambda : 4000
# arrival = lambda : random.randint(500, 1000)
arrival = lambda: np.random.poisson(24 * 3600 / 300)

# arrival = lambda : 3000
priority_var = lambda: np.random.choice([1, 2, 3], p=[0.15, 0.35, 0.5])
patience = [0, 3600, 60 * 240]
multiply = [6, 3, 1]
retribution = 0  # kara
doctors = 3

handled = []


def handle_patient(patient_num):
    global retribution

    handled.append(patient_num)
    service = env.now
    patients[patient_num]['service'] = service
    timeline.append(f'{datetime.timedelta(seconds=service)}: {patient_num}, service')
    patients[patient_num]['waited'] = patients[patient_num]['service'] - patients[patient_num]['arrival']
    how_much_point = patients[patient_num]['waited'] - patients[patient_num]['patience'] if patients[patient_num][
                                                                                                'waited'] > \
                                                                                            patients[patient_num][
                                                                                                'patience'] else 0

    retribution += how_much_point * multiply[patients[str(patient_num)]['priority'] - 1]
    yield env.timeout(service_time())


def go_to_hospital(env, patient_num):
    arrival_time = env.now
    priority = patients[patient_num]['priority']
    patients[patient_num]['arrival'] = arrival_time
    timeline.append(f'{datetime.timedelta(seconds=arrival_time)}: {patient_num}, prior {priority} arrival')
    with doctor_all.request(priority=priority) as request:
        yield request
        yield env.process(handle_patient(patient_num))

    departure_time = env.now
    patients[patient_num]['departure'] = departure_time
    timeline.append(f'{datetime.timedelta(seconds=departure_time)}: {patient_num}, prior {priority} departure')


def run_hospital(env):
    patient_num = 0

    # for _ in range(6):
    #   patients[str(patient_num)] = {}
    #   patients[str(patient_num)]['priority'] = random.randint(1, 3)
    #   env.process(go_to_hospital(env, patient_num=str(patient_num)))
    #   patient_num += 1

    while True:
        priority = priority_var()
        patients[str(patient_num)] = {}
        patients[str(patient_num)]['priority'] = priority
        patients[str(patient_num)]['patience'] = patience[priority - 1]
        env.process(go_to_hospital(env, patient_num=str(patient_num)))
        yield env.timeout(arrival())
        patient_num += 1


# random.seed(42)

env = simpy.Environment()
doctor_all = simpy.PriorityResource(env, 3)
env.process(run_hospital(env))
env.run(until=36000)

print('----------PATIENTS--------')
for i in patients.items():
    print(i)

print()
print('----------ORDER-----------')
print(handled)
print()

print('-----------TIMELINE----------')
for i in timeline:
    print(i)

print(retribution)




