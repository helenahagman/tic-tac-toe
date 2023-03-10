#import library for computer player
import random

welcome_intro = "Glad you found us, want to play Tic-Tac-Toe?\n"

class TicTacToeGame:

    def __init__(self):
        self.board = []

    def create_board(self):
        """
        Creates a 3x3 board for the game
        """
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)


    def game_rules():
        """
        Shows the rules of the game to the player
        """
        print("How to play the game:\n")
        print("Make a move by placing your marker, represented by X or 0, on the board.\n" 
        "Next move is made by the computer.\n"
        "The winner has successfully placed 3 markers in a row, vertically,\n"
        "horizontally or diagonally\n")
        input("Press enter to start the game")

    #def player_one():
        """
        Human player marks with X in the game
        """

    def computer_player()
        """
        Computer player marks with O in the game
        """


    #def start():
        """
        Start the game and shows the board
        """    
    
    #def win():
        """
        Defines what happens when the game is won
        A game is won when a player have all 3 markers in a row
        Horizantally, vertically or diagonally
        """

    
    #def board_full():
        """
        When both players used their initial 3 marks
        the game continues but now the players need to move a marker on the board to a different space
        """

                                                       