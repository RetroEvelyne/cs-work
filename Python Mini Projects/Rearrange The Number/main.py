def reversestring(user_input: str) -> str:
    final = user_input[::-1]
    return final


def validate_input(user_input: str) -> bool:
    try:
        int(user_input)
        valid = True
    except ValueError:
        valid = False
    return valid


def get_input() -> str:
    valid = False
    user_input = ""
    while not valid:
        user_input = input("| Please Input Your Number.\n"
                           "| This Will Reverse It And Find The Difference Between The Two:\n"
                           "╰-> ")
        valid = validate_input(user_input)
    return user_input


def main():
    user_input = get_input()
    reverse = reversestring(user_input)
    final = int(user_input) - int(reverse)
    print(final)


if __name__ == "__main__":
    main()
