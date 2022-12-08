from CustomDataTypes import Colors as C
from os import system


class Game:
    COLUMNS = ["A", "B", "C", "D", "E", "F", "G"]

    def __init__(self):
        self.game_board = [[{"symbol": "*", "color": "None"} for _ in range(7)] for _ in range(6)]
        self.turn = "red"

    def play(self):
        while True:
            self.print_game_board()
            print(f"Turn: {self.turn}")
            match self.turn:
                case "red":
                    column = self.ask_for_column()
                    self.drop_piece(column, "red")
                    self.turn = "yellow"
                case "yellow":
                    column = self.ask_for_column()
                    self.drop_piece(column, "yellow")
                    self.turn = "red"
            self.clear_screen()
            if self.check_for_win():
                self.print_game_board()
                if self.turn == "red":
                    print(f"{C.yellow}Yellow{C.norm} wins!")
                else:
                    print(f"{C.red}Red{C.norm} wins!")
                break

    def ask_for_column(self):
        while True:
            print("\rColumn: ", end="")
            column = input()
            if column.upper() in Game.COLUMNS:
                if self.game_board[0][Game.COLUMNS.index(column.upper())]["color"] == "None":
                    break
            print("\033[A                             \033[A")
        return Game.COLUMNS.index(column.upper())

    def print_game_board(self):
        print(f"{C.blue} ----------------------------{C.norm}")
        print(f"{C.blue} | {C.norm}A {C.blue}| {C.norm}B {C.blue}| {C.norm}C {C.blue}| {C.norm}D {C.blue}| {C.norm}E "
              f"{C.blue}| {C.norm}F {C.blue}| {C.norm}G {C.blue}|{C.norm}")
        print(f"{C.blue} ----------------------------{C.norm}")
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
            print(f"{C.blue} ----------------------------{C.norm}")

    def drop_piece(self, column, color):
        for row in range(5, -1, -1):
            if self.game_board[row][column]["color"] == "None":
                self.game_board[row][column]["color"] = color
                break

    def check_for_win(self):
        # Check for vertical win
        for col in range(7):
            count = 1
            for i in range(5):
                if self.game_board[i][col]["color"] == self.game_board[i+1][col]["color"] and \
                   self.game_board[i][col]["color"] != "None":
                    count += 1
                else:
                    count = 1
            if count == 4:
                return True

        # Check for horizontal win
        for row in range(6):
            count = 1
            for i in range(6):
                if self.game_board[row][i]["color"] == self.game_board[row][i+1]["color"] and \
                   self.game_board[row][i]["color"] != "None":
                    count += 1
                else:
                    count = 1
            if count == 4:
                return True

        # Check for diagonal win in positive slope
        for col in range(4):
            count = 1
            for row in range(6):
                try:
                    if self.game_board[row][col]["color"] == self.game_board[row+1][col+1]["color"] and \
                       self.game_board[row][col]["color"] != "None":
                        count += 1
                except IndexError:
                    pass
            if count == 4:
                return True
        for row in range(1, 3):
            count = 1
            for col in range(5):
                try:
                    if self.game_board[row][col]["color"] == self.game_board[row+1][col+1]["color"] and \
                       self.game_board[row][col]["color"] != "None":
                        count += 1
                except IndexError:
                    pass
            if count == 4:
                return True

        # Check for diagonal win in negative slope
        for col in range(4):
            count = 1
            for row in range(5, -1, -1):
                try:
                    if self.game_board[row][col]["color"] == self.game_board[row-1][col+1]["color"] and \
                       self.game_board[row][col]["color"] != "None":
                        count += 1
                except IndexError:
                    pass
            if count == 4:
                return True
        for row in range(5, 2, -1):
            count = 1
            for col in range(5):
                try:
                    if self.game_board[row][col]["color"] == self.game_board[row-1][col+1]["color"] and \
                       self.game_board[row][col]["color"] != "None":
                        count += 1
                except IndexError:
                    pass
            if count == 4:
                return True
        return False

    @staticmethod
    def clear_screen():
        system("cls" if system == "nt" else "clear")


if __name__ == "__main__":
    Game().play()
