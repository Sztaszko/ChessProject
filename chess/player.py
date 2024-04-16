from .utils import VALID_COLORS
import re

class Player():
    def __init__(self, color) -> None:

        if color not in VALID_COLORS:
            raise ValueError("Invalid color")
        self.color = color

    def input_move(self):
        print("It's {}'s move. Please enter the move: ".format(self.color))
        player_input = input()

        input_pattern = r"\[\d\]\[\d\] \[\d\]\[\d\]"

        if player_input == "quit":
            return player_input
        
        # Check if the input string matches the pattern
        if not re.match(input_pattern, player_input):
            print("Invalid input format. Coordinates must be in the format [x1][y1] [x2][y2].")
            return None
        
        coordinate_pairs = player_input.strip().split()

        coordinates = []

        for pair in coordinate_pairs:
            x, y = pair.strip('[]').split('][')
            coordinates.append((int(x), int(y)))

        return coordinates
