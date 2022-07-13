import json

FILE_NAME = 'labels.json'
with open(FILE_NAME, 'r+') as file:
    data = json.load(file)
    for key in data:
        data[key] = '\n\n'.join(data[key].split('\n\n\n\n'))

    file.seek(0)
    json.dump(data, file, indent=4)
    file.truncate()