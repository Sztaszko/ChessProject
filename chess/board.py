from enum import Enum

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
        # self.chessboard = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] for i in range(8)]
        self.chessboard = [[BoardLetters.A, BoardLetters.B, BoardLetters.C, BoardLetters.D, BoardLetters.E, BoardLetters.F, BoardLetters.G, BoardLetters.H] for i in range(8)]
    
    def move_piece(self, start_pos, end_pos):
        pass