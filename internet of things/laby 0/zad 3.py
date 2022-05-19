import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = r.json()
temp_list = []
for key, value in data.items():
    temp_list.append([key, value])

new_json = {}
temp_list.sort()
for element in temp_list:
    new_json[element[0]] = list(sorted(element[1])) if type(element[1]) is list else element[1]

with open('json_file.json', 'w') as file:
    json.dump(new_json, file)
