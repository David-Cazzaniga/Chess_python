# -------------------------------------------
# TO RUN THE PROGRAM RUN "MAIN CHESSBOARD"
# -------------------------------------------

# This file define all the classes and the function for the main chessboard

import copy
chessboard_log = []

# Defition of the classes

class Piece:
    def __init__(self, column, row, team):   # every piece has column and row for the posistion on the chessboard and a team
        self.column=column
        self.row=row
        self.team=team

class Tower(Piece):
    def __init__(self, column, row, team, first_move_done):   # first move done is a flag to let the algoritm know if you can castle or not
        super().__init__(column, row, team)
        self.first_move_done = first_move_done
    def print_letter(self):
        return "R"   # that's the letter print on the screen for the piece
    def possible_moves(self,chessboard):  # check if the piece is pinned, then, if available return an array with all the possible move
        if (pinned(self,chessboard)):
            move=[]
            x = watch_pinned(self,chessboard)
            if(x):
                move.extend(x)
            return move
        else:
            move = []
            x = watch_left(self,chessboard)
            if(x):
                move.extend(x)
            x = watch_right(self,chessboard)
            if(x):
                move.extend(x)
            x = watch_up(self,chessboard)
            if(x):
                move.extend(x)
            x = watch_down(self,chessboard)
            if(x):
                move.extend(x)
            x = watch_castling(self,chessboard)
            if(x):
                move.extend(x)
            return move
    
    def possible_moves_check(self,chessboard):   # check the same possible moves without checking if the piece is pinned cause it was already check and to avoid an infinite loop caused by the pinned function asking for the in check function having another request from the pinned function and so on
        move = []
        x = watch_left(self,chessboard)
        if(x):
            move.extend(x)
        x = watch_right(self,chessboard)
        if(x):
            move.extend(x)
        x = watch_up(self,chessboard)
        if(x):
            move.extend(x)
        x = watch_down(self,chessboard)
        if(x):
            move.extend(x)
        x = watch_castling(self,chessboard)
        if(x):
            move.extend(x)
        return move

class Knight(Piece):
    def print_letter(self):
        return "K"
    def possible_moves(self,chessboard):
        if (pinned(self,chessboard)):
            x = watch_pinned(self,chessboard)
            if(x):
                move.extend(x)
            return move
        else:
            move = []
            x = watch_knight(self,chessboard)
            if(x):    
                move.extend(x)
            return move
    
    def possible_moves_check(self,chessboard):
        move = []
        x = watch_knight(self,chessboard)
        if(x):    
            move.extend(x)
        return move

class Bishop(Piece):
    def print_letter(self):
        return "B"
    def possible_moves(self,chessboard):
        if (pinned(self,chessboard)):
            x = watch_pinned(self,chessboard)
            if(x):
                move.extend(x)
            return move
        else:
            move = []
            x = watch_up_left(self,chessboard)
            if(x):    
                move.extend(x)
            x = watch_down_left(self,chessboard)
            if(x):    
                move.extend(x)
            x = watch_down_right(self,chessboard)
            if(x):    
                move.extend(x)
            x = watch_up_right(self,chessboard)
            if(x):    
                move.extend(x)
            return move
    
    def possible_moves_check(self,chessboard):
        move = []
        x = watch_up_left(self,chessboard)
        if(x):    
            move.extend(x)
        x = watch_down_left(self,chessboard)
        if(x):    
            move.extend(x)
        x = watch_down_right(self,chessboard)
        if(x):    
            move.extend(x)
        x = watch_up_right(self,chessboard)
        if(x):    
            move.extend(x)
        return move

class Queen(Piece):
    def print_letter(self):
        return "Q"
    def possible_moves(self,chessboard):
        if (pinned(self,chessboard)):
            x = watch_pinned(self,chessboard)
            if(x):
                move.extend(x)
            return move
        else:
            move = []
            x = watch_left(self,chessboard)
            if(x):
                move.extend(x)
            x = watch_right(self,chessboard)
            if(x):
                move.extend(x)
            x = watch_up(self,chessboard)
            if(x):
                move.extend(x)
            x = watch_down(self,chessboard)
            if(x):
                move.extend(x)
            x = watch_up_left(self,chessboard)
            if(x):
                move.extend(x)
            x = watch_down_left(self,chessboard)
            if(x):
                move.extend(x)
            x = watch_down_right(self,chessboard)
            if(x):
                move.extend(x)
            x = watch_up_right(self,chessboard)
            if(x):
                move.extend(x)
            return move
    
    def possible_moves_check(self,chessboard):
        move = []
        x = watch_left(self,chessboard)
        if(x):
            move.extend(x)
        x = watch_right(self,chessboard)
        if(x):
            move.extend(x)
        x = watch_up(self,chessboard)
        if(x):
            move.extend(x)
        x = watch_down(self,chessboard)
        if(x):
            move.extend(x)
        x = watch_up_left(self,chessboard)
        if(x):
            move.extend(x)
        x = watch_down_left(self,chessboard)
        if(x):
            move.extend(x)
        x = watch_down_right(self,chessboard)
        if(x):
            move.extend(x)
        x = watch_up_right(self,chessboard)
        if(x):
            move.extend(x)
        return move

class King(Piece):
    def __init__(self, column, row, team, check, first_move_done):
        super().__init__(column, row, team)
        self.check = check
        self.first_move_done = first_move_done
    def print_letter(self):
        return "K"
    def possible_moves(self,chessboard):
        move = []
        coordinate_pieces_that_are_giving_check = in_check(self,chessboard)  # it ask for the pieces giving check in order to give the array to watch check defense function that return all the possible moves to avoid the check
        if(coordinate_pieces_that_are_giving_check):
            x = watch_check_defense(self,coordinate_pieces_that_are_giving_check, chessboard)
            if(x):    
                move.extend(x)
        else:
            x = watch_king(self,chessboard)
            if(x):    
                move.extend(x)
            x = watch_castling(self,chessboard)
            if(x):
                move.extend(x)
        return move

class Pawn(Piece):
    def __init__(self, column, row, team, first_move_done, two_square_advancement_previous_turn):  # two square advacment previous turn is a flag for the enpassant
        super().__init__(column, row, team)
        self.first_move_done = first_move_done
        self.two_square_advancement_previous_turn = two_square_advancement_previous_turn
    def print_letter(self):
        return "p"
    def possible_moves(self,chessboard):
        if (pinned(self,chessboard)):
            x = watch_pinned(self,chessboard)
            return x
        else:
            move = []
            x = watch_pawn(self,chessboard)
            if(x):    
                move.extend(x)
            x = watch_enpassant(self,chessboard,chessboard_log)
            if(x):    
                move.extend(x)
            return move
    
    def possible_moves_check(self,chessboard):
        move = []
        x = watch_pawn(self,chessboard)
        if(x):    
            move.extend(x)
        x = watch_enpassant(self,chessboard,chessboard_log)
        if(x):    
            move.extend(x)
        return move

# Defition of the function

