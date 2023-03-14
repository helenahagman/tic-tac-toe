#import library for computer player
import random

#Welcome message for the game
welcome = "Glad you found us, want to play Tic-Tac-Toe?\n"
print(welcome)

#Shows the rules of the game to the player
game_rules = '''
    Here's how you play the game:
        * Make a move by placing your marker, X or 0, on the board. 
        * Next move is made by the computer.
        * The player who successfully places 3 markers in a row, vertically,horizontally or diagonally will win\n'''
        
print(game_rules)
print("\n")

class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]        
        self.current_player = 'X'
       
    
    def player_name(self):
        """
        Player will chose their name for the game
        Only alphabetic characters will be accepted
        """
        print("Please pick a name for this game.")
        while True:
            name = input("Name: ")
            if name.isalpha():
                print(f"Hi {name}, let's play!")
                return name
            else:
                print("Your name can only be alphabetic characters, try again")
            
    
    def create_board(self):
        """
        Creates a board 3 rows and 3 columns
        """
        print('-------------')
        for i in range(0, 9, 3):
            print(f'| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |')
            print('-------------')


    def first_player():
        """
        Will choose randomly which player starts
        """
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return '{player_name}'


    def play(self, position):
        """
        Will start the game
        Human player and Computer player will take turns
        """
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'
        else:
            print("Not correct, make another move.")


        def make_move(self, is_human):
            """
            Will allow the players to make a move
            checks if it is a possible move and updates the board accordningly
            """
            player_name = self.name if is_human else "Computer"
            print(f"{self.name}, make your move.")
            while True: 
                col = int(input("Choose column, 0-2: "))
                row = int(input("Choose row, 0-2: "))
                if self.board[row][col] == "-":
                    symbol = self.symbol_1 if is_human else self.symbol_2
                    self.board[row][col] = symbol
                    break
                else:
                    print("You need to make another move, this space is taken")
            self.print_board()



        def winner_check(self):
            """
            Will check for a winner with 3 in a row, horizontally, vertically or diagonally 
            """
            winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
            for pos in winning_positions:
                if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] != ' ':
                    return self.board[pos[0]]
            if ' ' not in self.board:
                return 'tie'
            return None


        def print_board(self):
            """
            Will show the board with current status
            """
            for row in self.board:
                print(" ".join(row))
            


def start_game(board, symbol_1, symbol_2):
    """
    Starts the game and decides who will start
    Also checks if move is possible or not
    """
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Player" + player +", it is your turn")
    column = int(input("Choose a column:"
                    "[left column: 0, middle column: 1, right column: 2]"))

    row = int(input("Choose a row:"
                    "[upper row: 0, middle row: 1, right row: 2]"))
    

    while (column < 0 or column > 2) or (row < 0 or row > 2):
        wrong_selection(column, row)
        column = int(input("Choose a column:"
                    "[left column: 0, middle column: 1, right column: 2]"))

        row = int(input("Choose a row:"
                    "[upper row: 0, middle row: 1, right row: 2]"))
        


game = TicTacToeGame()
print(game.board)  
    
