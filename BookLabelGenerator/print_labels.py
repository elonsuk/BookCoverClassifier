import json

FILE_NAME = 'labels.json'
with open(FILE_NAME, 'r+') as file:
    data = json.load(file)
    for key in data:
        print(f'{key}: {data[key]}')