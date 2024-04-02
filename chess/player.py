from utils import VALID_COLORS

class Player():
    def __init__(self, color) -> None:

        if color not in VALID_COLORS:
            raise ValueError("Invalid color")
        self.color = color

    def make_move(self, start_pos, end_pos):
        pass