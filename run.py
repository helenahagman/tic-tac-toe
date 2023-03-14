#import library for computer player
import random


class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]        
        self.current_player = 'X'
       
    def welcome(self)
        """
        Welcome message for the game
        """
        welcome = "Welcome to the Tic-Tac-Toe game!"
        print(welcome)
    
    def show_rules(self):
        """
        Shows the rules of the game to the player
        """
        game_rules = '''
        Here's how you play the game:
            * Make a move by placing your marker, X, on the board. 
            * Next move is made by the computer, O.
            * You will take turns with the computer until the board is full.
            * The player who successfully places 3 markers in a row wins.
            * Vertical, horizontal or diagonal rows all count as a win.
            * If nobody won and the the board is full, it's a tie.\n'''
        
        print(game_rules)


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

    def want_to_play():
        """
        Asks the visitor if they want the game to start
        """
        while True:
            want_to_play_input = input("Type 'Start' to start the game:\n").lower()
            if want_to_play_input == 'Start':
                game_starts = "Starting game"
                print(game_starts)
                break
            else:
                print(f"{want_to_play_input} Incorrect, enter 'Start' to start the game.")


    def start_game(self):
        """
        Starts the game and decides who will start
        Checks if move is possible or not
        Checks if the game is won or not
        """
        while True:
            player_input = input(f"{self.current_player}, your turn, choose a number between 1 and 9")
            try:
                player_select = int(player_input)
            except ValueError:
                print("Try again, your number needs to be between 1 and 9")
                continue

            if player_select > 9 or player_select < 1:
                print("Try again, your number needs to be between 1 and 9")
                continue

            if self.board(player_select-1) = self.current_player
            self.print_board()
            winner = self.winner_check()
            if winner is not None:
                print(f"The winner is {winner}!")

            if ' ' not in self.board:
                print("Tie! Nobody wins.")
            
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            if self.current_player == 'O':
                self.computer_move()
   
    
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



    
    def print_board(self):
        """
        Will show the board with current status
        """
        for row in self.board:
            print(" ".join(row))
            





game = TicTacToeGame()
print(game.board)  
    
