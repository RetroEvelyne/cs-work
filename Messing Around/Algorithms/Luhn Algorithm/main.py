def reverse_payload(payload: int) -> int:
    ...


def main():
    number = input("Enter a valid number that works with the Luhn algorithm\n > ")
    checkdigit = int(number[-1])
    payload = int(number[:-1])



if __name__ == "__main__":
    main()
