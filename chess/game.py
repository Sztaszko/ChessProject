from .board import Board
from .player import Player


class Game():
    def __init__(self) -> None:
        self.running : bool = False
        self.white_player = Player("white")
        self.black_player = Player("black")

    def initialize(self) -> None:
        self.board = Board()
        self.board.initialize_pieces()
        self.board.print_board()
        self.print_start_info()
        self.round = 0

    
    def print_start_info(self) -> None:
        print("The board is set. To move type in coordinates of the piece and the target coordinates in brackets separated by space (i.e.: [1][0] [2][0])")

    def start(self) -> bool:
        self.running = True
        
        while True:
            coordinates = []

            self.board.print_board()

            if self.round %2 == 0:
                coordinates = self.white_player.input_move()
            else:
                coordinates = self.black_player.input_move()
            
            if coordinates == "quit":
                print("Quitting game")
                self.stop()
                break
            
            if self.board.move_piece(coordinates[0], coordinates[1]):
                self.round = self.round+1


    def stop(self):
        self.running = False

    
    def is_running(self) -> bool:
        return self.running
    

