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
        self.player_name()
    
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
            slef.name = name
            break
        else:
            print("Your name can only be alphabetic characters, try again")
            
           
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
        board = [["-"] * 3 for _ in range(3)]
        for row in board:
            print(row)
        self.board = board

    def play(self):
        """
        Will start the game
        Human player and Computer player will take turns
        """
        count = 0
        human_turn = first_player(self.name)
        while True:
            if human_turn == "human":
                self.human_move()
                count += 1
                computer_turn = "computer"
            else:
                self.computer_move()
                count += 1
                human_turn = "human"
            winner = self.check_winner()
            if winner:
                print(f"Congrats {winner} just won!")
                break
            elif count == 9:
                print("Tie! Nobody won, try again!")
                

        def human_move(self):
            """
            Will allow the human player to make a move
            checks if it is a possible move and updates the board accordningly
            """
            print(f"{player_name}, make your move.")
            while true: 
                col = int(input("Choose column, 0-2: "))
                row = int(input("Choose row, 0-2: "))
                if self.board[col][row] == "-":
                    self.board[col][row] = self.symbol_1
                    break
            self.print_board()

        def computer_move(self):
            """
            Will allow the computer player to make a random move
            Updates the board accordningly
            """
            print("Computer makes a move.")
            while true: 
                col = int(input("Choose column, 0-2: "))
                row = int(input("Choose row, 0-2: "))
                if self.board[col][row] == "-":
                    self.board[col][row] = self.symbol_1
                    break
            self.print_board()

        def winner_check(self):
            """
            Will check for a winner with 3 in a row 
            """
            cols = [[self.board[i][j]] for i in range(3)] for j in range(3)]
            rows = [[self.board[i][j]] for j in range(3)] for i in range(3)]
            diags = [[self.board[i][j]] for i in range(3)], [self.board[1][2-i]] for j in range(3)
            lines = cols + rows + diags
            for line in lines:
                if len(set(line)) == 1 and line[0] != "-":
                    return line[0]
            return None

        def print_board(self):
            """
            Will show the board with current status
            """
            for row in self.board:
                print(" ".join(row))
            



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
game.create_board()
print(game.board)  
    
