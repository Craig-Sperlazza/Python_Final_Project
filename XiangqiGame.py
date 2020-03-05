from typing import List, Optional, Any

# Portfolio Project
# Author: Craig Sperlazza
# Date: 2/26/2020
# Description: Creates

class XiangqiGame:
    """Class named XiangiGame which initializes the Game and Board. INSERT
    DESCRIPTION HERE.
    Data Members:
        The board which is initialized as a list with 10 nested lists and
            each nested list is initialized as 9 empty strings.
            This creates the 10x9 board
        A move data member. This will track whose turn it is (red or black)
        A game state data member initialized to UNFINISHED and the possible
            states of RED_WON, BLACK_WON, or UNFINISHED"
        A data member named is_in_check which is set to False
            and updated if the King is in check.
        A count data member initialized to one.
            This will be used to keep track of the count of moves.
    Methods:
        Get and set methods for each of the data members
        The Game class also calls the subclasses to initialize
            each piece object into the board.
        Convert coordinates method:
            This will take the string coordinates given and convert them to
            integers to use as list coordinates.
        Print board method: prints the board in readable format.

        Make move method
            Takes a current location and next location as parameter
            Converts this to integers to use as list coordinates
            Validate that it is a legal move
            Check that the position has a piece
            That if it is red’s turn, red is moving a red piece, etc.
            Then it will call a method in the piece subclass to
                make sure that is a valid move for the piece
            If that returns True
                It will then call various sub-methods within the Game class
                to further analyze if that is a legal move
            If all of these returns True
                It will then call a final method to make the move which
                will update the board with the piece in the new position
                and update the old position to empty. It will also change
                game state if necessary and update turn and count. """

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
            """Method that sets the current state of the game,
            which is one of three states RED_WON, BLACK_WON, or UNFINISHED"""
            if color == "BLACK":
                self._game_state = "BLACK_WON"
            elif color == "RED":
                self._game_state = "RED_WON"

        def get_red_move(self):
            """Method that returns True if it is Red's move"""
            return self.get_red_move()

        def set_red_move(self):
            """Method to set whether it is red's move (True) or blacks
            This will be called after every successful move"""
            if self._red_move == True:
                self._red_move = False
            else:
                self._red_move = True


        #####We now initialize the piece objects and place on Board##############

        ########################################################################
        ####################   RED PIECES  #####################################
        ########################################################################

        ####################   RED ROOKS   #####################################
        red_rook1 = Rook('RR', 'red', 'rook', 'a1')
        str_coord = 'a1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_rook1 #have to do y first because nested list

        red_rook2 = Rook('RR', 'red', 'rook', 'i1')
        str_coord = 'i1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_rook2  #have to do y first because nested list

        #print(red_rook2.get_type())

        ####################   RED KNIGHTS/HORSES  #############################
        red_knight1 = Knight('RN', 'red', 'knight', 'b1')
        str_coord = 'b1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_knight1  #have to do y first because nested list

        red_knight2 = Knight('RN', 'red', 'knight', 'h1')
        str_coord = 'h1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_knight2  #have to do y first because nested list

        ####################   RED BISHOPS/ELEPHANTS  ##########################
        red_bishop1 = Bishop('RB', 'red', 'bishop', 'c1')
        str_coord = 'c1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_bishop1  #have to do y first because nested list

        red_bishop2 = Bishop('RB', 'red', 'bishop', 'g1')
        str_coord = 'g1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_bishop2  #have to do y first because nested list

        ####################   RED GUARDS   ####################################
        red_guard1 = Guard('RG', 'red', 'guard', 'd1')
        str_coord = 'd1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_guard1  # have to do y first because nested list

        red_guard2 = Guard('RG', 'red', 'guard', 'f1')
        str_coord = 'f1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_guard2  # have to do y first because nested list

        ####################   RED KING    #####################################
        red_king = King('RK', 'red', 'king', 'e1')
        str_coord = 'e1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_king  # have to do y first because nested list


        ####################   RED CANNONS   ####################################
        red_cannon1 = Cannon('RC', 'red', 'cannon', 'b3')
        str_coord = 'b3'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_cannon1  # have to do y first because nested list

        red_cannon2 = Cannon('RC', 'red', 'cannon', 'h3')
        str_coord = 'h3'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_cannon2  # have to do y first because nested list

        ####################   RED PAWNS   #####################################
        red_pawn1 = Pawn('RP', 'red', 'pawn', 'a4')
        str_coord = 'a4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn1  # have to do y first because nested list

        red_pawn2 = Pawn('RP', 'red', 'pawn', 'c4')
        str_coord = 'c4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn2  # have to do y first because nested list

        red_pawn3 = Pawn('RP', 'red', 'pawn', 'e4')
        str_coord = 'e4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn3  # have to do y first because nested list

        red_pawn4 = Pawn('RP', 'red', 'pawn', 'g4')
        str_coord = 'g4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn4  # have to do y first because nested list

        red_pawn5 = Pawn('RP', 'red', 'pawn', 'i4')
        str_coord = 'i4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn5  # have to do y first because nested list

        ########################################################################
        ####################   BLACK PIECES  #####################################
        ########################################################################

        ####################   BLACK ROOKS   #####################################
        black_rook1 = Rook('BR', 'black', 'rook', 'a10')
        str_coord = 'a10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_rook1  # have to do y first because nested list

        black_rook2 = Rook('BR', 'black', 'rook', 'i10')
        str_coord = 'i10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_rook2  # have to do y first because nested list

        ####################   BLACK KNIGHTS/HORSES  #############################
        black_knight1 = Knight('BN', 'black', 'knight', 'b10')
        str_coord = 'b10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_knight1  # have to do y first because nested list

        black_knight2 = Knight('BN', 'black', 'knight', 'h10')
        str_coord = 'h10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_knight2  # have to do y first because nested list

        ####################   BLACK BISHOPS/ELEPHANTS  ##########################
        black_bishop1 = Bishop('BB', 'black', 'bishop', 'c10')
        str_coord = 'c10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_bishop1  # have to do y first because nested list

        black_bishop2 = Bishop('BB', 'black', 'bishop', 'g10')
        str_coord = 'g10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_bishop2  # have to do y first because nested list

        ####################   BLACK GUARDS   ####################################
        black_guard1 = Guard('BG', 'black', 'guard', 'd10')
        str_coord = 'd10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_guard1  # have to do y first because nested list

        black_guard2 = Guard('BG', 'black', 'guard', 'f10')
        str_coord = 'f10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_guard2  # have to do y first because nested list

        ####################   BLACK KING    #####################################
        black_king = King('BK', 'black', 'king', 'e10')
        str_coord = 'e10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_king  # have to do y first because nested list

        ####################   BLACK CANNONS   ####################################
        black_cannon1 = Cannon('BC', 'black', 'cannon', 'b8')
        str_coord = 'b8'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_cannon1  # have to do y first because nested list

        black_cannon2 = Cannon('BC', 'black', 'cannon', 'h8')
        str_coord = 'h8'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_cannon2  # have to do y first because nested list

        ####################   BLACK PAWNS   #####################################
        black_pawn1 = Pawn('BP', 'black', 'pawn', 'a7')
        str_coord = 'a7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn1  # have to do y first because nested list

        black_pawn2 = Pawn('BP', 'black', 'pawn', 'c7')
        str_coord = 'c7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn2  # have to do y first because nested list

        black_pawn3 = Pawn('BP', 'black', 'pawn', 'e7')
        str_coord = 'e7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn3  # have to do y first because nested list

        black_pawn4 = Pawn('BP', 'black', 'pawn', 'g7')
        str_coord = 'g7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn4  # have to do y first because nested list

        black_pawn5 = Pawn('BP', 'black', 'pawn', 'i7')
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
        """return the board in list form in its current position"""
        return self._board

    def set_board(self, x, y, x1, y1, piece):
        self._board[y1][x1] = piece
        self._board[y][x] = ""

    def print_board(self):
        """return the board in a 9x10 grid"""
        x = 10
        for item in self._board:
            # print(x)
            print(x, item)
            x -= 1
        print("   A   B   C   D   E   F   G   H   I")

    #def set_board(self, x_coord, y_coord, piece):


    def make_move(self, begin_coord, end_coord):
        """

        :param begin_coord: This will be a string representation of a coordinate
        move using algebraic notation. This will be the position of the piece
        the player wishes to move
        :param end_coord: This will be a string representation of a coordinate
        move using algebraic notation. This will be the position the player
        wishes to move to
        :return:
        If the game has been won, it will Return False
        If there is no piece at the coordinates, it will return False
        If Red tries to move Black (and vice versa), it will return False
        If the desired move is illegal for that piece type, it will return False
        If the desired move violates a principal of the game, such as generals
        facing each other or move into check, it will return False
        Otherwise, it will
            make the move by updating the board
            update game state if applicable
            update players turn
            and Return True
        """
        begin_coord = begin_coord
        end_coord = end_coord
        begin_coord_lst = self.convert_coord(begin_coord)
        end_coord_lst = self.convert_coord(end_coord)
        x = begin_coord_lst[0]
        y = begin_coord_lst[1]
        x_end = end_coord_lst[0]
        y_end = end_coord_lst[1]

        piece = self._board[y][x]
        #print(piece.get_color())
        #print(piece.get_name())
        #print(piece.get_type())
        #print(piece.get_read())

        if self._game_state == "UNFINISHED":
            #no piece on the coordinates
            if piece == "":
                #print(False)
                return False

            #no actual movement
            if x == x_end and y == y_end:
                return False

            """ THIS IS WORKING BUT WE NEED A PORTION TO UPDATE THE MOVE
            #black is trying to move a red piece
            if piece.get_color() == "red" and self._red_move == False:
                return False
            # red is trying to move a black piece
            elif piece.get_color() == "black" and self._red_move == True:
                return False
                #print(False)
            
            #THis is just a throwaway to get the iff from above
            if piece == piece:
                red = "blue"
            """

            if piece.get_type() == "rook":
                valid = piece.rook_valid_move(x, y, x_end, y_end, piece)
                if valid == False:
                    return False
                else:
                    #print(piece.get_color(), "rook valid move")
                    self.set_board(x, y, x_end, y_end, piece)

                #throwaway test function
                #piece.validate_move(x, y, x_1, y_1, piece)

            elif piece.get_type() == "pawn":
                valid = piece.pawn_valid_move(x, y, x_end, y_end, piece)
                if valid == False:
                    return False
                else:
                    #print(piece.get_color(), "pawn valid move")
                    self.set_board(x, y, x_end, y_end, piece)

            elif piece.get_type() == "cannon":
                valid = piece.cannon_valid_move(x, y, x_end, y_end, piece)
                if valid == False:
                    return False
                else:
                    # print(piece.get_color(), "pawn valid move")
                    self.set_board(x, y, x_end, y_end, piece)

            elif piece.get_type() == "king":
                pass

            elif piece.get_type() == "bishop":
                valid = piece.bishop_valid_move(x, y, x_end, y_end, piece)
                if valid == False:
                    return False
                else:
                    # print(piece.get_color(), "bishop valid move")
                    self.set_board(x, y, x_end, y_end, piece)

            elif piece.get_type() == "guard":
                pass

            elif piece.get_type() == "knight":
                pass