def in_check(king,chessboard):  # return an array containing all the coordinate of the moves giving check
    if(type(king) == King):
        move = []
        coordinate_pieces_that_are_giving_check = []   # check all the coordinates where a piece could possibly give the king check
        x = watch_up(king,chessboard)
        if(x):        
            move.extend(x)
        x = watch_right(king,chessboard)
        if(x):      
            move.extend(x)
        x = watch_down(king,chessboard)
        if(x):       
            move.extend(x)
        x = watch_left(king,chessboard)
        if(x):    
            move.extend(x)
        x = watch_up_left(king,chessboard)
        if(x):
            move.extend(x)
        x = watch_up_right(king,chessboard)
        if(x):  
            move.extend(x)
        x = watch_down_right(king,chessboard)
        if(x): 
            move.extend(x)
        x = watch_down_left(king,chessboard)
        if(x):        
            move.extend(x)
        x = watch_knight(king,chessboard)
        if(x):     
            move.extend(x)
        opposing_pieces_coodinate = []
        for m in move:                                                            # check if there are pieces in those coordinate excluding the other king
            if(chessboard[m.column][m.row].piece != None):
                opposing_pieces_coodinate.append(m)
        for piece in opposing_pieces_coodinate:
            if(type(chessboard[piece.column][piece.row].piece) != King):
                piece_moves = chessboard[piece.column][piece.row].piece.possible_moves_check(chessboard)
                for m in piece_moves:                                                                             # check if the piece has a capture move
                    if(m.move_type == "Capture" or m.move_type == "Promoting_capture"):
                        if(type(chessboard[m.column][m.row].piece) == King):      # check if the capture move target is the king
                            coordinate_pieces_that_are_giving_check.append(m)     # if it is the coordinate for the move is added to the array of the coordinate of the pieces giving check
        return coordinate_pieces_that_are_giving_check
    else:
        print("ERROR: It's not a King")

def king_position(team,chessboard):  # return the king piece from the team passed in the function
    for i in range(8):
        for j in range(8):
            if(type(chessboard[i][j].piece) == King and chessboard[i][j].piece.team == team):
                return chessboard[i][j].piece

def opponent_king_position(team,chessboard):  # return the king piece from the opposing team passed in the function
    if (team == "White"):
        team = "Black"
    else:
        team = "White"
    for i in range(8):
        for j in range(8):
            if(type(chessboard[i][j].piece) == King and chessboard[i][j].piece.team == team):
                return chessboard[i][j].piece

def pinned(piece,chessboard):   # return true or false if the piece passed is pinned or not checked by removing that piece and watch if the number of piece giving check would increase
    i = piece.column
    j = piece.row
    team = piece.team
    x = king_position(team,chessboard)
    piece_giving_check_before = in_check(x,chessboard)
    piece_save = chessboard[i][j].piece
    chessboard[i][j].piece = None
    chessboard[i][j].occupied = False
    piece_giving_check_after = in_check(x,chessboard)
    chessboard[i][j].piece = piece_save
    chessboard[i][j].occupied = True
    if (len(piece_giving_check_before) != len(piece_giving_check_after)):
        return True
    else:
        return False
    
def watch_left(piece,chessboard):  # return an array with all the cordinate free in the direction the function is checking plus the eventually possible capture 
    i = copy.copy(piece.column)
    j = copy.copy(piece.row)
    team = copy.copy(piece.team)
    starting_i = i
    starting_j = j
    move = []
    while(i-1 > -1):
        if(chessboard[i-1][j].piece == None):
            x = Coordinate(i-1,j,None,starting_i,starting_j)
            if(x):
                move.append(x)
        elif(chessboard[i-1][j].piece.team != team):
            x = Coordinate(i-1,j,"Capture",starting_i,starting_j)
            if(x):
                move.append(x)
            return move
        else:
            return move
        i = i-1
    else:
        return move

def watch_right(piece,chessboard):   # same 
    i = copy.copy(piece.column)
    j = copy.copy(piece.row)
    team = copy.copy(piece.team)
    starting_i = i
    starting_j = j
    move = []
    while(i+1 < 8):
        if(chessboard[i+1][j].piece == None):
            x = Coordinate(i+1,j,None,starting_i,starting_j)
            if(x):
                move.append(x)
        elif(chessboard[i+1][j].piece.team != team):
            x = Coordinate(i+1,j,"Capture",starting_i,starting_j)
            if(x):
                move.append(x)
            return move
        else:
            return move
        i = i+1
    else:
        return move

def watch_up(piece,chessboard):   # same
    i = copy.copy(piece.column)
    j = copy.copy(piece.row)
    team = copy.copy(piece.team)
    starting_i = i
    starting_j = j
    move = []
    while(j+1 < 8):
        if(chessboard[i][j+1].piece == None):
            x = Coordinate(i,j+1,None,starting_i,starting_j)
            if(x):
                move.append(x)
        elif(chessboard[i][j+1].piece.team != team):
            x = Coordinate(i,j+1,"Capture",starting_i,starting_j)
            if(x):
                move.append(x)
            return move
        else:
            return move
        j= j+1
    else:
        return move

def watch_down(piece,chessboard):   # same
    i = copy.copy(piece.column)
    j = copy.copy(piece.row)
    team = copy.copy(piece.team)
    starting_i = i
    starting_j = j
    move = []
    while(j-1 > -1):
        if(chessboard[i][j-1].piece == None):
            x = Coordinate(i,j-1,None,starting_i,starting_j)
            if(x):
                move.append(x)
        elif(chessboard[i][j-1].piece.team != team):
            x = Coordinate(i,j-1,"Capture",starting_i,starting_j)
            if(x):
                move.append(x)
            return move
        else:
            return move
        j = j-1
    else:
        return move

def watch_up_right(piece,chessboard):   # same
    i = copy.copy(piece.column)
    j = copy.copy(piece.row)
    team = copy.copy(piece.team)
    starting_i = i
    starting_j = j
    move = []
    while(j+1 < 8 and i+1 < 8):
        if(chessboard[i+1][j+1].piece == None):
            x = Coordinate(i+1,j+1,None,starting_i,starting_j)
            if(x):
                move.append(x)
        elif(chessboard[i+1][j+1].piece.team != team):
            x = Coordinate(i+1,j+1,"Capture",starting_i,starting_j)
            if(x):
                move.append(x)
            return move
        else:
            return move
        i = i+1
        j = j+1
    else:
        return move

def watch_down_right(piece,chessboard):   # same
    i = copy.copy(piece.column)
    j = copy.copy(piece.row)
    team = copy.copy(piece.team)
    starting_i = i
    starting_j = j
    move = []
    while(j-1 > -1 and i+1 < 8):
        if(chessboard[i+1][j-1].piece == None):
            x = Coordinate(i+1,j-1,None,starting_i,starting_j)
            if(x):
                move.append(x)
        elif(chessboard[i+1][j-1].piece.team != team):
            x = Coordinate(i+1,j-1,"Capture",starting_i,starting_j)
            if(x):
                move.append(x)
            return move
        else:
            return move
        i = i+1
        j = j-1
    else:
        return move

def watch_down_left(piece,chessboard):   # same
    i = copy.copy(piece.column)
    j = copy.copy(piece.row)
    team = copy.copy(piece.team)
    starting_i = i
    starting_j = j
    move = []
    while(j-1 > -1 and i-1 > -1):
        if(chessboard[i-1][j-1].piece == None):
            x = Coordinate(i-1,j-1,None,starting_i,starting_j)
            if(x):
                move.append(x)
        elif(chessboard[i-1][j-1].piece.team != team):
            x = Coordinate(i-1,j-1,"Capture",starting_i,starting_j)
            if(x):
                move.append(x)
            return move
        else:
            return move
        i = i-1
        j = j-1
    else:
        return move

def watch_up_left(piece,chessboard):   # same
    i = copy.copy(piece.column)
    j = copy.copy(piece.row)
    team = copy.copy(piece.team)
    starting_i = i
    starting_j = j
    move = []
    while(j+1 < 8 and i-1 > -1):
        if(chessboard[i-1][j+1].piece == None):
            x = Coordinate(i-1,j+1,None,starting_i,starting_j)
            if(x):
                move.append(x)
        elif(chessboard[i-1][j+1].piece.team != team):
            x = Coordinate(i-1,j+1,"Capture",starting_i,starting_j)
            if(x):
                move.append(x)
            return move
        else:
            return move
        i = i-1
        j = j+1
    else:
        return move

