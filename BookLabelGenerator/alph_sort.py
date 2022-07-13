import json

FILE_NAME = 'labels.json'
new_dict = {}
with open(FILE_NAME, 'r+') as file:
    data = json.load(file)
    descriptions = sorted(data.values(), reverse=False)
    for i in range(len(descriptions)):
        new_dict[i] = descriptions[i]

    file.seek(0)
    json.dump(new_dict, file, indent=4)
    file.truncate()