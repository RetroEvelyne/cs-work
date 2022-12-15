class Colors:
    black = "\033[0;30m"
    dark_gray = "\033[1;30m"
    blue = "\033[0;34m"
    light_blue = "\033[1;34m"
    green = "\033[0;32m"
    light_green = "\033[1;32m"
    cyan = "\033[0;36m"
    light_cyan = "\033[1;36m"
    red = "\033[0;31m"
    light_red = "\033[1;31m"
    purple = "\033[0;35m"
    light_purple = "\033[1;35m"
    brown = "\033[0;33m"
    yellow = "\033[1;33m"
    light_gray = "\033[0;37m"
    white = "\033[1;37m"
    norm = "\033[0m"


class Board:
    BOARD = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]

    def __init__(self):
        self.board = self.piece_setup(Board.BOARD)

    @staticmethod
    def piece_setup(board: list) -> list:
        board[0][0] = Pieces.Rook("white")
        board[0][1] = Pieces.Knight("white")
        board[0][2] = Pieces.Bishop("white")
        board[0][3] = Pieces.Queen("white")
        board[0][4] = Pieces.King("white")
        board[0][5] = Pieces.Bishop("white")
        board[0][6] = Pieces.Knight("white")
        board[0][7] = Pieces.Rook("white")
        for i in range(8):
            board[1][i] = Pieces.Pawn("white")
        for i in range(8):
            board[6][i] = Pieces.Pawn("black")
        board[7][0] = Pieces.Rook("black")
        board[7][1] = Pieces.Knight("black")
        board[7][2] = Pieces.Bishop("black")
        board[7][3] = Pieces.Queen("black")
        board[7][4] = Pieces.King("black")
        board[7][5] = Pieces.Bishop("black")
        board[7][6] = Pieces.Knight("black")
        board[7][7] = Pieces.Rook("black")
        return board


class Pieces:
    class Rook:
        def __init__(self, color: str):
            self.color = color
            self.name = "Rook"
            self.symbol = "R" if color == "white" else "r"
            self.moves = (0, "horizontal", "vertical")

    class Knight:
        def __init__(self, color: str):
            self.color = color
            self.name = "Knight"
            self.symbol = "N" if color == "white" else "n"
            self.moves = (0, "L")

    class Bishop:
        def __init__(self, color: str):
            self.color = color
            self.name = "Bishop"
            self.symbol = "B" if color == "white" else "b"
            self.moves = (0, "diagonal")

    class Queen:
        def __init__(self, color: str):
            self.color = color
            self.name = "Queen"
            self.symbol = "Q" if color == "white" else "q"
            self.moves = (0, "horizontal", "vertical", "diagonal")

    class King:
        def __init__(self, color: str):
            self.color = color
            self.name = "King"
            self.symbol = "K" if color == "white" else "k"
            self.moves = (1, "horizontal", "vertical", "diagonal")

    class Pawn:
        def __init__(self, color: str):
            self.color = color
            self.name = "Pawn"
            self.symbol = "P" if color == "white" else "p"
            self.first_move = True
            self.moves = (2, "vertical") if self.first_move else (1, "vertical")


