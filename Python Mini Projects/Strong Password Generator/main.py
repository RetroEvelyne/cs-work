# [x] Set the length from 10 to 128
# [x] Set how complicated the characters can be
# [x] Calculate password entropy
# Entropy = Length x Log_2(Number of possible symbols)

# Import math for its log function
# Import random for its choice function
from math import log
from random import choice


def get_entropy(length: int, num_possible: int) -> float:
    entropy = round(length * log(num_possible, 2), 3)
    return entropy


def get_avg_guesses(entropy: float) -> float:
    try:
        avg_guesses = round((2**(entropy - 1)), 3)
        return avg_guesses
    except OverflowError:
        return "TOO BIG OF A NUMBER FOR ME"


def unicode_method(length: int) -> tuple:
    password = ""
    allowed_characters = list(range(161, 1024))
    allowed_characters = allowed_characters + list(range(33, 127))
    for i in range(length):
        char = choice(allowed_characters)
        password += chr(char)
    return password, 957


def ascii_method(length: int) -> tuple:
    password = ""
    allowed_characters = list(range(33, 127))
    allowed_characters.remove(60)
    allowed_characters.remove(62)
    for i in range(length):
        char = choice(allowed_characters)
        password += chr(char)
    return password, 92


def latin_alphabet_method(length: int) -> tuple:
    password = ""
    allowed_characters = list(range(65, 91)) + list(range(97, 123))
    for i in range(length):
        char = choice(allowed_characters)
        password += chr(char)
    return password, 52


def password_generator():
    while True:
        while True:
            length = input("How Long Of A Password Do You Want? (10-128)\n > ")
            try:
                length = int(length)
                if 9 < length < 129:
                    while True:
                        method = (input("What Method Do You Want To Use (latin | ascii | unicode)\n > ")).lower()
                        match method:
                            case "latin":
                                password, num_possible = latin_alphabet_method(length)
                                break
                            case "ascii":
                                password, num_possible = ascii_method(length)
                                break
                            case "unicode":
                                password, num_possible = unicode_method(length)
                                break
                    break
            except (TypeError, ValueError):
                pass
        print(f"Your Password Is:\n"
              f"{password}\n"
              f"And The Entropy Of This Password Is:\n"
              f"{get_entropy(length, num_possible)}\n"
              f"Which Means That It Would Take On Average:\n"
              f"{get_avg_guesses(get_entropy(length, num_possible))}\n"
              f"Guesses To Have A 50% Chance Of Breaking The Password")
        another_password = (input("Would You Like To Generate Another Password? (y/n)\n > ")).lower()
        if another_password == "y" or another_password == "yes":
            pass
        else:
            break


def password_hints():
    another_hint = "y"
    hints = ["Passwords Should Be At Least 12 Characters Long But More Is Better",
             "A Combination Of Different Types Of Characters Is Best",
             "Passwords Shouldn't Be A Word Found In A Dictionary Or Be A Proper Noun",
             "All Your Passwords Should Be Significantly Different",
             "Never Share Your Password With Anyone, Even If You Trust Them",
             "Use A Secure Password Manager",
             "Educate Yourself",
             "Always Enable 2FA"
             ]
    while another_hint == "y" or another_hint == "yes":
        another_hint = (input(f"Your Hint Is:\n"
                              f"{choice(hints)}\n"
                              f"Would You Like Another One? (y/n)\n"
                              f" > ")).lower()
    return


def exit_program():
    exit_sure = (input("Are You Sure? (y/n)\n > ")).lower()
    if exit_sure == "y" or exit_sure == "yes":
        exit(0)
    return


def main():
    while True:
        menu_input = input("(1) Generate A Password\n"
              "(2) Show Password Hints\n"
              "(3) Exit\n"
              " > ")
        match menu_input:
            case "1":
                password_generator()
            case "2":
                password_hints()
            case "3":
                exit_program()


if __name__ == "__main__":
    main()
