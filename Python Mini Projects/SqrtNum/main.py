def main(number):
    guess = number / 2
    while True:
        guess = (guess + (number / guess)) / 2
        error = abs(number - (guess ** 2))
        if error <= 0.000000000000001:
            break
    return guess


if __name__ == "__main__":
    square_root = main(646238743)
    print(square_root)
