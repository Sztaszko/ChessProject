from .utils import VALID_COLORS
from .board import Board

class Piece():
    def __init__(self, color) -> None:
        if color not in VALID_COLORS:
            raise ValueError("Invalid color")
        self.color = color
    
    def validate_move(self, start_pos, end_pos, board:Board):
        raise NotImplementedError("Subclass must implement, this is an abstract method")
    
    def _is_in_board(self, end_pos, board:Board) -> bool:
        return end_pos[0] < board.size[0] and end_pos[1] < board.size[1]
    
class Pawn(Piece):
    def validate_move(self, start_pos, end_pos, board:Board) -> bool:
        if super()._is_in_board(end_pos, board):
            #TODO
            #add the en passant and the first move
            if end_pos[0] == start_pos[0] and end_pos[1] == start_pos[1]+1: #normal movement
                return True
            elif end_pos[1] == start_pos[1]+1 and (end_pos[0] == start_pos[0]+1 or end_pos[0] == start_pos[0]-1): #taking a piece
                return True
            else: return False
        return False