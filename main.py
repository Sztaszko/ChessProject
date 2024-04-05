# main.py
from chess import board

def main():
    brd = board.Board()
    brd.initialize_pieces()
    brd.print_board()
    brd.move_piece((1,0), (2,0)) # valid
    brd.move_piece((0,1), (2,2)) # valid
    brd.move_piece((6,1), (5,1)) # valid
    brd.move_piece((7,0), (2,0)) # valid - taking


if __name__== "__main__":
    main()