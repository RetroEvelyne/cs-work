from CustomDataTypes import Stack, Colors as C
from sys import stdin


class Game:
    COLUMNS = ["A", "B", "C", "D", "E", "F", "G"]

    def __init__(self):
        self.game_board = [[{"symbol": "✪", "color": "None"} for _ in range(7)] for _ in range(6)]
        self.turn = "red"

    def play(self):
        while True:
            self.print_game_board()
            print(f"Turn: {self.turn}")
            match self.turn:
                case "red":
                    while True:
                        print("\033[A\033[J", end="")
                        column = input("Column:")
                        if column.upper() in Game.COLUMNS:
                            break
                    self.turn = "yellow"
                case "yellow":
                    ...
                    self.turn = "red"
            break

    def print_game_board(self):
        print(f"{C.blue} --------------------------------{C.norm}")
        for row in self.game_board:
            for col in row:
                match col["color"]:
                    case "red":
                        print(f" {C.blue}| {C.red}{col['symbol']}{C.norm}", end="")
                    case "yellow":
                        print(f" {C.blue}| {C.yellow}{col['symbol']}{C.norm}", end="")
                    case _:
                        print(f" {C.blue}| {C.norm}{col['symbol']}", end="")
            print(f"{C.blue} |{C.norm}")
            print(f"{C.blue} --------------------------------{C.norm}")


if __name__ == "__main__":
    Game().play()
