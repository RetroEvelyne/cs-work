import json
import colors as c


def load_json(file_name: str) -> dict:
    with open(file_name, "r") as file:
        code_json = json.load(file)
    return code_json


class MorseConverter:
    def __init__(self, file_name: str):
        self.json_file = load_json(file_name)

    def get_input(self, input_type: str) -> str | list:
        valid = False
        user_input = str
        while not valid:
            if input_type == "decoded":
                user_input = input(f"\nHello, Please Enter Your String!\n{c.purple}╰-> {c.norm}").lower()
                valid = self.validate_input("decoded", user_input)
            if input_type == "coded":
                user_input = input(f"\nHello, Please Enter Your Morse Code!\n"
                                   f"{c.purple}|{c.cyan} - {c.norm}Each Word Seperated By A '/'\n"
                                   f"{c.purple}|{c.cyan} - {c.norm}Each Letter Seperated By A Space\n"
                                   f"{c.purple}╰-> {c.norm}").split()
                valid = self.validate_input("coded", user_input)
        return user_input

    def validate_input(self, input_type: str, user_input: str | list) -> bool:
        if input_type == "decoded":
            for char in user_input:
                if char not in self.json_file:
                    print(f"{c.red}Error, Cannot Translate{c.norm}")
                    return False
            return True

        elif input_type == "coded":
            for char in user_input:
                if char not in self.json_file.values():
                    print(f"{c.red}Error, Cannot Translate{c.norm}")
                    return False
            return True

    def decoded_to_morse(self):
        user_input = self.get_input("decoded")
        final_string = ""
        for char in user_input:
            final_string = final_string + str(self.json_file[char]) + " "
        return final_string

    def morse_to_decoded(self) -> str:
        user_input = self.get_input("coded")
        final_string = ""
        for char in user_input:
            final_string = final_string + str(list(self.json_file.keys())
                                              [list(self.json_file.values()).index(char)])
        return final_string


def main(code_json: str):
    choice = input(f"Do You Want To {c.red}Code {c.norm}Or {c.red}Decode{c.norm}?\n{c.purple}╰-> {c.norm}").lower()
    match choice:
        case "code":
            code = MorseConverter(code_json)
            morse = code.decoded_to_morse()
            print(f"\nYour Coded String Is:\n{c.purple}{morse}")
        case "decode":
            decode = MorseConverter(code_json)
            text = decode.morse_to_decoded()
            print(f"\nYour Decoded String Is:\n{c.purple}{text}")
        case _:
            print(f"{c.red}Uh Oh... That's Not Right.\n{c.norm}")
            main(code_json)


if __name__ == "__main__":
    main("code.json")
