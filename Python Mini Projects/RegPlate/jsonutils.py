import json


def read_json_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return


def write_json_file(filename, data):
    try:
        json_data = read_json_file(filename)
        json_data["registration_data"].append(data)
    except FileNotFoundError:
        return
    with open(filename, 'w') as f:
        json.dump(json_data, f, indent=4)

