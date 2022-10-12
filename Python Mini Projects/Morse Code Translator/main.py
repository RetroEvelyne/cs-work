import json
import colors as c


def load_json(file_name: str) -> dict:
    with open(file_name, "r") as file:
        code_json = json.load(file)
    return code_json


class MorseConverter:
    def __init__(self, file_name: str):
        self.json_file = load_json(file_name)

    def validate_input(self):
        user_input = input(f"")

    def uncoded_to_morse(self):
        ...

    def morse_to_uncoded(self):
        ...


def main(code_json: str):
    choice = input(f"Do You Want To {c.red}Code {c.norm}Or {c.red}Uncode{c.norm}?\n{c.purple}╰-> {c.norm}").lower()
    match choice:
        case "code":
            code = MorseConverter(code_json)
            code.uncoded_to_morse()
        case "uncode":
            uncode = MorseConverter(code_json)
            uncode.morse_to_uncoded()
        case _:
            print(f"{c.red}Uh Oh... That's Not Right.\n{c.norm}")
            main(code_json)


if __name__ == "__main__":
    main("code.json")
