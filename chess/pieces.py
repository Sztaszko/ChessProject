from .utils import VALID_COLORS

class Piece():
    def __init__(self, color) -> None:
        if color not in VALID_COLORS:
            raise ValueError("Invalid color")
        self.color = color
    
    def validate_move(self, start_pos, end_pos,):
        raise NotImplementedError("Subclass must implement, this is an abstract method")
    
    def symbol(self) -> str:
        return str("[ ]")
    
    def _is_in_board(self, end_pos) -> bool:
        return end_pos[0] < 8 and end_pos[1] < 8 and end_pos[0] >= 0 and end_pos[1] >= 0
    
    

class Pawn(Piece):
    def validate_move(self, start_pos, end_pos) -> bool:
        if super()._is_in_board(end_pos):
            #TODO
            #add the en passant and the first move
            if end_pos[0] == start_pos[0] and end_pos[1] == start_pos[1]+1: #normal movement
                return True
            elif end_pos[1] == start_pos[1]+1 and (end_pos[0] == start_pos[0]+1 or end_pos[0] == start_pos[0]-1): #taking a piece
                return True
            else: return False
        return False
    
    def symbol(self) -> str:
        return str(" P ")
    
class Rook(Piece):
    def validate_move(self, start_pos, end_pos):
        if super()._is_in_board(end_pos):
            
            if end_pos[0] == start_pos[0] and end_pos[1] != start_pos[1]:
                return True
            elif end_pos[0] != start_pos[0] and end_pos[1] == start_pos[1]:
                return True
            else: return False

        return False
    
    def symbol(self) -> str:
        return str(" R ")
    
class Knight(Piece):
    
    
    def symbol(self) -> str:
        return str(" N ")
    
class Bishop(Piece):

    def symbol(self) -> str:
        return str(" B ")
    

class Queen(Piece):

    def symbol(self) -> str:
        return str(" Q ")
    
class King(Piece):

    def symbol(self) -> str:
        return str(" K ")