def watch_knight(piece,chessboard):   # same but not in a straight line, but checking the possible knight position
    i = piece.column
    j = piece.row
    team = piece.team
    move = []
    if(i-1 > -1 and j-2 >-1):
        if(chessboard[i-1][j-2].piece == None):
            x = Coordinate(i-1,j-2,None,i,j)
            move.append(x)
        elif(chessboard[i-1][j-2].piece != None):
            if(chessboard[i-1][j-2].piece.team != team):
                x = Coordinate(i-1,j-2,"Capture",i,j)
                move.append(x)

    if(i-2 > -1 and j-1 >-1):
        if(chessboard[i-2][j-1].piece == None):
            x = Coordinate(i-2,j-1,None,i,j)
            move.append(x)
        elif(chessboard[i-2][j-1].piece != None):
            if(chessboard[i-2][j-1].piece.team != team):
                x = Coordinate(i-2,j-1,"Capture",i,j)
                move.append(x)
    
    if(i-2 > -1 and j+1 < 8):
        if(chessboard[i-2][j+1].piece == None):
            x = Coordinate(i-2,j+1,None,i,j)
            move.append(x)
        elif(chessboard[i-2][j+1].piece != None):
            if(chessboard[i-2][j+1].piece.team != team):
                x = Coordinate(i-2,j+1,"Capture",i,j)
                move.append(x)
    
    if(i-1 > -1 and j+2 < 8):
        if(chessboard[i-1][j+2].piece == None):
            x = Coordinate(i-1,j+2,None,i,j)
            move.append(x)
        elif(chessboard[i-1][j+2].piece != None):
            if(chessboard[i-1][j+2].piece.team != team):
                x = Coordinate(i-1,j+2,"Capture",i,j)
                move.append(x)
    
    if(i+1 < 8 and j+2 < 8):
        if(chessboard[i+1][j+2].piece == None):
            x = Coordinate(i+1,j+2,None,i,j)
            move.append(x)
        elif(chessboard[i+1][j+2].piece != None):
            if(chessboard[i+1][j+2].piece.team != team):
                x = Coordinate(i+1,j+2,"Capture",i,j)
                move.append(x)

    if(i+2 < 8 and j+1 < 8):
        if(chessboard[i+2][j+1].piece == None):
            x = Coordinate(i+2,j+1,None,i,j)
            move.append(x)
        elif(chessboard[i+2][j+1].piece != None):
            if(chessboard[i+2][j+1].piece.team != team):
                x = Coordinate(i+2,j+1,"Capture",i,j)
                move.append(x)

    if(i+2 < 8 and j-1 > -1):
        if(chessboard[i+2][j-1].piece == None):
            x = Coordinate(i+2,j-1,None,i,j)
            move.append(x)
        elif(chessboard[i+2][j-1].piece != None):
            if(chessboard[i+2][j-1].piece.team != team):
                x = Coordinate(i+2,j-1,"Capture",i,j)
                move.append(x)

    if(i+1 < 8 and j-2 > -1):
        if(chessboard[i+1][j-2].piece == None):
            x = Coordinate(i+1,j-2,None,i,j)
            move.append(x)
        elif(chessboard[i+1][j-2].piece != None):
            if(chessboard[i+1][j-2].piece.team != team):
                x = Coordinate(i+1,j-2,"Capture",i,j)
                move.append(x)

    return move

