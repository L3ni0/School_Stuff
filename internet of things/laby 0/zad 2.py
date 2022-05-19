import json


def write_json_file(name, to_dump):
    with open(name, 'w') as file:
        json.dump(to_dump, file)


def read_json_file(name):
    with open(name, 'r') as file:
        data = json.load(file)
        print(data)

read_json_file('data.json')