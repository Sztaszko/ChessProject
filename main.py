# main.py


class Board():
    """The Board class represents chessboard. It is responsible for movement validation and pieces arrangement.
    """

    def __init__(self) -> None:
         self.square
    
    def move_piece(self, start_pos, end_pos):
        pass


class Piece():
    def __init__(self) -> None:
        pass
    
    def move():
        pass

class Player():
    VALID_COLORS = ["white", "black"]

    def __init__(self, color) -> None:

        if color not in self.VALID_COLORS:
            raise ValueError("Invalid color")
        self.color = color

    def make_move(self, piece: Piece, end_pos):
        pass


def main():
    pass


if __name__== "__main__":
    main()