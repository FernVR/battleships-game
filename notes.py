from random import randint
import random

# Youtube video notes:
 """

class GameBoard:
    """
    """
    def __init__(self, board):
        self.board = board

    def letters_to_numbers():
        letters_numbers = {"A": 0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
        return letters_numbers

    def print_game_board(self):
        print("   A B C D E F G H")
        print("  ////////////////")

        row_number = 1
        for row in self.board:
            print(row_number, "|".join(row))
            row_number += 1

class Battleship:
    """
    """
    def __init__(self, board):
        self.board = board

    def generate_ships(self):
        for i in range(5):
            self.x_row, self.y_col = random.randint(0, 7), random.randint(0,7)
            while self.board[self.x_row][self.y_col] == "X":
                self.x_row, self.y_col = random.randint(0, 7), random.randint(0,7)
            self.board[self.x_row][self.y_col] = "X"
        return self.board

    def get_user_input(self):
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in "12345678":
                print("invalid input. please enter a valid input")
                x_row = input("Enter the row of the ship: ")
            y_col = input("Enter the column LETTER of the ship: ").upper()

            while y_col not in "ABCDEFGH":
                print("invalid input. please enter a valid input")
                y_col = input("Enter the column LETTER of the ship: ").upper()
            return int(x_row) -1, GameBoard.letters_to_numbers()[y_col]
        except ValueError and KeyError:
            print("Invalid Input")
            return self.get_user_input()
    
    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships
    

def run_game():
    computer_board = GameBoard([[" "] * 8 for i in range(8)])
    user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
    Battleship.generate_ships(computer_board)
    # Starts at 10 turns
    turns = 10
    while turns > 0:
        GameBoard.print_game_board(user_guess_board)
        # Get user input
        user_x_row, user_y_col = Battleship.get_user_input(object)
        # Check if duplicate guess
        while user_guess_board.board[user_x_row][user_y_col] == "-" or user_guess_board.board[user_x_row][user_y_col] == "X":
            print("You guessed that one already!\n")
            user_x_row, user_y_col = Battleship.get_user_input(object)
        # Check hit or miss
        if computer_board.board[user_x_row][user_y_col] == "X":
            print("You sunk one Battleship!")
            user_guess_board.board[user_x_row][user_y_col] == "X"
        else:
            print("Missed!")
            user_guess_board.board[user_x_row][user_y_col] == "-"
        # Check if win or lose
        if Battleship.count_hit_ships(user_guess_board) == 5:
            print("You have hit all 5 Battleships!\n")
            print("WINNER WINNER CHICKEN DINNER")
            break
        else:
            turns -= 1
            print(f"You have {turns} turns remaining...")
            if turns == 0:
                print("sorry... you ran out of turns!")
                print("Game Over")
                GameBoard.print_game_board(user_guess_board)
                break 

if __name__ == '__main__':
    run_game()

"""




# Creating functions we need:

def print_rules():
    """
    Prints rules of game to terminal 
    "Do you want to proceed Y/N" Text input to check
    if user wants to continue 
    """

def name_input():
    """
    Takes name of the user and asks what size grid they want?
    6/10 grid size 
    """

def create_grid():
    """
    creates player grid 
    creates computer grid 
    prints grids to terminal
    """

def player_turn():
    """
    Allows player to take their turn
    Validates their guess, Hit or Miss.
    """

def computer_turn():
    """
    Generates computer turn
    Validates the guess, Hit or Miss
    """

def play():
    """
    function to start game
    """





# Youtube Video 2 notes:

# LEGEND 
# X for placing battleship and hit battleship
# " " for available space
# " - " for missed shot

HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
GUESS_BOARD = [[" "] * 8 for x in range(8)]

letters_to_numbers = {"A": 0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}

def print_board(board):
    print("  ///////////////")
    print("  A B C D E F G H")
    print("  ---------------")

    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def create_ships(board):
    for ship in range(5):
        ship_row, ship_col = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_col] == "X":
            ship_row, ship_col = randint(0, 7), randint(0, 7)
        board[ship_row][ship_col] = "X"


def get_ship_location():
    row = input("Please enter a ship ROW (1-8)")
    while row not in "12345678":
        print("Please enter a valid row.")
        row = input("Please enter a ship ROW (1-8)")
    column = input("Please enter a ship COLUMN (A-H)").upper()
    while column not in "ABCDEFGH":
        print("Please enter a valid column.")
        column = input("Please enter a ship COLUMN (A-H)").upper()
    return int(row) - 1, letters_to_numbers[column]


            
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count




create_ships(HIDDEN_BOARD)
print_board(HIDDEN_BOARD)

turns = 10
while turns > 0:
    print("Welcome to Battleships!")
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == "-":
        print("You've already guessed that")
    elif HIDDEN_BOARD[row][column] == "X":
        print("Well done! You hit the ship!")
        GUESS_BOARD[row][column] = "X"
        turns -= 1
    else:
        print("sorry you missed!!")
        GUESS_BOARD[row][column] = "-"
        turns -= 1
    
    if count_hit_ships(GUESS_BOARD) == 5:
        print("Congrats!! you have hit all the battleships")
        print("Game Over")
        break
    print("You have " + str(turns) + " turns remaining")
    if turns == 0:
        print("No more turns, Game Over")
        break

    
    






    
