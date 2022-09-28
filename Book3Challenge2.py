from random import randint, choice

continuegame = True
while continuegame:
    valid = False
    a, b, guesses = 0, 0, 0
    while not valid:
        try:
            a, b = input("input two numbers:\n> ").split()
            a, b = int(a), int(b)
            valid = True
        except TypeError:
            print("input valid numbers")
    valid = False
    compnum = randint(a, b)
    while not valid:
        try:
            usernum = int(input(f"enter guess between {a} and {b}:\n> "))
            if usernum >= a or usernum <= b:
                if compnum == usernum:
                    valid = True
                    cong = input(f"congratulations user, {usernum} was the correct number.\n"
                                 f"would you like to try again? (y/n)\n")
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
        except TypeError:
            print("input valid number")
