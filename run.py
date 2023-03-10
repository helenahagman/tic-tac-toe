#import library for computer player
import random

welcome = "Glad you found us, want to play Tic-Tac-Toe?\n"

print(welcome)

class TicTacToeGame:

    def main():
        """
        Main function
        """
        board = create_board()
        game = game_rules()
        symbol_1, symbol_2 = decice_symbol()

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

game_rules()

    def player_name():
        """
        Player will chose their name for the game
        Only alphabetic characters will be accepted
        """
        print("Choose a name for this game")
        while True:
            name = input("My name is: ")
            if name.isalpha():
                print(f"Hi {name}, let's play!")
        else:
            print("Your name can only be alphabetic characters, try again")
            
player_name()

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


    