class Piece:
    """NEED TO UPDATE--WORK IN PROGRESS"""
    def __init__(self, name, color, type, position = None):
        self._name = name
        self._color = color
        self._type = type
        self._position = position

    def __repr__(self):   #print piece on board instead of object reference
        return self._name

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_type(self):
        return self._type

    def get_position(self):
        return self._position

class Rook(Piece):
    """NEED TO UPDATE--WORK IN PROGRESS"""
    def __init__(self, name, color, type, position = None):
        super().__init__(name, color, type, position)

    def rook_valid_move(self, x1, y1, x2, y2, piece):
        #print(piece.get_color())
        #print(x1, y1, x2, y2)
        if x1 != x2 and y1 != y2:
            #print("cant move")
            return False
        elif x1 == x2 and y1 == y2:
            #print("not ok")
            return False
        return



class Pawn(Piece):
    """NEED TO UPDATE--WORK IN PROGRESS"""

    def __init__(self, name, color, type, position=None):
        super().__init__(name, color, type, position)

    def pawn_valid_move(self, x1, y1, x2, y2, piece):
        if piece.get_color() == "red":
            print(x1, y1, x2, y2, "red")
            if y1 == 5 or y1 == 6: #precrossing the river
                if y2 != (y1 - 1) or x1 != x2:
                    print("cant move preriver")
                    return False
                else:
                    print("valid Pre-river")
            else: #after the pawn crosses the river
                if y2 == (y1 - 1) and x2 == x1:
                    print("validpostY")
                    return
                elif x2 == (x1 - 1) and y2 == y1:
                    print("validpostX-1")
                    return
                elif x2 == (x1 + 1) and y2 == y1:
                    print("validpostX+1")
                    return
                else:
                    print("cant move postriver")
                    return False
        if piece.get_color() == "black":
            print(x1, y1, x2, y2, "black")
            if y1 == 3 or y1 == 4: #precrossing the river
                if y2 != (y1 + 1) or x1 != x2:
                    print("cant move preriver")
                    return False
                else:
                    print("valid Pre-river")
            else: #after the pawn crosses the river
                if y2 == (y1 + 1) and x2 == x1:
                    print("validpostY")
                    return
                elif x2 == (x1 - 1) and y2 == y1:
                    print("validpostX-1")
                    return
                elif x2 == (x1 + 1) and y2 == y1:
                    print("validpostX+1")
                    return
                else:
                    print("cant move postriver")
                    return False

