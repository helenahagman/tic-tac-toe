#import library for computer player
import random


class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]        
        self.current_player = 'X'
       
    def welcome(self):
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
            * If nobody won and the the board is full, it's a tie.
            * The board is numbered like this:
        print('| 1 | 2 | 3 |')
        print('| 4 | 5 | 6 |')
        print('| 7 | 8 | 9 |')\n'''
        
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

    def want_to_play(self):
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
        self.welcome()
        self.show_rules()
        self.create_board()
        self.first_player()
        self.player_name()

        while True:
            player_input = input(f"{self.current_player}, your turn, choose a number between 1 and 9: ")
            try:
                player_select = int(player_input)
            except ValueError:
                print("Try again, your number needs to be between 1 and 9: ")
                continue

            if player_select > 9 or player_select < 1:
                print("Try again, your number needs to be between 1 and 9: ")
                continue

            self.board[player_select-1] = self.current_player
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

    def winner_check(self):
        winning_combinations = [
            # Horizontal
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            # Vertical
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            # Diagonal
            (0, 4, 8),
            (2, 4, 6)
        ]

        for comb in winning_combinations:
            if self.board[comb[0]] == self.board[comb[1]] == self.board[comb[2]] != ' ':
                return self.board[comb[0]]

        return None

    def make_move(self, is_human):
        """
        Prompts the player to select a move and updates the board accordingly.
        If is_human is True, the move will be made by the human player, otherwise the computer player.
        """
        player = "human" if is_human else "computer"
        prompt = f"Enter the cell number where you want to place '{self.current_player}': "
    
        if is_human:
            move = input(prompt)
            while not self.is_valid_move(move):
                print("Try again")
                move = input(prompt)
            self.board[int(move) - 1] = self.current_player
        else:
            move = self.get_computer_move()
            self.board[move] = self.current_player

        print(f"{player} played {self.current_player} in cell {move + 1}.\n")


    def winner_check(self):
        """
        Checks if there is a winner and returns the winner (if any).
        """
        winning_combinations = [
            # Horizontal
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            # Vertical
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            # Diagonal
            (0, 4, 8),
            (2, 4, 6)
        ]

        for comb in winning_combinations:
            if self.board[comb[0]] == self.board[comb[1]] == self.board[comb[2]] != ' ':
                return self.board[comb[0]]

        return None

    def game_over(self):
        """
        Will check if the game is over 
        """
        return self.winner_check() or ' ' not in self.board


    def play(self, position):
        """
        Main function to play the game
        """
        print("Welcome to the Tic-Tac-Toe game!")
        self.player_name()
        self.first_player()
        self.create_board()

        while not self.game_over():
            if self.current_player == 'X':
                self.make_move(True)
            else:
                self.make_move(False)
            self.print_board()
        
        if self.winner_check() == 'X':
            print("You win!")
        elif self.winner_check() == 'O':
            print("Computer wins!")
        else:
            print("Nobody won, it is a tie!")



if__name__ == "__main__":
game = TicTacToeGame()
game.play()  
    
