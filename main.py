# main.py
from chess import game

def main():

    app = game.Game()
    app.initialize()
    app.start()


    # brd = board.Board()
    # brd.initialize_pieces()
    # brd.print_board()
    # brd.move_piece((1,0), (2,0)) # valid, white Pawn to 2,0
    # brd.move_piece((6,1), (5,1)) # valid, black Pawn to 5,1
    # brd.move_piece((0,1), (2,2)) # valid, white knight to 2,2
    # brd.move_piece((7,0), (2,0)) # invalid, black Rook to 2,0 (taking a white Pawn), but there is black Pawn on the path
    # brd.move_piece((6,3), (5,3)) # valid, black Pawn to 5,3
    # brd.move_piece((7,2), (5,4)) # invalid, black Bishop to 5,2, but there is black Pawn on the path
    # brd.print_board()


if __name__== "__main__":
    main()