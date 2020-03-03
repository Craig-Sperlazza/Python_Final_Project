from typing import List, Optional, Any

# Portfolio Project
# Author: Craig Sperlazza
# Date: 2/26/2020
# Description: Creates

class XiangqiGame:
    """Class named..."""

    def __init__(self):
        """Initializes a board as a list made of ten list elements, all of
        which are initially set as an empty string.
         The init function also creates and sets the current state of the game to UNFINISHED"""
        self._board = [["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],]
        self._red_move = True
        self._game_state = "UNFINISHED"
        self._is_in_check = False
        self._black_is_in_check = False
        self._red_is_in_check = False

        def get_game_state(self):
            """Method that returns the current state of the game,
            which is one of three states RED_WON, BLACK_WON, or UNFINISHED"""
            return self._game_state

        def set_game_state(self, color):
            if color == "BLACK":
                self._game_state = "BLACK_WON"
            elif color == "RED":
                self._game_state = "RED_WON"

        def get_red_move(self):
            return self.get_red_move()

        def set_red_move(self):
            if self._red_move == True:
                self._red_move = False
            else:
                self._red_move = True

        def make_move(self, begin_coord, end_coord):


        #####We now initialize the piece objects and place on Board##############

        ########################################################################
        ####################   RED PIECES  #####################################
        ########################################################################

        ####################   RED ROOKS   #####################################
        red_rook1 = Piece('RR', 'red', 'rook', 'a1')
        str_coord = 'a1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_rook1 #have to do y first because nested list

        red_rook2 = Piece('RR', 'red', 'rook', 'i1')
        str_coord = 'i1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_rook2  #have to do y first because nested list

        ####################   RED KNIGHTS/HORSES  #############################
        red_knight1 = Piece('RN', 'red', 'knight', 'b1')
        str_coord = 'b1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_knight1  #have to do y first because nested list

        red_knight2 = Piece('RN', 'red', 'knight', 'h1')
        str_coord = 'h1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_knight2  #have to do y first because nested list

        ####################   RED BISHOPS/ELEPHANTS  ##########################
        red_bishop1 = Piece('RB', 'red', 'bishop', 'c1')
        str_coord = 'c1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_bishop1  #have to do y first because nested list

        red_bishop2 = Piece('RB', 'red', 'bishop', 'g1')
        str_coord = 'g1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_bishop2  #have to do y first because nested list

        ####################   RED GUARDS   ####################################
        red_guard1 = Piece('RG', 'red', 'guard', 'd1')
        str_coord = 'd1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_guard1  # have to do y first because nested list

        red_guard2 = Piece('RG', 'red', 'guard', 'f1')
        str_coord = 'f1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_guard2  # have to do y first because nested list

        ####################   RED KING    #####################################
        red_king = Piece('RK', 'red', 'king', 'e1')
        str_coord = 'e1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_king  # have to do y first because nested list


        ####################   RED CANONS   ####################################
        red_canon1 = Piece('RC', 'red', 'canon', 'b3')
        str_coord = 'b3'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_canon1  # have to do y first because nested list

        red_canon2 = Piece('RC', 'red', 'canon', 'h3')
        str_coord = 'h3'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_canon2  # have to do y first because nested list

        ####################   RED PAWNS   #####################################
        red_pawn1 = Piece('RP', 'red', 'pawn', 'a4')
        str_coord = 'a4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn1  # have to do y first because nested list

        red_pawn2 = Piece('RP', 'red', 'pawn', 'c4')
        str_coord = 'c4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn2  # have to do y first because nested list

        red_pawn3 = Piece('RP', 'red', 'pawn', 'e4')
        str_coord = 'e4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn3  # have to do y first because nested list

        red_pawn4 = Piece('RP', 'red', 'pawn', 'g4')
        str_coord = 'g4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn4  # have to do y first because nested list

        red_pawn5 = Piece('RP', 'red', 'pawn', 'i4')
        str_coord = 'i4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn5  # have to do y first because nested list

        ########################################################################
        ####################   BLACK PIECES  #####################################
        ########################################################################

        ####################   BLACK ROOKS   #####################################
        black_rook1 = Piece('BR', 'black', 'rook', 'a10')
        str_coord = 'a10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_rook1  # have to do y first because nested list

        black_rook2 = Piece('BR', 'black', 'rook', 'i10')
        str_coord = 'i10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_rook2  # have to do y first because nested list

        ####################   BLACK KNIGHTS/HORSES  #############################
        black_knight1 = Piece('BN', 'black', 'knight', 'b10')
        str_coord = 'b10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_knight1  # have to do y first because nested list

        black_knight2 = Piece('BN', 'black', 'knight', 'h10')
        str_coord = 'h10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_knight2  # have to do y first because nested list

        ####################   BLACK BISHOPS/ELEPHANTS  ##########################
        black_bishop1 = Piece('BB', 'black', 'bishop', 'c10')
        str_coord = 'c10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_bishop1  # have to do y first because nested list

        black_bishop2 = Piece('BB', 'black', 'bishop', 'g10')
        str_coord = 'g10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_bishop2  # have to do y first because nested list

        ####################   BLACK GUARDS   ####################################
        black_guard1 = Piece('BG', 'black', 'guard', 'd10')
        str_coord = 'd10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_guard1  # have to do y first because nested list

        black_guard2 = Piece('BG', 'black', 'guard', 'f10')
        str_coord = 'f10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_guard2  # have to do y first because nested list

        ####################   BLACK KING    #####################################
        black_king = Piece('BK', 'black', 'king', 'e10')
        str_coord = 'e10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_king  # have to do y first because nested list

        ####################   BLACK CANONS   ####################################
        black_canon1 = Piece('BC', 'black', 'canon', 'b8')
        str_coord = 'b8'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_canon1  # have to do y first because nested list

        black_canon2 = Piece('BC', 'black', 'canon', 'h8')
        str_coord = 'h8'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_canon2  # have to do y first because nested list

        ####################   BLACK PAWNS   #####################################
        black_pawn1 = Piece('BP', 'black', 'pawn', 'a7')
        str_coord = 'a7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn1  # have to do y first because nested list

        black_pawn2 = Piece('BP', 'black', 'pawn', 'c7')
        str_coord = 'c7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn2  # have to do y first because nested list

        black_pawn3 = Piece('BP', 'black', 'pawn', 'e7')
        str_coord = 'e7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn3  # have to do y first because nested list

        black_pawn4 = Piece('BP', 'black', 'pawn', 'g7')
        str_coord = 'g7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn4  # have to do y first because nested list

        black_pawn5 = Piece('BP', 'black', 'pawn', 'i7')
        str_coord = 'i7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn5  # have to do y first because nested list


    def convert_coord(self, str_pos):
        """
        Method to convert string move to a list of integer coordinates on board.
        param: string value representing 'xy' coordinates
        returns: list of integers [x, y] coordinates
        """
        x = 0
        y = 0

        if str_pos[0] == 'a':
            x = 0
        elif str_pos[0] == 'b':
            x = 1
        elif str_pos[0] == 'c':
            x = 2
        elif str_pos[0] == 'd':
            x = 3
        elif str_pos[0] == 'e':
            x = 4
        elif str_pos[0] == 'f':
            x = 5
        elif str_pos[0] == 'g':
            x = 6
        elif str_pos[0] == 'h':
            x = 7
        elif str_pos[0] == 'i':
            x = 8

        if str_pos[1] == '1' and len(str_pos) == 3:
            y = 0
            #elif len(str_pos)< 2:
        elif str_pos[1] == '1' and len(str_pos) < 3:
            y = 9
        elif str_pos[1] == '2':
            y = 8
        elif str_pos[1] == '3':
            y = 7
        elif str_pos[1] == '4':
            y = 6
        elif str_pos[1] == '5':
            y = 5
        elif str_pos[1] == '6':
            y = 4
        elif str_pos[1] == '7':
            y = 3
        elif str_pos[1] == '8':
            y = 2
        elif str_pos[1] == '9':
            y = 1
        return [x, y]
        # new = [x, y]
        # print(new)

    def get_board(self):
        """return the board in a 9x10 grid"""
        x = 10
        for item in self._board:
            # print(x)
            print(x, item)
            x -= 1
        print("   A   B   C   D   E   F   G   H   I")

    #def set_board(self, x_coord, y_coord, piece):





class Piece:
    def __init__(self, title, color, type, position = None):
        self._title = title
        self._color = color
        self._type = type
        self._position = position

    def __repr__(self):   #print piece on board instead of object reference
        return self._title

    def get_title(self):
        return self._title

    def get_color(self):
        return self._color

    def get_type(self):
        return self._color

    def get_position(self):
        return self._position

class Cannon(Piece):
    def __init__(self, title, color, type, position = None, board = XiangqiGame.get_board):
        super().__init__(title, color, type, position)
        self._board = board

    #def


# red = Piece('red')
# cannon1 = Cannon(red, 'b3')
# cannon2 = Cannon(red, 'h3')
game = XiangqiGame()
# game._board[2][3]=cannon1
# print(game._board[2][3])
# print(game.get_board())
game.get_board()

new = Cannon()
new.get_board()