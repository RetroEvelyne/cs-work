from random import choice, randint, random
from time import sleep

green = "\033[92m"
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
              "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!",
              "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"',
              ",", "<", ".", ">", "/", "?", "`", "~", " "]

while True:
    string = ""
    for i in range(randint(1, 100)):
        string += choice(characters) + (" " * randint(0, 10))
    print(f"{green}{string}")
    sleep(random())
