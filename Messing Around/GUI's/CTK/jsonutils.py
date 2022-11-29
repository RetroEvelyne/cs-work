import json


def open_file(file: str) -> dict:
    with open(file, "r") as f:
        data = json.load(f)
    return data


def write_to_file(file: str, data: dict):
    with open(file, "w") as f:
        f.write(json.dumps(data, indent=2))
