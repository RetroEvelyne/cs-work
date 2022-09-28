from random import randint, choice
import string


def challenge2():
    continuegame = True
    while continuegame:
        valid = False
        a, b, guesses = 0, 0, 0
        while not valid:
            try:
                a, b = input("input two numbers:\n> ").split()
                a, b = int(a), int(b)
                valid = True
            except:
                print("input valid numbers")
        valid = False
        compnum = randint(a, b)
        while not valid:
            try:
                usernum = int(input(f"Enter guess between {a} and {b}:\n> "))
                if usernum >= a or usernum <= b:
                    if compnum == usernum:
                        valid = True
                        cong = input(f"Congratulations User, {usernum} was the correct number.\n"
                                     f"Would you like to try again? (y/n)\n")
                        if cong.lower() == "y" or cong.lower() == "yes":
                            pass
                        elif cong.lower() == "n" or cong.lower() == "no":
                            continuegame = False
                    elif compnum > usernum:
                        print(f"higher than {usernum}")
                        guesses += 1
                    elif compnum < usernum:
                        print(f"lower than {usernum}")
                        guesses += 1
                    else:
                        pass
                else:
                    print("input valid number")
            except:
                print("input valid number")


def challenge4():
    numplate = []
    for i in range(2):
        numplate.append(choice(string.ascii_uppercase))
    for i in range(5):
        numplate.append(randint(0, 9))
    numplate.insert(4, " ")


if __name__ == "__main__":
    cnum = int(input("what challenge?\n> "))
    match cnum:
        case 1:
            pass
        case 2:
            challenge2()
        case 3:
            pass
        case 4:
            challenge4()
        case other:
            pass
