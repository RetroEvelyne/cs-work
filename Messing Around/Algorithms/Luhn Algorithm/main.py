def luhn_algorithm(payload: str) -> bool:
    final = 0
    is_second = False
    for i in payload:
        x = int(i)
        if is_second:
            x *= 2
            if x > 9:
                temp = 0
                for digit in str(x):
                    temp += int(digit)
                x = temp
        is_second = not is_second
        final += x

    if final % 10 == 0:
        return True
    else:
        return False


def main():
    number = input("Enter a valid number that works with the Luhn algorithm\n > ")
    if luhn_algorithm(number):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
