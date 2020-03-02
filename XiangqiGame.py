from typing import List, Optional, Any

# Portfolio Project
# Author: Craig Sperlazza
# Date: 2/26/2020
# Description: Creates

class Board:
    """Class named Board that has three private data members: the board,
    current state of game (which will update to alert if either
    x or o have won the game or if it is unifinished), and an x piece tracker"""

    def __init__(self):
        """Initializes a board as a list made of eight list elements, tracks
         position for x, and sets the current state of the game to UNFINISHED"""
        self._board = [["R", "N", "B", "G", "K", "G", "B", "N", "R"],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "C", "", "", "", "", "", "C", ""],
                       ["P", "", "P", "", "P", "", "P", "", "P"],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["P", "", "P", "", "P", "", "P", "", "P"],
                       ["", "C", "", "", "", "", "", "C", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["R", "N", "B", "G", "K", "G", "B", "N", "R"]]

    def get_board(self):
        """return the board in a 9x10 grid"""
        x = 10
        for item in self._board:
            # print(x)
            print(x, item)
            x -= 1
        print("    A    B    C    D    E    F    G    H   I")

fb = Board()
print(fb.get_board())