def watch_castling(piece,chessboard):   # return the coordinate of the moves if the castle is available, it work either passing the rook or the king
    if (type(piece) == Tower or type(piece) == King):
        i = piece.column
        j = piece.row
        team = piece.team
        p = piece.first_move_done
        moves = []
        if(p == False):
            if(team == "White"):
                if(chessboard[4][0].piece != None):
                    if(type(chessboard[4][0].piece) == King):
                        if(chessboard[4][0].piece.team == team):
                            if(chessboard[4][0].piece.first_move_done == False):
                                if((i == 0 and j == 0) or (i == 4 and j == 0)):
                                    if(chessboard[0][0].piece != None):
                                        if(type(chessboard[0][0].piece) == Tower):
                                            if(chessboard[0][0].piece.team == team):
                                                if(chessboard[0][0].piece.first_move_done == False):        
                                                    if(not(in_check(chessboard[4][0].piece,chessboard))):
                                                        if(chessboard[1][0].piece == None and chessboard[2][0].piece == None and chessboard[3][0].piece == None):
                                                            castling_flag = True
                                                            for k in range(2):
                                                                fake_square = Piece(k+2,0,team)  # the fake square is used to check if the squares crossed by the king are in check
                                                                coordinate_that_Im_watching = Coordinate(k+2,0,None,None,None)
                                                                fake_piece_moves = []
                                                                x = watch_up_left(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                x = watch_up(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                x = watch_up_right(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                x = watch_knight(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                for move in fake_piece_moves:
                                                                    if(move.move_type == "Capture"):
                                                                        opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves_check(chessboard)
                                                                        for opponent_piece_move in opponent_piece_moves:
                                                                            if(opponent_piece_move.column == coordinate_that_Im_watching.column and opponent_piece_move.row == coordinate_that_Im_watching.row):
                                                                                castling_flag = False
                                                            if (castling_flag == True):   # if none of the squares were in check the castling flag is True so it's possible to castle
                                                                if (type(piece) == King):
                                                                    castling = Coordinate(2,0,"queenside castling",i,j)  
                                                                    moves.append(castling)
                                                                elif(type(piece) == Tower):
                                                                    castling = Coordinate(3,0,"queenside castling",i,j)
                                                                    moves.append(castling)
                                if((i == 7 and j == 0) or (i == 4 and j == 0)):
                                    if(chessboard[7][0].piece != None):
                                        if(type(chessboard[7][0].piece) == Tower):
                                            if(chessboard[7][0].piece.team == team):
                                                if(chessboard[7][0].piece.first_move_done == False):
                                                    if(not(in_check(chessboard[4][0].piece,chessboard))):
                                                        if(chessboard[5][0].piece == None and chessboard[6][0].piece == None):
                                                            castling_flag = True
                                                            for k in range(2):
                                                                fake_square = Piece(k+5,0,team)
                                                                coordinate_that_Im_watching = Coordinate(k+5,0,None,None,None)
                                                                fake_piece_moves = []
                                                                x = watch_up_left(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                x = watch_up(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                x = watch_up_right(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                x = watch_knight(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                for move in fake_piece_moves:
                                                                    if(move.move_type == "Capture"):
                                                                        opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves_check(chessboard)
                                                                        for opponent_piece_move in opponent_piece_moves:
                                                                            if(opponent_piece_move.column == coordinate_that_Im_watching.column and opponent_piece_move.row == coordinate_that_Im_watching.row):
                                                                                castling_flag = False
                                                            if (castling_flag == True):
                                                                if (type(piece) == King):
                                                                    castling = Coordinate(6,0,"kingside castling",i,j) 
                                                                    moves.append(castling)
                                                                elif(type(piece) == Tower):
                                                                    castling = Coordinate(5,0,"kingside castling",i,j)
                                                                    moves.append(castling)
            else:
                if(chessboard[4][7].piece != None):
                    if(type(chessboard[4][7].piece) == King):
                        if(chessboard[4][7].piece.team == team):
                            if(chessboard[4][7].piece.first_move_done == False):
                                if((i == 0 and j == 7) or (i == 4 and j == 7)):
                                    if(chessboard[0][7].piece != None):
                                        if(type(chessboard[0][7].piece) == Tower):
                                            if(chessboard[0][7].piece.team == team):
                                                if(chessboard[0][7].piece.first_move_done == False):
                                                    if(not(in_check(chessboard[4][7].piece,chessboard))):
                                                        if(chessboard[3][7].piece == None and chessboard[2][7].piece == None and chessboard[1][7].piece == None):
                                                            castling_flag = True
                                                            for k in range(2):
                                                                fake_square = Piece(k+2,7,team)
                                                                coordinate_that_Im_watching = Coordinate(k+2,7,None,None,None)
                                                                fake_piece_moves = []
                                                                x = watch_down_left(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                x = watch_down(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                x = watch_down_right(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                x = watch_knight(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                for move in fake_piece_moves:
                                                                    if(move.move_type == "Capture"):
                                                                        opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves_check(chessboard)
                                                                        for opponent_piece_move in opponent_piece_moves:
                                                                            if(opponent_piece_move.column == coordinate_that_Im_watching.column and opponent_piece_move.row == coordinate_that_Im_watching.row):
                                                                                castling_flag = False
                                                            if (castling_flag == True):
                                                                if (type(piece) == King):
                                                                    castling = Coordinate(2,7,"queenside castling",i,j)  
                                                                    moves.append(castling)                                            
                                                                elif(type(piece) == Tower):
                                                                    castling = Coordinate(3,7,"queenside castling",i,j)
                                                                    moves.append(castling)
                                if((i == 7 and j == 7) or (i == 4 and j == 7)):
                                    if(chessboard[7][7].piece != None):
                                        if(type(chessboard[7][7].piece) == Tower):
                                            if(chessboard[7][7].piece.team == team):
                                                if(chessboard[7][7].piece.first_move_done == False):
                                                    if(not(in_check(chessboard[4][7].piece,chessboard))):
                                                        if(chessboard[5][7].piece == None and chessboard[6][7].piece == None):
                                                            castling_flag = True
                                                            for k in range(2):
                                                                fake_square = Piece(k+5,7,team)
                                                                coordinate_that_Im_watching = Coordinate(k+5,7,None,None,None)
                                                                fake_piece_moves = []
                                                                x = watch_down_left(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                x = watch_down(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                x = watch_down_right(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                x = watch_knight(fake_square,chessboard)
                                                                if(x):
                                                                    fake_piece_moves.extend(x)
                                                                for move in fake_piece_moves:
                                                                    if(move.move_type == "Capture"):
                                                                        opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves_check(chessboard)
                                                                        for opponent_piece_move in opponent_piece_moves:
                                                                            if(opponent_piece_move.column == coordinate_that_Im_watching.column and opponent_piece_move.row == coordinate_that_Im_watching.row):
                                                                                castling_flag = False
                                                            if (castling_flag == True):
                                                                if (type(piece) == King):
                                                                    castling = Coordinate(6,7,"kingside castling",i,j)  
                                                                    moves.append(castling)
                                                                elif(type(piece) == Tower):
                                                                    castling = Coordinate(5,7,"kingside castling",i,j)
                                                                    moves.append(castling)
        return moves             
    else:
        print("ERROR: Neither king nor tower")

def watch_pawn(piece,chessboard):  # return the cordinate of the moves available for the pawn
    i = piece.column
    j = piece.row
    team = piece.team
    p = piece.first_move_done
    move = []
    if(piece.team == "White"):
        if(chessboard[i][j+1].piece == None):
            if(j == 6):
                x = Coordinate(i,7,"Promotion",i,j)
            else:
                x = Coordinate(i,j+1,None,i,j)
            move.append(x)
        if(i-1 > -1):
            if(chessboard[i-1][j+1].piece != None):
                if(chessboard[i-1][j+1].piece.team != team):
                    if(j == 6):
                        x = Coordinate(i-1,7,"Promoting_capture",i,j)
                    else:
                        x = Coordinate(i-1,j+1,"Capture",i,j)
                    move.append(x)
        if(i+1 < 8):
            if(chessboard[i+1][j+1].piece != None):
                if(chessboard[i+1][j+1].piece.team != team):
                    if(j == 6):
                        x = Coordinate(i+1,7,"Promoting_capture",i,j)
                    else:
                        x = Coordinate(i+1,j+1,"Capture",i,j)
                    move.append(x)
    else:
        if(chessboard[i][j-1].piece == None):
            if(j == 1):
                x = Coordinate(i,0,"Promotion",i,j)
            else:
                x = Coordinate(i,j-1,None,i,j)
            move.append(x)
        if(i-1 > -1):
            if(chessboard[i-1][j-1].piece != None):
                if(chessboard[i-1][j-1].piece.team != team):
                    if(j == 1):
                        x = Coordinate(i-1,0,"Promoting_capture",i,j)
                    else:
                        x = Coordinate(i-1,j-1,"Capture",i,j)
                    move.append(x)
        if(i+1 < 8):
            if(chessboard[i+1][j-1].piece != None):
                if(chessboard[i+1][j-1].piece.team != team):
                    if(j == 1):
                        x = Coordinate(i+1,0,"Promoting_capture",i,j)
                    else:
                        x = Coordinate(i+1,j-1,"Capture",i,j)
                    move.append(x)
    if (p == False and team == "White"):
        if(chessboard[i][j+1].piece == None and chessboard[i][j+2].piece == None):
            x=Coordinate(i,j+2,"double_pawn_advancement",i,j)
            move.append(x)
    elif (p == False and team == "Black"):
        if(chessboard[i][j-1].piece == None and chessboard[i][j-2].piece == None):
            x=Coordinate(i,j-2,"double_pawn_advancement",i,j)
            move.append(x)
    return move

def watch_enpassant(piece,chessboard,chessboard_log):  # return an array with the coordinate of the enpassant in case it's available otherwise None
    i = piece.column
    j = piece.row
    team = piece.team
    move = []
    if(chessboard_log):
        if(team == "White" and j == 4):
            if(i+1 < 8):
                if(type(chessboard[i+1][j].piece) == Pawn):
                    if(chessboard_log[-1].column == i+1 and chessboard_log[-1].row == j and chessboard_log[-1].move_type == "double_pawn_advancement"):
                        x = Coordinate(i+1,j+1,"en_passant",i,j)
                        move.append(x)
            if(i-1 > -1):
                if(type(chessboard[i-1][j].piece) == Pawn):
                    if(chessboard_log[-1].column == i-1 and chessboard_log[-1].row == j and chessboard_log[-1].move_type == "double_pawn_advancement"):
                        x = Coordinate(i-1,j+1,"en_passant",i,j)
                        move.append(x)
        if(team == "Black" and j == 3):
            if(i+1 < 8):
                if(type(chessboard[i+1][j].piece) == Pawn):
                    if(chessboard_log[-1].column == i+1 and chessboard_log[-1].row == j and chessboard_log[-1].move_type == "double_pawn_advancement"):
                        x = Coordinate(i+1,j-1,"en_passant",i,j)
                        move.append(x)
            if(i-1 > -1):
                if(type(chessboard[i-1][j].piece) == Pawn):
                    if(chessboard_log[-1].column == i-1 and chessboard_log[-1].row == j and chessboard_log[-1].move_type == "double_pawn_advancement"):
                        x = Coordinate(i-1,j-1,"en_passant",i,j)
                        move.append(x)
    return move

def watch_king(piece,chessboard):  # return an array with the coordinate of the possible moves of the king
    i = piece.column
    j = piece.row
    team = piece.team
    moves = []
    chessboard[i][j].piece = None
    chessboard[i][j].occupied = False
    if(i-1 > -1):
        for k in range(3):
            if(j-1+k > -1 and j-1+k < 8):  
                fake_square = Piece(i-1,j-1+k,team)                   # the fake squares are used to verify if the squares around the king are in check
                coordinate_Im_checking = Coordinate(i-1,j-1+k,None,None,None)
                fake_piece_moves = []                                                 
                piece_save = chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece
                if(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece != None):
                    if(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece.team != team):
                        chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = None 
                x = watch_up_left(fake_square,chessboard)
                if (x):
                    fake_piece_moves.extend(x)
                x = watch_up(fake_square,chessboard)
                if (x):
                    fake_piece_moves.extend(x)
                x = watch_up_right(fake_square,chessboard)
                if (x):
                    fake_piece_moves.extend(x)
                x = watch_right(fake_square,chessboard)
                if (x):
                    fake_piece_moves.extend(x)
                x = watch_down_right(fake_square,chessboard)
                if (x):
                    fake_piece_moves.extend(x)
                x = watch_down(fake_square,chessboard)
                if (x):
                    fake_piece_moves.extend(x)
                x = watch_down_left(fake_square,chessboard)
                if (x):
                    fake_piece_moves.extend(x)
                x = watch_left(fake_square,chessboard)
                if (x):
                    fake_piece_moves.extend(x)
                free_fake_square = True
                for move in fake_piece_moves:
                    if(move.move_type == "Capture"):
                        if(type(chessboard[move.column][move.row].piece) == King):
                            opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves(chessboard)
                            for opponent_piece_move in opponent_piece_moves:
                                if (coordinate_Im_checking.column == opponent_piece_move.column and coordinate_Im_checking.row == opponent_piece_move.row):
                                    free_fake_square = False
                        elif(type(chessboard[move.column][move.row].piece) == Pawn):
                            chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = fake_square
                            opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves_check(chessboard)
                            chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = piece_save
                            for opponent_piece_move in opponent_piece_moves:
                                if (coordinate_Im_checking.column == opponent_piece_move.column and coordinate_Im_checking.row == opponent_piece_move.row):
                                    free_fake_square = False
                        else:
                            opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves_check(chessboard)
                            for opponent_piece_move in opponent_piece_moves:
                                if (coordinate_Im_checking.column == opponent_piece_move.column and coordinate_Im_checking.row == opponent_piece_move.row):
                                    free_fake_square = False
                chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = piece_save
                if (free_fake_square == True):
                    if(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece == None):
                        x = Coordinate(fake_square.column,fake_square.row,None,i,j)
                        moves.append(x)
                    elif(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece.team != team):
                        x = Coordinate(fake_square.column,fake_square.row,"Capture",i,j)
                        moves.append(x)
    if(i+1 < 8):
        for k in range(3):
            if(j-1+k > -1 and j-1+k < 8):
                fake_square = Piece(i+1,j-1+k,team)
                coordinate_Im_checking = Coordinate(i+1,j-1+k,None,None,None)
                fake_piece_moves = []
                piece_save = chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece
                if(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece != None):
                    if(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece.team != team):
                        chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = None
                x = watch_up_left(fake_square,chessboard)
                if(x):
                    fake_piece_moves.extend(x)
                x = watch_up(fake_square,chessboard)
                if(x):
                    fake_piece_moves.extend(x)
                x = watch_up_right(fake_square,chessboard)
                if(x):
                    fake_piece_moves.extend(x)
                x = watch_right(fake_square,chessboard)
                if(x):
                    fake_piece_moves.extend(x)
                x = watch_down_right(fake_square,chessboard)
                if(x):
                    fake_piece_moves.extend(x)
                x = watch_down(fake_square,chessboard)
                if(x):
                    fake_piece_moves.extend(x)
                x = watch_down_left(fake_square,chessboard)
                if(x):
                    fake_piece_moves.extend(x)
                x = watch_left(fake_square,chessboard)
                if(x):
                    fake_piece_moves.extend(x)
                free_fake_square = True
                for move in fake_piece_moves:
                    if(move.move_type == "Capture"):
                        if(type(chessboard[move.column][move.row].piece) == King):
                            opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves(chessboard)
                            for opponent_piece_move in opponent_piece_moves:
                                if (coordinate_Im_checking.column == opponent_piece_move.column and coordinate_Im_checking.row == opponent_piece_move.row):
                                    free_fake_square = False
                        elif(type(chessboard[move.column][move.row].piece) == Pawn):
                            chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = fake_square
                            opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves_check(chessboard)
                            chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = piece_save
                            for opponent_piece_move in opponent_piece_moves:
                                if (coordinate_Im_checking.column == opponent_piece_move.column and coordinate_Im_checking.row == opponent_piece_move.row):
                                    free_fake_square = False
                        else:
                            opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves_check(chessboard)
                            for opponent_piece_move in opponent_piece_moves:
                                if (coordinate_Im_checking.column == opponent_piece_move.column and coordinate_Im_checking.row == opponent_piece_move.row):
                                    free_fake_square = False
                chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = piece_save
                if (free_fake_square == True):
                    if(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece == None):
                        x = Coordinate(fake_square.column,fake_square.row,None,i,j)
                        moves.append(x)
                    elif(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece.team != team):
                        x = Coordinate(fake_square.column,fake_square.row,"Capture",i,j)
                        moves.append(x)
    if(j-1 > -1):
        fake_square = Piece(i,j-1,team)
        coordinate_Im_checking = Coordinate(i,j-1,None,None,None)
        fake_piece_moves = []
        piece_save = chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece
        if(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece != None):
            if(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece.team != team):
                chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = None
        x = watch_up_left(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_up(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_up_right(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_right(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_down_right(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_down(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_down_left(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_left(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        free_fake_square = True
        for move in fake_piece_moves:
            if(move.move_type == "Capture"):
                if(type(chessboard[move.column][move.row].piece) == King):
                    opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves(chessboard)
                    for opponent_piece_move in opponent_piece_moves:
                        if (coordinate_Im_checking.column == opponent_piece_move.column and coordinate_Im_checking.row == opponent_piece_move.row):
                            free_fake_square = False
                elif(type(chessboard[move.column][move.row].piece) == Pawn):
                    chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = fake_square
                    opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves_check(chessboard)
                    chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = piece_save
                    for opponent_piece_move in opponent_piece_moves:
                        if (coordinate_Im_checking.column == opponent_piece_move.column and coordinate_Im_checking.row == opponent_piece_move.row):
                            free_fake_square = False
                else:
                    opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves_check(chessboard)
                    for opponent_piece_move in opponent_piece_moves:
                        if (coordinate_Im_checking.column == opponent_piece_move.column and coordinate_Im_checking.row == opponent_piece_move.row):
                            free_fake_square = False
        chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = piece_save
        if (free_fake_square == True):
            if(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece == None):
                x = Coordinate(fake_square.column,fake_square.row,None,i,j)
                moves.append(x)
            elif(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece.team != team):
                x = Coordinate(fake_square.column,fake_square.row,"Capture",i,j)
                moves.append(x)
    if(j+1 < 8):
        fake_square = Piece(i,j+1,team)
        coordinate_Im_checking = Coordinate(i,j+1,None,None,None)
        fake_piece_moves = []
        piece_save = chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece
        if(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece != None):
            if(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece.team != team):
                chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = None
        x = watch_up_left(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_up(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_up_right(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_right(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_down_right(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_down(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_down_left(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        x = watch_left(fake_square,chessboard)
        if(x):
            fake_piece_moves.extend(x)
        free_fake_square = True
        for move in fake_piece_moves:
            if(move.move_type == "Capture"):
                if(type(chessboard[move.column][move.row].piece) == King):
                    opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves(chessboard)
                    for opponent_piece_move in opponent_piece_moves:
                        if (coordinate_Im_checking.column == opponent_piece_move.column and coordinate_Im_checking.row == opponent_piece_move.row):
                            free_fake_square = False
                elif(type(chessboard[move.column][move.row].piece) == Pawn):
                    chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = fake_square
                    opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves_check(chessboard)
                    chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = piece_save
                    for opponent_piece_move in opponent_piece_moves:
                        if (coordinate_Im_checking.column == opponent_piece_move.column and coordinate_Im_checking.row == opponent_piece_move.row):
                            free_fake_square = False
                else:
                    opponent_piece_moves = chessboard[move.column][move.row].piece.possible_moves_check(chessboard)
                    for opponent_piece_move in opponent_piece_moves:
                        if (coordinate_Im_checking.column == opponent_piece_move.column and coordinate_Im_checking.row == opponent_piece_move.row):
                            free_fake_square = False
        chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece = piece_save
        if (free_fake_square == True):
            if(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece == None):
                x = Coordinate(fake_square.column,fake_square.row,None,i,j)
                moves.append(x)
            elif(chessboard[coordinate_Im_checking.column][coordinate_Im_checking.row].piece.team != team):
                x = Coordinate(fake_square.column,fake_square.row,"Capture",i,j)
                moves.append(x)
    chessboard[i][j].piece = piece
    chessboard[i][j].occupied = True
    return moves

def watch_check_defense(piece, coordinate_pieces_that_are_giving_check, chessboard):   # return an array with the coordinates of the moves to avoid the check (check all the pieces moves passing it just the king)
    i = piece.column
    j = piece.row
    team = piece.team
    move = []
    if(len(coordinate_pieces_that_are_giving_check)>1):
        x = watch_king(piece,chessboard)
        if(x):
            move.extend(x)
        return move
    elif(len(coordinate_pieces_that_are_giving_check) == 0):
        print("ERROR: pieces that are giving check array empty")
        return move
    else:
        iold = coordinate_pieces_that_are_giving_check[0].old_column
        jold = coordinate_pieces_that_are_giving_check[0].old_row
        if(type(chessboard[iold][jold].piece) == Knight or type(chessboard[iold][jold].piece) == Pawn or (i-iold == 1 and -2 < j-jold < 2) or (iold-i == 1 and -2 < j-jold < 2) or (i == iold and (j == jold+1 or j == jold-1))):
            x = watch_king(piece,chessboard)
            if(x):
                move.extend(x)
            return move
        else:
            coordinate_squares_for_defense = []   # find the squares between the piece giving check and the king
            if(i == iold):
                if(jold < j):
                    for p in range(j-jold-1):
                        x = Coordinate(i,jold+p+1,None,None,None)
                        coordinate_squares_for_defense.append(x)
                if(jold > j):
                    for p in range(jold-j-1):
                        x = Coordinate(i,jold-p-1,None,None,None)
                        coordinate_squares_for_defense.append(x)
            elif(j == jold):
                if(iold < i):
                    for p in range(i-iold-1):
                        x = Coordinate(iold+p+1,j,None,None,None)
                        coordinate_squares_for_defense.append(x)
                if(iold > i):
                    for p in range(iold-i-1):
                        x = Coordinate(iold-p-1,j,None,None,None)
                        coordinate_squares_for_defense.append(x)
            elif(iold > i):
                if(jold > j):
                    for p in range(iold-i-1):
                        x = Coordinate(iold-p-1,jold-p-1,None,None,None)
                        coordinate_squares_for_defense.append(x)
                if(jold < j):
                    for p in range(iold-i-1):
                        x = Coordinate(iold-p-1,jold+p+1,None,None,None)
                        coordinate_squares_for_defense.append(x)
            elif(iold < i):
                if(jold > j):
                    for p in range(i-iold-1):
                        x = Coordinate(iold+p+1,jold-p-1,None,None,None)
                        coordinate_squares_for_defense.append(x)
                if(jold < j):
                    for p in range(i-iold-1):
                        x = Coordinate(iold+p+1,jold+p+1,None,None,None)
                        coordinate_squares_for_defense.append(x)
            else:
                print("ERROR: piece in an unexpcted position, whatch check defense")
            for a in range(8):                                   # watch if any pieces not pinned can move in those squares 
                for b in range(8):
                    if(chessboard[a][b].piece != None):
                        if(chessboard[a][b].piece.team == team):
                            if(type(chessboard[a][b].piece) != King):
                                if(not(pinned(chessboard[a][b].piece,chessboard))):
                                    x = chessboard[a][b].piece.possible_moves_check(chessboard)
                                    if(x):
                                        for c in x:
                                            for square_coordinate in coordinate_squares_for_defense:
                                                if(c.column == square_coordinate.column and c.row == square_coordinate.row):
                                                    y = Coordinate(c.column,c.row,None,a,b)
                                                    move.append(y)
        x = watch_king(piece,chessboard)
        if (x):
            move.extend(x)
        return move

def watch_pinned(piece,chessboard):   # return the coordinate of the moves available when the piece passed in the function is pinned  
    i = piece.column
    j = piece.row
    team = piece.team
    king = king_position(team,chessboard)
    move = []
    moves_coordinate = chessboard[i][j].piece.possible_moves_check(chessboard)
    chessboard[i][j].piece = None
    chessboard[i][j].occupied = False
    for move_coordinate in  moves_coordinate:
        if(move_coordinate.move_type == "Capture" or move_coordinate.move_type == "Promoting_capture"):
            salvataggio_pezzo_mangiato = chessboard[move_coordinate.column][move_coordinate.row].piece
            chessboard[move_coordinate.column][move_coordinate.row].piece = piece
            piece_giving_check_after = in_check(king,chessboard)
            if(len(piece_giving_check_after) == 0):
                move.append(move_coordinate)
            chessboard[move_coordinate.column][move_coordinate.row].piece = salvataggio_pezzo_mangiato
        else:
            chessboard[move_coordinate.column][move_coordinate.row].piece = piece
            chessboard[move_coordinate.column][move_coordinate.row].occupied = True
            piece_giving_check_after = in_check(king,chessboard)
            if(len(piece_giving_check_after) == 0):
                move.append(move_coordinate)
            chessboard[move_coordinate.column][move_coordinate.row].piece = None
            chessboard[move_coordinate.column][move_coordinate.row].occupied = False
    chessboard[i][j].piece = piece
    chessboard[i][j].occupied = True
    return move
    
def watch_stall(team,chessboard):   # return true or false if there are none available moves and the king is not in check
    move = []
    for i in range(8):
        for j in range(8):
            if(chessboard[i][j].piece != None):
                if(chessboard[i][j].piece.team == team):
                    if(type(chessboard[i][j].piece) != King):
                        x = chessboard[i][j].piece.possible_moves_check(chessboard)
                        if (x):
                            move.extend(x)
                    else:
                        x = chessboard[i][j].piece.possible_moves(chessboard)
                        if (x):
                            move.extend(x)
    if(len(move) == 0):
        return True
    else:
        return False

def from_input_to_coordinate(input):   # return the the array coordinate from the algebraic notation
    if(len(input) == 2):  
        letter = input[0]   
        letter = letter.upper()
        if(letter.isalpha()):
            position = ord(letter) - ord('A')
            if(-1 < position < 8):
                pass
            else:
                return None
        else:
            return None
        number = input[1]   
        if(number.isdigit()):
            number = int(number)
            if(0 < number < 9 ):
                number = number -1
            else:
                return None
        else:
            return None
        x = Coordinate(position,number,None,None,None)
        return x
    else:
        return None

def check_mate(chessboard):   # return true if there is a check mate in both the team
    White_king = king_position("White",chessboard)
    Black_king = king_position("Black",chessboard)
    x = chessboard[White_king.column][White_king.row].piece.possible_moves(chessboard)
    if(in_check(White_king,chessboard) and not(x)):
        return True
    x = chessboard[Black_king.column][Black_king.row].piece.possible_moves(chessboard)
    if(in_check(Black_king,chessboard) and not(x)):
        return True

# definition and initialization chessboard

class Coordinate:
    def __init__(self,column,row,move_type,old_column,old_row):
        self.column = column
        self.row = row
        self.move_type = move_type
        self.old_column = old_column
        self.old_row = old_row

class Square: #Non Davide
    def __init__(self, piece, column, row, occupied):
        self.piece=piece
        self.column=column
        self.row=row
        self.occupied=occupied

def initialization_chessboard():  # create the double array and insert al the pieces of the chessboard
    chessboard = []
    for i in range(8):
        n = []
        for j in range(8):
            n.insert(i,0)
        chessboard.append(n)

    i = 0
    while(i<8):
        if(i == 0):
            chessboard[0][0] = Square(Tower(0,0,"White",False),0,0,True)
            chessboard[1][0] = Square(Knight(1,0,"White"),1,0,True)
            chessboard[2][0] = Square(Bishop(2,0,"White"),2,0,True)
            chessboard[3][0] = Square(Queen(3,0,"White"),3,0,True)
            chessboard[4][0] = Square(King(4,0,"White",False, False),4,0,True)
            chessboard[5][0] = Square(Bishop(5,0,"White"),5,0,True)
            chessboard[6][0] = Square(Knight(6,0,"White"),6,0,True)
            chessboard[7][0] = Square(Tower(7,0,"White",False),7,0,True)

        elif(i == 1):
            j = 0
            while(j<8):
                chessboard[j][1] = Square(Pawn(j,1,"White",False,False),j,1,True)
                j = j+1
        
        elif(i == 6):
            j = 0
            while(j<8):
                chessboard[j][6] = Square(Pawn(j,6,"Black",False,False),j,6,True)
                j = j+1
        
        elif(i == 7):
            chessboard[0][7] = Square(Tower(0,7,"Black",False),0,7,True)
            chessboard[1][7] = Square(Knight(1,7,"Black"),1,7,True)
            chessboard[2][7] = Square(Bishop(2,7,"Black"),2,7,True)
            chessboard[3][7] = Square(Queen(3,7,"Black"),3,7,True)
            chessboard[4][7] = Square(King(4,7,"Black",False, False),4,7,True)
            chessboard[5][7] = Square(Bishop(5,7,"Black"),5,7,True)
            chessboard[6][7] = Square(Knight(6,7,"Black"),6,7,True)
            chessboard[7][7] = Square(Tower(7,7,"Black",False),7,7,True)

        else:
            j = 0
            while(j<8):
                chessboard[j][i] = Square(None,j,i,False)
                j = j+1

        i = i+1

    return chessboard

def initialization_test_chessboard():   # test chessboard used for testing the program
    chessboard = []
    for i in range(8):
        n = []
        for j in range(8):
            n.insert(i,0)
        chessboard.append(n)

    i = 0
    while(i<8):
        j = 0
        while(j<8):
            chessboard[j][i] = Square(None,j,i,False)
            j = j+1
        i = i+1

    chessboard[0][3] = Square(Tower(0,3,"Black",True),0,3,True)
    chessboard[5][5] = Square(Pawn(5,5,"Black",True,False),5,5,True)
    chessboard[6][6] = Square(Pawn(6,6,"Black",False,False),6,6,True)
    chessboard[4][4] = Square(Pawn(4,4,"White",True,False),4,4,True)
    #chessboard[7][6] = Square(Tower(7,6,"White",False),7,6,True)
    chessboard[5][4] = Square(King(5,4,"White",False,True),5,4,True)
    chessboard[5][6] = Square(King(5,6,"Black",False,True),5,6,True)

    return chessboard

def chessboard_print(chessboard):  # print the chessboard
    for i in range(8):  
        print("---------------------------------")      # for divide the row
        row = "|{}|{}|{}|{}|{}|{}|{}|{}| {}."
        piecesarray = []
        for j in range(8):  
            if(chessboard[j][7-i].occupied == True):
                letter = chessboard[j][7-i].piece.print_letter()
                if(chessboard[j][7-i].piece.team == "White"):
                    piecesarray.append(" "+letter+" ")
                elif(chessboard[j][7-i].piece.team == "Black"):
                    piecesarray.append("'"+letter+"'")     # with '' for the black pieces
                else:
                    print("ERROR: Team neither White nor Black")
            elif(chessboard[j][7-i].occupied == False):
                piecesarray.append("   ")
            else:
                print("ERROR: chessboard not printed successfully")
        print(row.format(piecesarray[0],piecesarray[1],piecesarray[2],piecesarray[3],piecesarray[4],piecesarray[5],piecesarray[6],piecesarray[7],8-i))
    print("---------------------------------")
    print("  A   B   C   D   E   F   G   H  ")

# functions to move the pieces

def move_piece(coordinate,chessboard):   # for every move type except promotion there is an if for make that type of move
    old_column = coordinate.old_column
    old_row = coordinate.old_row
    new_column = coordinate.column
    new_row = coordinate.row
    piece = type(chessboard[old_column][old_row].piece)
    team = chessboard[old_column][old_row].piece.team
    if (coordinate.move_type == "queenside castling"):
        chessboard[new_column][new_row].piece = chessboard[old_column][old_row].piece
        chessboard[old_column][old_row].piece.column = new_column
        chessboard[old_column][old_row].piece.row = new_row
        chessboard[old_column][old_row].piece.first_move_done = True
        chessboard[old_column][old_row].piece = None
        chessboard[old_column][old_row].occupied = False
        chessboard[new_column][new_row].occupied = True
        if(piece == King):
            if(team == "White"):
                chessboard[3][0].piece = chessboard[0][0].piece
                chessboard[0][0].piece.column = 3
                chessboard[0][0].piece.row = 0
                chessboard[0][0].piece.first_move_done = True
                chessboard[0][0].piece = None
                chessboard[0][0].occupied = False
                chessboard[3][0].occupied = True
            else:
                chessboard[3][7].piece = chessboard[0][7].piece
                chessboard[0][7].piece.column = 3
                chessboard[0][7].piece.row = 7
                chessboard[0][7].piece.first_move_done = True
                chessboard[0][7].piece = None
                chessboard[0][7].occupied = False
                chessboard[3][7].occupied = True
        if(piece == Tower):
            if(team == "White"):
                chessboard[2][0].piece = chessboard[4][0].piece
                chessboard[4][0].piece.column = 2
                chessboard[4][0].piece.row = 0
                chessboard[4][0].piece.first_move_done = True
                chessboard[4][0].piece = None
                chessboard[4][0].occupied = False
                chessboard[2][0].occupied = True
            else:
                chessboard[2][7].piece = chessboard[4][7].piece
                chessboard[4][7].piece.column = 2
                chessboard[4][7].piece.row = 7
                chessboard[4][7].piece.first_move_done = True
                chessboard[4][7].piece = None
                chessboard[4][7].occupied = False
                chessboard[2][7].occupied = True
    elif (coordinate.move_type == "kingside castling"):
        chessboard[new_column][new_row].piece = chessboard[old_column][old_row].piece
        chessboard[old_column][old_row].piece.column = new_column
        chessboard[old_column][old_row].piece.row = new_row
        chessboard[old_column][old_row].piece.first_move_done = True
        chessboard[old_column][old_row].piece = None
        chessboard[old_column][old_row].occupied = False
        chessboard[new_column][new_row].occupied = True
        if(piece == King):
            if(team == "White"):
                chessboard[5][0].piece = chessboard[7][0].piece
                chessboard[7][0].piece.column = 5
                chessboard[7][0].piece.row = 0
                chessboard[7][0].piece.first_move_done = True
                chessboard[7][0].piece = None
                chessboard[7][0].occupied = False
                chessboard[5][0].occupied = True
            else:
                chessboard[5][7].piece = chessboard[7][7].piece
                chessboard[7][7].piece.column = 5
                chessboard[7][7].piece.row = 7
                chessboard[7][7].piece.first_move_done = True
                chessboard[7][7].piece = None
                chessboard[7][7].occupied = False
                chessboard[5][7].occupied = True
                
        if(piece == Tower):
            if(team == "White"):
                chessboard[6][0].piece = chessboard[4][0].piece
                chessboard[4][0].piece.column = 6
                chessboard[4][0].piece.row = 0
                chessboard[4][0].piece.first_move_done = True
                chessboard[4][0].piece = None
                chessboard[4][0].occupied = False
                chessboard[6][0].occupied = True
            else:
                chessboard[6][7].piece = chessboard[4][7].piece
                chessboard[4][7].piece.column = 6
                chessboard[4][7].piece.row = 7
                chessboard[4][7].piece.first_move_done = True
                chessboard[4][7].piece = None
                chessboard[4][7].occupied = False
                chessboard[6][7].occupied = True
    elif (coordinate.move_type == "en_passant"):
        chessboard[new_column][new_row].piece = chessboard[old_column][old_row].piece
        chessboard[old_column][old_row].piece.column = new_column
        chessboard[old_column][old_row].piece.row = new_row
        chessboard[old_column][old_row].piece = None
        chessboard[old_column][old_row].occupied = False
        chessboard[new_column][new_row].occupied = True
        if(team == "White"):
            chessboard[new_column][new_row-1].piece = None
            chessboard[new_column][new_row-1].occupied = False
        if(team == "Black"):
            chessboard[new_column][new_row+1].piece = None
            chessboard[new_column][new_row+1].occupied = False
    elif (coordinate.move_type == "Capture"):
        chessboard[new_column][new_row].piece = chessboard[old_column][old_row].piece
        chessboard[old_column][old_row].piece.column = new_column
        chessboard[old_column][old_row].piece.row = new_row
        if(type(chessboard[new_column][new_row].piece) == Pawn or type(chessboard[new_column][new_row].piece) == Tower or type(chessboard[new_column][new_row].piece) == King):
            chessboard[old_column][old_row].piece.first_move_done = True
        chessboard[old_column][old_row].piece = None
        chessboard[old_column][old_row].occupied = False
    elif (coordinate.move_type == None or coordinate.move_type == "double_pawn_advancement"):
        chessboard[new_column][new_row].piece = chessboard[old_column][old_row].piece
        chessboard[old_column][old_row].piece.column = new_column
        chessboard[old_column][old_row].piece.row = new_row
        if(type(chessboard[new_column][new_row].piece) == Pawn or type(chessboard[new_column][new_row].piece) == Tower or type(chessboard[new_column][new_row].piece) == King):
            chessboard[old_column][old_row].piece.first_move_done = True
        chessboard[old_column][old_row].piece = None
        chessboard[old_column][old_row].occupied = False
        chessboard[new_column][new_row].occupied = True
    else:
        print("ERRORE: move type not exist")
    chessboard_log.append(coordinate)
    
def move_piece_promotion(coordinate,chessboard,promotion_piece):  # for the promotion of the pawn 
    old_column = coordinate.old_column
    old_row = coordinate.old_row
    new_column = coordinate.column
    new_row = coordinate.row
    team = chessboard[old_column][old_row].piece.team
    if (coordinate.move_type == "Promotion" or coordinate.move_type == "Promoting_capture"):
        if (promotion_piece == "T"):
            promoved_piece = Tower(new_column,new_row,team,True)
        if (promotion_piece == "C"):
            promoved_piece = Knight(new_column,new_row,team)
        if (promotion_piece == "A"):
            promoved_piece = Bishop(new_column,new_row,team)
        if (promotion_piece == "D"):
            promoved_piece = Queen(new_column,new_row,team)
        chessboard[new_column][new_row].piece = promoved_piece
        chessboard[new_column][new_row].occupied = True
        chessboard[old_column][old_row].piece = None
        chessboard[old_column][old_row].occupied = False
    else:
        print("ERRORE: not promotion movetype in promotion function")
    chessboard_log.append(coordinate)

def print_coordinate(coordinate,index):  # print the coordinate in the algebraic notation from the array of coordinates returned by the functions
    old_column = coordinate.old_column
    old_row = coordinate.old_row
    new_column = coordinate.column
    new_row = coordinate.row
    old_column = chr(ord('A')+old_column)
    old_row = old_row+1
    new_column = chr(ord('A')+new_column)
    new_row = new_row + 1
    if(coordinate.move_type == "queenside castling"):
        print(f"{index}) {old_column}{old_row} -> 0-0-0")
    elif(coordinate.move_type == "kingside castling"):
        print(f"{index}) {old_column}{old_row} -> 0-0")
    elif(coordinate.move_type == "en_passant"):
        print(f"{index}) {old_column}{old_row} -> {new_column}{new_row} e.p.")
    elif(coordinate.move_type == "Promotion"):
        print(f"{index}) {old_column}{old_row} -> {new_column}{new_row} Promotion")
    elif(coordinate.move_type == "Promoting_capture"):
        print(f"{index}) {old_column}{old_row} -> {new_column}{new_row}x Promotion")
    elif(coordinate.move_type == "Capture"):
        print(f"{index}) {old_column}{old_row} -> {new_column}{new_row}x")
    else:
        print(f"{index}) {old_column}{old_row} -> {new_column}{new_row}")

def existing_coordinate_position(coordinate,team,chessboard):   # check if the coordinates gived by the user are correct
    if(coordinate != None):
        column = coordinate.column
        row = coordinate.row
        if(chessboard[column][row].piece != None):
            if(chessboard[column][row].piece.team == team):
                return True
        else:
            return False
    else:
        return False

def existing_coordinate_move (number,move):   # check if the number of the move choosed by the user is correct
    if(number):
        try:
            n = int(number)
            l = len(move)
            if(-1 < n <= l):
                return True
            else:
                return False
        except:
            return False

def Promotion():   # ask the user in which piece he/she want to promote
    print("0 for go back")
    k = input("Choose the piece you want to promote in\nR - K - B - Q\n")
    if(k == "R" or k == "K" or k == "B" or k == "Q" or k == 0):
        return k
    else:
        while (not(k == "R" or k == "K" or k == "B" or k == "Q" or k == 0)):
                print("ERRORE: wrong piece")
                print("0 for go back")
                k = input("Choose the piece you want to promote in\nR - K - B - Q\n")
        return k


