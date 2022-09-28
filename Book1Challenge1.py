def main():
    valid = False
    price = 0
    diners = 0
    while not valid:
        try:
            diners = int(input("how many Diners?\n> "))
            valid = True
        except:
            print("input valid number")
    valid = False
    while not valid:
        try:
            price = round(float(input("how much is the bill?\n> ")), 2)
            valid = True
        except:
            print("input valid number")
    print("Price Per Customer Is £"+str(round(float(price / diners), 2)))


if __name__ == '__main__':
    main()
