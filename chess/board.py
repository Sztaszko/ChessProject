from enum import Enum
from .pieces import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class BoardLetters(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8

class Board():
    """The Board class represents chessboard. It is responsible pieces arrangement.
    """
    def __init__(self) -> None:
        #self.chessboard = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] for i in range(8)]
        # self.chessboard = [[BoardLetters.A, BoardLetters.B, BoardLetters.C, BoardLetters.D, BoardLetters.E, BoardLetters.F, BoardLetters.G, BoardLetters.H] for i in range(8)]
        self.chessboard = [[Piece("none")]*8 for _ in range(8)] #8x8 chessboard with Piece as empty squares
        
    def initialize_pieces(self) -> None: #initialize pieces in starting positions
        self.chessboard[0] = [Rook('white'), Knight('white'), Bishop('white'), Queen('white'), King('white'), Bishop('white'), Knight('white'), Rook('white')]
        self.chessboard[1] = [Pawn('white')] * 8

        self.chessboard[6] = [Pawn('black')] * 8
        self.chessboard[7] = [Rook('black'), Knight('black'), Bishop('black'), King('black'), Queen('black'), Bishop('black'), Knight('black'), Rook('black')]

    def print_board(self) -> None:
        for row in reversed(self.chessboard):
            print(" ".join(piece.symbol() for piece in row))
    
    def move_piece(self, start_pos, end_pos):
        pass