from .utils import VALID_COLORS
from .pieces import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class Board():
    """The Board class represents chessboard. It is responsible pieces arrangement.
    """
    def __init__(self) -> None:
        self.chessboard = [[Square('black') if (i+j)%2==0 else Square('white') for i in range(8)] for j in range(8)] #8x8 chessboard with empty squares
        
    def initialize_pieces(self) -> None: #initialize pieces in starting positions
        
        #white pieces
        idx = 0
        for square in self.chessboard[0]:
            if idx == 0 or idx == 7:
                square.set_piece(Rook('white'))
            elif idx == 1 or idx == 6:
                square.set_piece(Knight('white'))
            elif idx == 2 or idx == 5:
                square.set_piece(Bishop('white'))
            elif idx == 3:
                square.set_piece(Queen('white'))
            elif idx == 4:
                square.set_piece(King('white'))
            idx=idx+1

        for square in self.chessboard[1]:
            square.set_piece(Pawn('white'))
        
        #black pieces
        for square in self.chessboard[6]:
            square.set_piece(Pawn('black'))

        idx = 0
        for square in self.chessboard[7]:
            if idx == 0 or idx == 7:
                square.set_piece(Rook('black'))
            elif idx == 1 or idx == 6:
                square.set_piece(Knight('black'))
            elif idx == 2 or idx == 5:
                square.set_piece(Bishop('black'))
            elif idx == 3:
                square.set_piece(Queen('black'))
            elif idx == 4:
                square.set_piece(King('black'))
            idx=idx+1

    def print_board(self) -> None:
        for row in reversed(self.chessboard):
            print(" ".join(square.symbol() for square in row))
    
    def move_piece(self, start_pos, end_pos) -> bool:
        if end_pos[0] > 7 or end_pos[1] > 7 or end_pos[0] < 0 or end_pos[1] < 0:
            print("Position out of range")
            return False
        
        moved_piece : Piece = self.chessboard[start_pos[0]][start_pos[1]].piece

        if moved_piece is None:
            print("No piece on the square")
            return False
        
        if not moved_piece.validate_move(start_pos, end_pos):
            print("Movement not valid")
            return False
        
        if self.chessboard[end_pos[0]][end_pos[1]].piece is not None:
            if self.chessboard[end_pos[0]][end_pos[1]].piece.color != moved_piece.color:
                print("Taking a piece")
            else: 
                print("Can't take your own piece")
                return False
        
        print("Movement valid")
        self.chessboard[end_pos[0]][end_pos[1]].piece = moved_piece
        self.chessboard[start_pos[0]][start_pos[1]].piece = None
        #TODO add analysis of the movement path 

        return True
        


class Square():
    def __init__(self, color, piece=None) -> None:
        if color not in VALID_COLORS:
            raise ValueError("Invalid color")
        self.color = color

        if piece is not None:
            self.piece = piece
        else:
            self.piece = None
    
    def set_piece(self, piece:Piece) -> None:
        if piece is not None:
            self.piece = piece
        else:
            self.piece = None
        
    def symbol(self) -> str:
        if self.piece is None:
            return "[ ]"
        elif isinstance(self.piece, Pawn):
            return " P "
        elif isinstance(self.piece, Rook):
            return " R "
        elif isinstance(self.piece, Knight):
            return " N "
        elif isinstance(self.piece, Bishop):
            return " B "
        elif isinstance(self.piece, Queen):
            return " Q "
        elif isinstance(self.piece, King):
            return " K "
        