# Project started 16/05/23 ---- ended 7/7/2023
# the goal of this project is to create a program that allow you to play an entire game of chess
# --------------------------------------
#  Click run and enjoy a chess game
# --------------------------------------

import chessboard_and_pieces as cp # all the classes and the function for the chessboard
End_Game = False  # flag for the endo fo the game
Turn = "White"  # first move is white

chessboard = cp.initialization_chessboard()
cp.chessboard_print(chessboard)

while(not(End_Game)):
    if(cp.check_mate(chessboard)):
        print("CHECK MATE")
        if(Turn == "White"):
            print("Black wins")
        else:
            print("White wins")
        End_Game = True
    elif(cp.watch_stall(Turn,chessboard)):
        print("STALL")
        End_Game = True
    else:
        if(Turn == "White"):
            print("White turn")
            king = cp.king_position("White",chessboard)
            if (cp.in_check(king,chessboard)):
                print("CHECK")
                x = chessboard[king.column][king.row].piece.possible_moves(chessboard)
                i = 1
                for c_move in x:
                    cp.print_coordinate(c_move,i)
                    i = i+1
                y = input("Where do you want to move? (Write the number left of the move)\n")
                while (not(cp.existing_coordinate_move(y,x))):
                     print("ERROR: incorrect coordinate")
                     y = input("Where do you want to move? (Write the number left of the move)\n")
                y = int(y)
                if(y > 0):
                    cp.move_piece(x[y-1],chessboard)
            else:
                y = 0
                while(y == 0):
                    x = input("Which piece do you want to move?\n")
                    old_coordinate = cp.from_input_to_coordinate(x)
                    while(not(cp.existing_coordinate_position(old_coordinate,"White",chessboard))):
                        print("ERROR: incorrect coordinate")
                        x = input("Which piece do you want to move?\n")
                        old_coordinate = cp.from_input_to_coordinate(x)
                    m = chessboard[old_coordinate.column][old_coordinate.row].piece.possible_moves(chessboard)
                    i = 1
                    if(len(m) > 0):
                        print("0) to choose another piece")
                        for c_move in  m:
                            cp.print_coordinate(c_move,i)
                            i = i+1
                        y = input("Where do you want to move? (Write the number left of the move)\n")
                        while (not(cp.existing_coordinate_move(y,m))):
                            print("ERROR: incorrect coordinate")
                            y = input("Where do you want to move? (Write the number left of the move)\n")
                    else:
                        print("no moves available")
                    y = int(y)
                    if(y > 0):
                        if(m[y-1].move_type == "Promotion" or m[y-1].move_type == "Promoting_capture"):
                            piece_to_promote_to = cp.Promotion()
                            if(piece_to_promote_to != 0):
                                cp.move_piece_promotion(m[y-1],chessboard,piece_to_promote_to)
                            else:
                                y = 0
                        else:
                            cp.move_piece(m[y-1],chessboard)
        else:
            print("Black turn")
            king = cp.king_position("Black",chessboard)
            if (cp.in_check(king,chessboard)):
                print("CHECK")
                x = king.possible_moves(chessboard)
                i = 1
                for c_move in x:
                    cp.print_coordinate(c_move,i)
                    i = i+1
                y = input("Where do you want to move? (Write the number left of the move)\n")
                while (not(cp.existing_coordinate_move(y,x))):
                     print("ERROR: incorrect coordinate")
                     y = input("Where do you want to move? (Write the number left of the move)\n")
                y = int(y)
                if(y > 0):
                    cp.move_piece(x[y-1],chessboard)
            else:
                y = 0
                while(y == 0):
                    x = input("Which piece do you want to move?\n")
                    old_coordinate = cp.from_input_to_coordinate(x)
                    while(not(cp.existing_coordinate_position(old_coordinate,"Black",chessboard))):
                        print("ERROR: incorrect coordinate")
                        x = input("Which piece do you want to move?\n")
                        old_coordinate = cp.from_input_to_coordinate(x)
                    m = chessboard[old_coordinate.column][old_coordinate.row].piece.possible_moves(chessboard)
                    i = 1
                    if(len(m)>0):
                        print("0) to choose another piece")
                        for c_move in  m:
                            cp.print_coordinate(c_move,i)
                            i = i+1
                        y = input("Where do you want to move? (Write the number left of the move)\n")
                        while (not(cp.existing_coordinate_move(y,m))):
                            print("ERROR: incorrect coordinate")
                            y = input("Where do you want to move? (Write the number left of the move)\n")
                    else:
                        print("no moves available")
                    y = int(y)
                    if(y > 0):
                        if(m[y-1].move_type == "Promotion" or m[y-1].move_type == "Promoting_capture"):
                            piece_to_promote_to = cp.Promotion()
                            if(piece_to_promote_to != 0):
                                cp.move_piece_promotion(m[y-1],chessboard,piece_to_promote_to)
                            else: 
                                y = 0 
                        else:
                            cp.move_piece(m[y-1],chessboard)
        cp.chessboard_print(chessboard)
        if (Turn == "White"):
            Turn = "Black"
        else:
            Turn = "White"