class Game:
    def __init__(self):
        self.board: Board = Board()
        self.turn: str = "white"
        self.game_over: bool = False
        self.winner = None

    def game_loop(self):
        while not self.game_over:
            self.display_board()
            self.get_move()
            self.check_for_checkmate()
            print(self.board.board)
            self.turn = "white" if self.turn == "black" else "black"

    def display_board(self):
        ranks = ["8", "7", "6", "5", "4", "3", "2", "1"]
        print(f"{Colors.light_purple}  a b c d e f g h{Colors.norm}")
        for row in self.board.board:
            print(f"{Colors.light_purple}{ranks.pop(0)}{Colors.norm}", end=" ")
            for piece in row:
                try:
                    if piece.color == "white":
                        print(f"{Colors.white}{piece.symbol}{Colors.norm}", end=" ")
                    else:
                        print(f"{Colors.black}{piece.symbol}{Colors.norm}", end=" ")
                except AttributeError:
                    print(" ", end="")
            print()

    def get_move(self):
        move = input(f"{self.turn.title()}'s move (a1-a2): ")
        if move == "exit":
            self.game_over = True
        else:
            if self.validate_move(move):
                self.make_move(move)

    @staticmethod
    def translate_letters(letter: str) -> int:
        match letter:
            case "a":
                return 0
            case "b":
                return 1
            case "c":
                return 2
            case "d":
                return 3
            case "e":
                return 4
            case "f":
                return 5
            case "g":
                return 6
            case "h":
                return 7
            case _:
                return -1

    def validate_move(self, move: str) -> bool:
        # If the move command is not in the right format, return False
        if len(move) != 5:
            return False
        if move[2] != "-" or move[0] not in "abcdefgh" or move[3] not in "abcdefgh" \
                or move[1] not in "12345678" or move[4] not in "12345678":
            return False
        # If the move command has no effect, return False
        if move[0] == move[3] and move[1] == move[4]:
            return False

        # If the target piece is taken up by a piece of the same color, the move is invalid
        if self.board.board[self.translate_letters(move[3])][int(move[4]) - 1] in \
                [Pieces.Rook, Pieces.Knight, Pieces.Bishop, Pieces.Queen, Pieces.King, Pieces.Pawn]:
            if self.board.board[self.translate_letters(move[3])][int(move[4]) - 1].color == self.turn:
                return False

        if move[0] == move[3] and move[1] != move[4]:
            if "vertical" in self.board.board[self.translate_letters(move[0])][int(move[1]) - 1].moves:
                if int(move[1]) < int(move[4]):
                    amount = int(move[4]) - int(move[1])
                    if amount < self.board.board[self.translate_letters(move[0])][int(move[1]) - 1].moves[0] or \
                            self.board.board[self.translate_letters(move[0])][int(move[1]) - 1].moves[0] == 0:
                        return True

        if move[1] == move[4] and move[0] != move[3]:
            if "horizontal" in self.board.board[self.translate_letters(move[0])][int(move[1]) - 1].moves:
                if self.translate_letters(move[0]) < self.translate_letters(move[3]):
                    amount = self.translate_letters(move[3]) - self.translate_letters(move[0])
                    if amount < self.board.board[self.translate_letters(move[0])][int(move[1]) - 1].moves[0] or \
                            self.board.board[self.translate_letters(move[0])][int(move[1]) - 1].moves[0] == 0:
                        return True

        if move[0] != move[3] and move[1] != move[4]:
            if "diagonal" in self.board.board[self.translate_letters(move[0])][int(move[1]) - 1].moves:
                if abs(self.translate_letters(move[0]) - self.translate_letters(move[3])) == \
                        abs(int(move[1]) - int(move[4])):
                    amount = abs(int(move[1]) - int(move[4]))
                    if amount < self.board.board[self.translate_letters(move[0])][int(move[1]) - 1].moves[0] or \
                            self.board.board[self.translate_letters(move[0])][int(move[1]) - 1].moves[0] == 0:
                        return True
            elif "L" in self.board.board[self.translate_letters(move[0])][int(move[1]) - 1].moves:
                if abs(self.translate_letters(move[0]) - self.translate_letters(move[3])) == 1 and \
                        abs(int(move[1]) - int(move[4])) == 2:
                    return True
                elif abs(self.translate_letters(move[0]) - self.translate_letters(move[3])) == 2 and \
                        abs(int(move[1]) - int(move[4])) == 1:
                    return True

    def make_move(self, move: str):
        match self.board.board[self.translate_letters(move[0])][int(move[1]) - 1]:
            case Pieces.Rook:
                self.board.board[self.translate_letters(move[3])][int(move[4]) - 1] = Pieces.Rook(self.turn)
            case Pieces.Knight:
                self.board.board[self.translate_letters(move[3])][int(move[4]) - 1] = Pieces.Knight(self.turn)
            case Pieces.Bishop:
                self.board.board[self.translate_letters(move[3])][int(move[4]) - 1] = Pieces.Bishop(self.turn)
            case Pieces.Queen:
                self.board.board[self.translate_letters(move[3])][int(move[4]) - 1] = Pieces.Queen(self.turn)
            case Pieces.King:
                self.board.board[self.translate_letters(move[3])][int(move[4]) - 1] = Pieces.King(self.turn)
            case Pieces.Pawn:
                self.board.board[self.translate_letters(move[3])][int(move[4]) - 1] = Pieces.Pawn(self.turn)
                self.board.board[self.translate_letters(move[3])][int(move[4]) - 1].first_move = False
            case _:
                pass
        #self.board.board[self.translate_letters(move[3])][int(move[4]) - 1] = \
            #self.board.board[self.translate_letters(move[0])][int(move[1]) - 1]
        self.board.board[self.translate_letters(move[0])][int(move[1]) - 1] = None

    def check_for_checkmate(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.game_loop()
