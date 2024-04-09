from .utils import VALID_COLORS


class Piece():
    def __init__(self, color) -> None:
        if color not in VALID_COLORS:
            raise ValueError("Invalid color")
        self.color = color
    
    def validate_move(self, start_pos, end_pos,):
        raise NotImplementedError("Subclass must implement, this is an abstract method")
    
    def get_movement_path(self, start_pos, end_pos) -> list:
        """Method used to generate path of the piece. It returns the list of coordinates between start position and end position.
        For example: Rook[6][0] moves to position [3][0]. Generated list will be [(5,0),(4,0)]
        """
        raise NotImplementedError("Subclass must implement, this is an abstract method")
    
    

class Pawn(Piece):
    def validate_move(self, start_pos, end_pos) -> bool:
        # board coordinates are: (row, column)
        #TODO add the en passant and the first move
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

    def get_movement_path(self, start_pos, end_pos) -> list:
        #TODO if first_move...
        return []

    

#TODO add validation for end_pos != start_pos

class Rook(Piece):
    def validate_move(self, start_pos, end_pos):
        if (end_pos[0] == start_pos[0] and end_pos[1] != start_pos[1]) or (end_pos[0] != start_pos[0] and end_pos[1] == start_pos[1]):
            return True
        else: return False

    def get_movement_path(self, start_pos, end_pos) -> list: 
        if not self.validate_move(start_pos, end_pos):
            return None
        
        movement_path = []
        if (end_pos[0] == start_pos[0]):
            if end_pos[1] > start_pos[1]:
                movement_path = [(start_pos[0],i) for i in range (start_pos[1]+1, end_pos[1], 1)]
            elif end_pos[1] < start_pos[1]:
                movement_path = [(start_pos[0],i) for i in range (start_pos[1]-1, end_pos[1], -1)]

        if (end_pos[1] == start_pos[1]):
            if end_pos[0] > start_pos[0]:
                movement_path = [(i,start_pos[1]) for i in range (start_pos[0]+1, end_pos[0], 1)]
            elif end_pos[0] < start_pos[0]:
                movement_path = [(i,start_pos[1]) for i in range (start_pos[0]-1, end_pos[0], -1)]
        
        return movement_path
    
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

    def get_movement_path(self, start_pos, end_pos) -> list:
        if self.validate_move(start_pos, end_pos): 
            return [] # the knight jumps over pieces
        else: return None
    
class Bishop(Piece):
    def validate_move(self, start_pos, end_pos):
        if (abs(end_pos[0] - start_pos[0]) == abs(end_pos[1] - start_pos[1])):
            return True
        else: return False
    
    def get_movement_path(self, start_pos, end_pos) -> list: 
        if not self.validate_move(start_pos, end_pos):
            return None
        
        movement_path = []
        if (end_pos[0] > start_pos[0]) and (end_pos[1] > start_pos[1]): # moving up-right
            movement_path = [(start_pos[0]+i, start_pos[1]+i) for i in range(1, end_pos[0]-start_pos[0], 1)]
        elif (end_pos[0] > start_pos[0]) and (end_pos[1] < start_pos[1]): # moving up-left
            movement_path = [(start_pos[0]+i, start_pos[1]-i) for i in range(1, end_pos[0]-start_pos[0], 1)]
        elif (end_pos[0] < start_pos[0]) and (end_pos[1] > start_pos[1]): # moving down-right
            movement_path = [(start_pos[0]-i, start_pos[1]+i) for i in range(1, start_pos[0]-end_pos[0], 1)]
        elif (end_pos[0] < start_pos[0]) and (end_pos[1] > start_pos[1]): # moving down-left
            movement_path = [(start_pos[0]-i, start_pos[1]-i) for i in range(1, start_pos[0]-end_pos[0], 1)]
        
        return movement_path

class Queen(Piece):
    def validate_move(self, start_pos, end_pos):
        if ((end_pos[0] - start_pos[0] == end_pos[1] - start_pos[1]) #bishop move
            or (end_pos[0] == start_pos[0] and end_pos[1] != start_pos[1]) 
            or (end_pos[0] != start_pos[0] and end_pos[1] == start_pos[1])): #Rook move
            return True
        else: return False

    def get_movement_path(self, start_pos, end_pos) -> list:
        if self.validate_move(start_pos, end_pos):
            return [(start_pos[0]+i, start_pos[1]+j) for i in range(1, abs(end_pos[0]-start_pos[0])) for j in range(1, abs(end_pos[1]-start_pos[1]))]
        else: return None
    
class King(Piece):
    def validate_move(self, start_pos, end_pos):
        if ((end_pos[0] - start_pos[0] == 1 and end_pos[1] - start_pos[1] == 1) #bishop move
            or (end_pos[0] == start_pos[0] and end_pos[1] - start_pos[1] == 1) 
            or (end_pos[0] - start_pos[0] == 1 and end_pos[1] == start_pos[1])):
            return True
        else: return False

    def get_movement_path(self, start_pos, end_pos) -> list:
        if self.validate_move(start_pos, end_pos):
            return [(start_pos[0]+i, start_pos[1]+j) for i in range(1, abs(end_pos[0]-start_pos[0])) for j in range(1, abs(end_pos[1]-start_pos[1]))]
        else: return None