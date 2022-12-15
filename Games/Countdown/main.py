from time import sleep
from math import ceil, floor
from random import sample, randint, choice


def intput(prompt: str) -> int:
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input")
        return intput(prompt)


def splintput(prompt: str) -> tuple[int, int]:
    try:
        input1, input2 = input(prompt).split()
        return int(input1), int(input2)
    except ValueError:
        print("Invalid input")
        return splintput(prompt)


class Colors:
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    blue = "\033[94m"
    purple = "\033[95m"
    cyan = "\033[96m"
    norm = "\033[0m"


class NumbersGame:
    # Constants for the object
    UPPER = [25, 50, 75, 100]
    LOWER = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    OPERATIONS = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    # Initialize The Game
    def __init__(self, lower_amount: int, upper_amount: int):
        self._numbers: list = sample(NumbersGame.LOWER, k=ceil(lower_amount / 2)) \
                              + sample(NumbersGame.LOWER, k=floor(lower_amount / 2)) \
                              + sample(NumbersGame.UPPER, k=upper_amount)  # numbers: List of numbers in play
        # Gets 2 samples from the lower list
        # and 1 from the upper list
        # This simulates the actual cards in countdown
        self._target: int = self.pencil()  # target: The target number to reach, uses PENCIL to generate a number

    # Main Game Loop
    def play(self) -> None:
        # Countdown Numbers Game
        # https://en.wikipedia.org/wiki/Countdown_(game_show)#Numbers_round
        while True:
            print(f"Numbers: {(str(self._numbers)).replace('[', '').replace(']', '')}")
            print(f"Target: {self._target}")
            for i in range(4):
                print("\rYou Have 30 Seconds To Solve The Problem From Now", end="")
                sleep(0.5)
            for i in range(10, -1, -1):
                print(f"\rTime Left: {i}", end="")
                sleep(1)
            print("\nTime's Up!")
            answer: int = intput("What Did You Get?\n> ")
            if answer == self._target:
                print("Correct!\n10 Points!")
            elif (answer - self._target) in range(-10, 11):
                print(f"Close! You Got {abs(answer - self._target)} Points!")
            break

    # My Own Version Of CECIL That Makes Every Round Possible To Solve
    # PENCIL: Python, Easy, Numbers, Calculator, In, Lambda
    def pencil(self) -> int:
        target: int = 0
        # Make sure the target is within the range of 100-999
        while not (100 <= target <= 999):
            # Copy a list of the numbers in play
            numbers_copy: list = self._numbers.copy()
            # Set the target to one of those numbers then remove it from the list
            target = numbers_copy.pop(randint(0, len(numbers_copy) - 1))
            # Choose a random number of operations to do.
            # This is always above 2 to make the round more interesting
            # and always below 5 to make sure it doesn't run out of numbers
            for _ in range(randint(2, 5)):
                # Choose a random operation from the operations dict, this has lambda functions inside to carry out
                # the operation, that item is then removed from the list of numbers available to use
                target = int(round(NumbersGame.OPERATIONS[choice(["+", "-", "*", "/"])]
                                   (target, numbers_copy.pop(randint(0, len(numbers_copy) - 1))), 0))
        return target


if __name__ == "__main__":
    while True:
        lower, higher = splintput("Input how many lower and higher numbers you want: (int int)\n> ")
        if lower + higher == 6 and higher <= 4:
            NumbersGame.play(NumbersGame(int(lower), int(higher)))
            break
