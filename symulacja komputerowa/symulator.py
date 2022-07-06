import simpy
import random
import statistics

patients = {}

# service_time = lambda : random.randint(1200, 3600)
service_time = lambda: 4000
# arrival = lambda : random.randint(1000, 2000)
arrival = lambda: 3000
doctors = 3

handled = []


def handle_patient(patient_num):
    handled.append(patient_num)
    patients[patient_num]['service'] = env.now
    patients[patient_num]['waited'] = patients[patient_num]['service'] - patients[patient_num]['arrival']
    yield env.timeout(service_time())


def go_to_hospital(env, patient_num):
    arrival_time = env.now
    priority = patients[patient_num]['priority']
    patients[patient_num]['arrival'] = arrival_time
    with doctor.request(priority=priority, preempt=True) as request:
        yield request
        yield env.process(handle_patient(patient_num))

    departure_time = env.now

    patients[patient_num]['departure'] = departure_time


def run_hospital(env):
    patient_num = 0

    for _ in range(6):
        patients[str(patient_num)] = {}
        patients[str(patient_num)]['priority'] = random.randint(1, 3)
        env.process(go_to_hospital(env, patient_num=str(patient_num)))
        patient_num += 1

    while True:
        patients[str(patient_num)] = {}
        patients[str(patient_num)]['priority'] = random.randint(1, 10)
        yield env.timeout(arrival())
        env.process(go_to_hospital(env, patient_num=str(patient_num)))
        patient_num += 1


random.seed(42)

env = simpy.Environment()
doctor = simpy.PriorityResource(env, 1)
env.process(run_hospital(env))
env.run(until=36000)

for i in patients.items():
    print(i)

print(handled)




