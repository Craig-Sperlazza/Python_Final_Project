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
        self._white_is_in_check = False

        #####We now initialize the piece objects and place on list##############

        ########################################################################
        ####################   RED PIECES  #####################################
        ########################################################################

        ####################   RED ROOKS   #####################################
        red_rook1 = Piece('rR', 'red', 'rook', 'a1')
        str_coord = 'a1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_rook1 #have to do y first because nested list

        red_rook2 = Piece('rR', 'red', 'rook', 'i1')
        str_coord = 'i1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_rook2  #have to do y first because nested list

        ####################   RED KNIGHTS/HORSES  #############################
        red_knight1 = Piece('rN', 'red', 'knight', 'b1')
        str_coord = 'b1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_knight1  #have to do y first because nested list

        red_knight2 = Piece('rN', 'red', 'knight', 'h1')
        str_coord = 'h1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_knight2  #have to do y first because nested list

        ####################   RED BISHOPS/ELEPHANTS  ##########################
        red_bishop1 = Piece('rB', 'red', 'bishop', 'c1')
        str_coord = 'c1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_bishop1  #have to do y first because nested list

        red_bishop2 = Piece('rB', 'red', 'bishop', 'g1')
        str_coord = 'g1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_bishop2  #have to do y first because nested list

        ####################   RED GUARDS   ####################################
        red_guard1 = Piece('rG', 'red', 'guard', 'd1')
        str_coord = 'd1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_guard1  # have to do y first because nested list

        red_guard2 = Piece('rG', 'red', 'guard', 'f1')
        str_coord = 'f1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_guard2  # have to do y first because nested list

        ####################   RED KING    #####################################
        red_king = Piece('rK', 'red', 'king', 'e1')
        str_coord = 'e1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_king  # have to do y first because nested list


        ####################   RED CANONS   ####################################
        red_canon1 = Piece('rC', 'red', 'canon', 'b3')
        str_coord = 'b3'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_canon1  # have to do y first because nested list

        red_canon2 = Piece('rC', 'red', 'canon', 'h3')
        str_coord = 'h3'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_canon2  # have to do y first because nested list

        ####################   RED PAWNS   #####################################
        red_pawn1 = Piece('rP', 'red', 'pawn', 'a4')
        str_coord = 'a4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn1  # have to do y first because nested list

        red_pawn2 = Piece('rP', 'red', 'pawn', 'c4')
        str_coord = 'c4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn2  # have to do y first because nested list

        red_pawn3 = Piece('rP', 'red', 'pawn', 'e4')
        str_coord = 'e4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn3  # have to do y first because nested list

        red_pawn4 = Piece('rP', 'red', 'pawn', 'g4')
        str_coord = 'g4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn4  # have to do y first because nested list

        red_pawn5 = Piece('rP', 'red', 'pawn', 'i4')
        str_coord = 'i4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn5  # have to do y first because nested list
        """
        initial = [['G', 'red', 'e1'], ['G', 'black', 'e10'],
                   ['A', 'red', 'd1'], ['A', 'red', 'f1'],
                   ['A', 'black', 'd10'], ['A', 'black', 'f10'],
                   ['E', 'red', 'c1'], ['E', 'red', 'g1'],
                   ['E', 'black', 'c10'], ['E', 'black', 'g10'],
                   ['H', 'red', 'b1'], ['H', 'red', 'h1'],
                   ['H', 'black', 'b10'], ['H', 'black', 'h10'],
                   ['R', 'red', 'a1'], ['R', 'red', 'i1'],
                   ['R', 'black', 'a10'], ['R', 'black', 'i10'],
                   ['C', 'red','b3'], ['C', 'red', 'h3'],
                   ['C', 'black', 'b8'], ['C', 'black', 'h8'],
                   ['S', 'red', 'a4'], ['S', 'red', 'c4'],
                   ['S', 'red', 'e4'], ['S', 'red', 'g4'],
                   ['S', 'red', 'i4'], ['S', 'black', 'a7'],
                   ['S', 'black', 'c7'], ['S', 'black', 'e7'],
                   ['S', 'black', 'g7'], ['S', 'black', 'i7']]
        for obj in range(len(initial)):
            title = initial[obj][0]
            color = initial[obj][1]
            position = initial[obj][2]
            piece = Piece(title, color, position)
            x_coord = self.find_coord(position)[0]
            y_coord = self.find_coord(position)[1]
            # print(title, color, position)
            # print(x_coord, y_coord)
            self._board[y_coord][x_coord] = piece
        """

    def get_red_move(self):
        return self.get_red_move()

    def set_red_move(self):
        if self._red_move == True:
            self._red_move = False
        else:
            self._red_move = True

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

        if str_pos[1] == '1':
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
        print("   A   B   C   D   E   F   G   H  I")

    #def set_board(self, x_coord, y_coord, piece):



class Piece:
    def __init__(self, title, color, type, position = None):
        self._title = title
        self._color = color
        self._type = type
        self._position = position

    def __repr__(self):   # operator overload to print piece on board
        return self._title
        """
        if self._color == 'red':
            return "\033[1;31;48m" + self._title + ' ' + "\033[1;37;48m" # red
        return "\033[1;32;48m" + self._title + ' ' + "\033[1;37;48m" # black
        """

    def get_title(self):
        return self._title

    def get_color(self):
        return self._color

class Cannon(Piece):
    def __init__(self, color, position):
        super().__init__(color)
        super().__init__(position)


# red = Piece('red')
# cannon1 = Cannon(red, 'b3')
# cannon2 = Cannon(red, 'h3')
game = XiangqiGame()
# game._board[2][3]=cannon1
# print(game._board[2][3])
# print(game.get_board())
game.get_board()