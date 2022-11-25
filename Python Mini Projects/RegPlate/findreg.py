import jsonutils


def find_reg_from_json(reg) -> tuple:
    data = jsonutils.read_json_file("regdata.json")
    for item in data:
        if item["reg"] == reg:
            return item["name"], item["phone"]
