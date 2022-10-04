def numsquaresum(numberlist):
    total = 0
    for i in numberlist:
        total += (i ** 2)
    return total


def checkforhappy(number, checklist):
    while number not in checklist:
        numberstring = str(number)
        numberlist = [int(i) for i in numberstring]
        checklist.append(number)
        number = numsquaresum(numberlist)
        if number == 1:
            return True
        elif number in checklist:
            return False


def main():
    happynums = []
    number = 1
    while len(happynums) < 8:
        checklist = []
        numhappy = checkforhappy(number, checklist)
        if numhappy:
            happynums.append(number)
        number += 1
    print(happynums)


if __name__ == "__main__":
    main()
