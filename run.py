#import library for computer player
import random

#Welcome message for the game
welcome = "Glad you found us, want to play Tic-Tac-Toe?\n"
print(welcome)

#Shows the rules of the game to the player
game_rules = '''
    Here's how you play the game:
        - Make a move by placing your marker, X or 0, on the board. 
        - Next move is made by the computer.
        - The player who successfully places 3 markers in a row, vertically,horizontally or diagonally will win'''
        
print(game_rules)
print("\n")

class TicTacToeGame:
    def __init__(self):
        self.board = []
        self.symbol_1, self_symbol_2 = self.decide_symbol()

    def main():
        """
        Main function
        """
        self.create_board()
        self.game_rules()
        

    
    def decide_symbol(self):
        """
        Will randomly choose what symbol the player and computer will play, X or O
        """
        symbol_1 = random.choice(["X", "O"])
        if symbol_1 == "X":
            symbol_2 = "O"
        else:
            symbol_2 = "X"
        return symbol_1, symbol_2

    def create_board(self):
        """
        Creates a 3x3 board for the game
        """
        print("Tic-Tac-Toe")
        board = [ [0] * 3 ] * 3
        for row in board:
            print(row)


def player_name():
    """
    Player will chose their name for the game
    Only alphabetic characters will be accepted
    """
    print("Print your name for this game")
    while True:
        name = input("My name is: ")
        if name.isalpha():
            print(f"Hi {name}, let's play!")
            break
        else:
            print("Your name can only be alphabetic characters, try again")
            
player_name()

def first_player():
    """
    Will choose randomly which player starts
    """
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return '{player_name}'
        

def start_game(board, symbol_1, symbol_2):
    """
    Starts the game and decides who will start
    """
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Player" + player +", it´s your turn")



game = TicTacToeGame()
game.create_board()
print(game.board)  
    
