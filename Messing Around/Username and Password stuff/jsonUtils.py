import json


def openfile(file: str) -> dict:
    with open(file, "r") as f:
        data = json.load(f)
    return data


def writetofile(file: str, data: dict):
    with open(file, "w") as f:
        f.write(json.dumps(data, indent=2))
