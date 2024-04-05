from .utils import VALID_COLORS


class Piece():
    def __init__(self, color) -> None:
        if color not in VALID_COLORS:
            raise ValueError("Invalid color")
        self.color = color
    
    def validate_move(self, start_pos, end_pos,): #TODO consider moving calling _is_in_board earlier
        raise NotImplementedError("Subclass must implement, this is an abstract method")
    
    

class Pawn(Piece):
    def validate_move(self, start_pos, end_pos) -> bool:
        # board coordinates are: (row, column)
        #TODO
        #add the en passant and the first move
        if self.color == 'white':
            if end_pos[0] == start_pos[0]+1 and end_pos[1] == start_pos[1]: #normal movement
                return True
            elif end_pos[0] == start_pos[0]+1 and (end_pos[1] == start_pos[1]+1 or end_pos[1] == start_pos[1]-1): #taking a piece
                return True
            else: return False
        elif self.color == 'black':
            if end_pos[0] == start_pos[0]-1 and end_pos[1] == start_pos[1]: #normal movement
                return True
            elif end_pos[0] == start_pos[0]-1 and (end_pos[1] == start_pos[1]-1 or end_pos[1] == start_pos[1]+1): #taking a piece
                return True
            else: return False

    

#TODO add validation for end_pos != start_pos

class Rook(Piece):
    def validate_move(self, start_pos, end_pos):
        if (end_pos[0] == start_pos[0] and end_pos[1] != start_pos[1]) or (end_pos[0] != start_pos[0] and end_pos[1] == start_pos[1]):
            return True
        else: return False
    
    
class Knight(Piece):
    def validate_move(self, start_pos, end_pos):
        if ((end_pos[0] == start_pos[0]+2 and end_pos[1] != start_pos[1]+1) # TODO this can be replaced with difference and absolute value
            or (end_pos[0] == start_pos[0]+2 and end_pos[1] != start_pos[1]-1) 
            or (end_pos[0] == start_pos[0]-2 and end_pos[1] != start_pos[1]+1)
            or (end_pos[0] == start_pos[0]-2 and end_pos[1] != start_pos[1]-1)
            or (end_pos[0] == start_pos[0]+1 and end_pos[1] != start_pos[1]+2)
            or (end_pos[0] == start_pos[0]+1 and end_pos[1] != start_pos[1]-2)
            or (end_pos[0] == start_pos[0]-1 and end_pos[1] != start_pos[1]+2)
            or (end_pos[0] == start_pos[0]-1 and end_pos[1] != start_pos[1]-2)):
            return True
        else: return False
    
class Bishop(Piece):
    def validate_move(self, start_pos, end_pos):
        if (end_pos[0] - start_pos[0] == end_pos[1] - start_pos[1]):
            return True
        else: return False
    
    

class Queen(Piece):
    def validate_move(self, start_pos, end_pos):
        if ((end_pos[0] - start_pos[0] == end_pos[1] - start_pos[1]) #bishop move
            or (end_pos[0] == start_pos[0] and end_pos[1] != start_pos[1]) or (end_pos[0] != start_pos[0] and end_pos[1] == start_pos[1])): #Rook move
            return True
        else: return False
    
class King(Piece):
    def validate_move(self, start_pos, end_pos):
        if ((end_pos[0] - start_pos[0] == 1 and end_pos[1] - start_pos[1] == 1) #bishop move
            or (end_pos[0] == start_pos[0] and end_pos[1] - start_pos[1] == 1) 
            or (end_pos[0] - start_pos[0] == 1 and end_pos[1] == start_pos[1])):
            return True
        else: return False