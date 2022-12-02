from CustomDataTypes import Stack, Colors as c


class Game:
    def __init__(self):
        self.game_board = [[{"symbol": "✪", "color": "none"} for _ in range(7)] for _ in range(6)]
        self.turn = 1

    def play(self):
        while True:
            self.print_game_board()
            print(f"Turn: {self.turn}")
            self.turn += 1
            break

    def print_game_board(self):
        print(f"{c.purple}     1     2     3     4     5     6     7")
        print(f"{c.blue} --------------------------------{c.norm}")
        for row in self.game_board:
            for col in row:
                match col["color"]:
                    case "red":
                        print(f" {c.blue}| {c.red}{col['symbol']}{c.norm}", end="")
                    case "yellow":
                        print(f" {c.blue}| {c.yellow}{col['symbol']}{c.norm}", end="")
                    case _:
                        print(f" {c.blue}| {c.norm}{col['symbol']}", end="")
            print(f"{c.blue} |{c.norm}")
            print(f"{c.blue} --------------------------------{c.norm}")


if __name__ == "__main__":
    game = Game()
    game.play()