class Knight(Piece):
    """NEED TO UPDATE--WORK IN PROGRESS"""
    def __init__(self, name, color, type, position = None):
        super().__init__(name, color, type, position)
        #self._board = board

class Bishop(Piece):
    """NEED TO UPDATE--WORK IN PROGRESS"""
    def __init__(self, name, color, type, position = None):
        super().__init__(name, color, type, position)

    def bishop_valid_move(self, x1, y1, x2, y2, piece):
        #print(piece.get_color())
        print(x1, y1, x2, y2)
        if piece.get_color() == "red":
            print(x1, y1, x2, y2, "red")
            if y2 <= 4:  # can not cross the river
                print("can't cross river")
                return False
            else:
                print(x1, y1, x2, y2, "diagonal")
                if x2 == x1 or y2 == y1: #cant go stright in either direction
                    print("cant go straight")
                    return False
                elif x2 == (x1 - 2) and y2 == (y1 - 2):
                    print("TL")
                    return
                elif x2 == (x1 + 2) and y2 == (y1 - 2):
                    print("TR")
                    return
                elif x2 == (x1 - 2) and y2 == (y1 + 2):
                    print("BL")
                    return
                elif x2 == (x1 + 2) and y2 == (y1 + 2):
                    print("BR")
                    return
                else:
                    return False

