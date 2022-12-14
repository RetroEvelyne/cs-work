class Board:
    BOARD = [
        [("a", 1), ("a", 2), ("a", 3), ("a", 4), ("a", 5), ("a", 6), ("a", 7), ("a", 8)],
        [("b", 1), ("b", 2), ("b", 3), ("b", 4), ("b", 5), ("b", 6), ("b", 7), ("b", 8)],
        [("c", 1), ("c", 2), ("c", 3), ("c", 4), ("c", 5), ("c", 6), ("c", 7), ("c", 8)],
        [("d", 1), ("d", 2), ("d", 3), ("d", 4), ("d", 5), ("d", 6), ("d", 7), ("d", 8)],
        [("e", 1), ("e", 2), ("e", 3), ("e", 4), ("e", 5), ("e", 6), ("e", 7), ("e", 8)],
        [("f", 1), ("f", 2), ("f", 3), ("f", 4), ("f", 5), ("f", 6), ("f", 7), ("f", 8)],
        [("g", 1), ("g", 2), ("g", 3), ("g", 4), ("g", 5), ("g", 6), ("g", 7), ("g", 8)],
        [("h", 1), ("h", 2), ("h", 3), ("h", 4), ("h", 5), ("h", 6), ("h", 7), ("h", 8)]
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
            self.moves = ("horizontal", "vertical", 0)

    class Knight:
        def __init__(self, color: str):
            self.color = color
            self.name = "Knight"
            self.symbol = "N" if color == "white" else "n"
            self.moves = ("L", 0)

    class Bishop:
        def __init__(self, color: str):
            self.color = color
            self.name = "Bishop"
            self.symbol = "B" if color == "white" else "b"
            self.moves = ("diagonal", 0)

    class Queen:
        def __init__(self, color: str):
            self.color = color
            self.name = "Queen"
            self.symbol = "Q" if color == "white" else "q"
            self.moves = ("horizontal", "vertical", "diagonal", 0)

    class King:
        def __init__(self, color: str):
            self.color = color
            self.name = "King"
            self.symbol = "K" if color == "white" else "k"
            self.moves = ("horizontal", "vertical", "diagonal", 1)

    class Pawn:
        def __init__(self, color: str):
            self.color = color
            self.name = "Pawn"
            self.symbol = "P" if color == "white" else "p"
            self.first_move = True
            self.moves = ("vertical", 2) if self.first_move else ("vertical", 1)

