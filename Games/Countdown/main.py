import time
from math import ceil, floor
from random import sample


class NumberGame:
    UPPER = [25, 50, 75, 100]
    LOWER = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self, lower: int, upper: int):
        self.numbers = sample(NumberGame.LOWER, k=ceil(lower/2)) \
                     + sample(NumberGame.LOWER, k=floor(lower/2)) \
                     + sample(NumberGame.UPPER, k=upper)

    def play(self):
        # Countdown Numbers Game

        # Get the target number



if __name__ == "__main__":
    NumberGame.play(NumberGame(4, 4))