class King(Piece):
    """NEED TO UPDATE--WORK IN PROGRESS"""
    def __init__(self, name, color, type, position = None):
        super().__init__(name, color, type, position)
        #self._board = board

class Guard(Piece):
    """NEED TO UPDATE--WORK IN PROGRESS"""
    def __init__(self, name, color, type, position = None):
        super().__init__(name, color, type, position)
        #self._board = board

class Cannon(Piece):
    """NEED TO UPDATE--WORK IN PROGRESS"""
    def __init__(self, name, color, type, position = None):
        super().__init__(name, color, type, position)

    def cannon_valid_move(self, x1, y1, x2, y2, piece):
        print(piece.get_color())
        print(x1, y1, x2, y2)
        if x1 != x2 and y1 != y2:
            #print("cant move")
            return False
        elif x1 == x2 and y1 == y2:
            #print("not ok")
            return False
        return


game = XiangqiGame()
game.print_board() #starting board


"""
#################   RED BISHOP TESTING  ############################

game.make_move("c1", "d2") #cant go diagonal 1 spot
game.print_board()

game.make_move("c1", "f4") #cant go diagonal 3 spot
game.print_board()

game.make_move("c1", "e3") #will work
game.print_board()

game.make_move("e3", "e4") #cant go straight
game.print_board()

game.make_move("e3", "h3") #cant go straight
game.print_board()

game.make_move("e3", "a3") #cant go straight
game.print_board()

game.make_move("e3", "c1") #will work go back to start
game.print_board()

game.make_move("c1", "a3") #valid Top Left
game.print_board()

game.make_move("a3", "c5") #valid Top right
game.print_board()

game.make_move("c5", "e3") #valid bottom right
game.print_board()

game.make_move("e3", "c1") #valid bottom left
game.print_board()
"""

"""
############## BLACK CANNON TESTING ######################
game.make_move("b8", "b7")
game.print_board()
game.make_move("b7", "b2")
game.print_board()
game.make_move("b2", "g2")
game.print_board()
game.make_move("g2", "g8")
game.print_board()
game.make_move("g8", "b8")
game.print_board()
game.make_move("b8", "c7")
game.print_board()
"""

"""
############## RED CANNON TESTING ######################
game.make_move("b3", "b4")
game.print_board()
game.make_move("b4", "b8")
game.print_board()
game.make_move("b8", "g8")
game.print_board()
game.make_move("g8", "b8")
game.print_board()
game.make_move("b8", "b4")
game.print_board()
game.make_move("b4", "b1")
game.print_board()
"""

"""
########BLACK PAWN TESTING##################################
game.make_move("a7", "a6") #passes
game.print_board()
game.make_move("a6", "a5")
game.print_board()
game.make_move("a5", "a4")
game.print_board()

game.make_move("a4", "b4")
game.print_board()

game.make_move("b4", "a4")
game.print_board()

game.make_move("a6", "a7")
game.print_board()
game.make_move("a7", "b7")
game.make_move("b7", "a7")

#game.make_move("a7", "a6") #fails
#game.print_board()
"""

"""
########RED PAWN TESTING###################################
game.make_move("a4", "a5")
game.print_board()
game.make_move("a5", "a6")
game.print_board()
game.make_move("a6", "a7")
game.print_board()
game.make_move("a7", "b7")
game.make_move("b7", "a7")
game.print_board()


##################ROOK#####################################
#NOTE I DELETED MOST OF TESTING
#game.make_move("a1", "a2") #rook




#print(game.get_board()) #prints it as a list
"""



