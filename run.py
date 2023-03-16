import random
# import library for computer player

# Welcome message for the game
welcome = "Welcome to the Tic-Tac-Toe game!"
print(welcome)
    
# Shows the rules of the game to the player
game_rules = '''
    Here's how you play the game:
        * Make a move by placing your marker, X, on the board. 
        * Next move is made by the computer, O.
        * You will take turns with the computer until the board is full.
        * The player who successfully places 3 markers in a row wins.
        * Vertical, horizontal or diagonal rows all count as a win.
        * If nobody won and the board is full, it's a tie.
        * The board is numbered like this:
        | 1 | 2 | 3 |
        | 4 | 5 | 6 |
        | 7 | 8 | 9 | '''
        
print(game_rules)
print("\n")


class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]        
        self.current_player = 'X'
       

    def create_board(self):
        """
        Creates a board 3 rows and 3 columns
        """
        print('-------------')
        for i in range(0, 9, 3):
            print(f'| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |')
            print('-------------')


    def player_name(self):
        """
        Player will choose their name for the game
        Only alphabetic characters will be accepted
        """
        print("Please pick a name for this game.")
        while True:
            name = input("Name: \n")
            if name.isalpha():
                print(f"Hi {name}, let's play!")
                self.player = name
                return name
            else:
                print("Your name can only be alphabetic characters, try again")


    def make_move(self, position):
        """
        Tells the player to make a move
        Also updates the board after each move
        """
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        else:
            print("You can not make that move, try again.")
            return False


    def start_game(self):
        """
        Starts the game and decides who will start
        Checks if move is possible or not
        Checks if the game is won or not
        """
        self.player_name()
        self.create_board()
        while not self.game_over():
            if self.current_player == 'X':
                while True:
                    position = input("Your turn, enter a number between 1 and 9: \n")
                    if position.isnumeric():
                        position = int(position) - 1
                        if position < 0 or position > 8:
                            print("Try again, a number between 1 and 9: ")
                            continue
                        if self.make_move(position):
                            break
                    else:
                        print("Try again, a number between 1 and 9: ")
            else:
                print("Computer move")
                available_positions = [i for i, x in enumerate(self.board) if x == ' ']
                position = random.choice(available_positions)
                self.make_move(position)
            self.create_board()
            winner = self.winner_check()
            if winner is not None:
                if winner == 'X':
                    print(f"The winner is {self.player}!")
                else:
                    print("Tuff luck, computer wins!")
                break
            if ' ' not in self.board:
                print("Tie! Nobody wins.")
                break
            self.current_player = 'O' if self.current_player == 'X' else 'X'
       
        while True:
            play_again = input("Play again? Print Y for yes or N to quit: ")
            if play_again.upper() == "N":
                print("Ok, see you later!")
                break
            elif play_again.upper() == "Y" :
                self.board = [' ' for _ in range(9)]
                self.current_player = 'X'
                self.start_game()
            else:
                print("Want to play again? Press Y or N if you want to end the game.")
               

    def winner_check(self):
        """
        Checks if there is a winner 
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
            self.create_board()
        
        if self.winner_check() == 'X':
            print("You win!")
        elif self.winner_check() == 'O':
            print("Computer wins!")
        else:
            print("Nobody won, it is a tie!")



if __name__ == "__main__":
    game = TicTacToeGame()
    game.start_game()
    
