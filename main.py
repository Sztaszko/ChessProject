# main.py
from chess import board

def main():
    brd = board.Board()
    brd.initialize_pieces()
    brd.print_board()


if __name__== "__main__":
    main()