import json

with open('data\parser.json') as file:
    data_auto = json.load(file)

c = input('Введите авто: ')

for i in data_auto:
    d = i.values()
    print(d)
