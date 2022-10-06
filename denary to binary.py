def dtob():
    num = input("Enter a number\n> ")
    valid = False
    binum = ""
    while not valid:
        try:
            while int(num) > 0:
                n1 = int(num) // 2
                n2 = int(num) % 2
                num = n1
                binum = str(n2) + binum
            valid = True
        except ValueError:
            num = input("Enter a number\n> ")
    print(binum)


def btod():
    pass


if __name__ == "__main__":
    menu = input("Pick Your Options\n1: Denary to Binary\n2: Binary to Denary\n> ")
    menuvalid = False
    while not menuvalid:
        match menu:
            case "1":
                dtob()
            case "2":
                btod()
            case _:
                menu = input("Pick Your Options\n1: Denary to Binary\n2: Binary to Denary\n> ")
