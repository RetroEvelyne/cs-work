def reverse():
    ...


def validate_input(user_input: str) -> bool:
    ...
    return valid


def get_input() -> str:
    valid = False
    user_input = ""
    while not valid:
        user_input = input()
        valid = validate_input(user_input)
    return user_input


def main():
    ...


if __name__ == "__main__":
    main()
