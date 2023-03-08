import json


def open_file_json_auto():
    with open('data\parser.json') as file:
        data_auto = json.load(file)
    return data_auto