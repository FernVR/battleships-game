# Import libraries
from random import randint
import random
import time

# ANSI Escape codes
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
END_COLOR = "\033[0m"

# LEGEND 
# "X" for placing battleship and hit battleship
# "~" for available space
# "O" for missed shot

AVAILABLE_BLOCK = "~"
MISSED_SHOT = "O"
GUESSED_SHIP = "X"

GRID_SIZE = 8

# Generates 8 empty slots for game board
HIDDEN_BRD = [[BLUE + "~" + END_COLOR] * GRID_SIZE for x in range(GRID_SIZE)]
GUESS_BRD = [[BLUE + "~" + END_COLOR] * GRID_SIZE for x in range(GRID_SIZE)]
# Computer board for computer guess ?

HIDDEN_COMP_BRD = [[BLUE + "~" + END_COLOR] * GRID_SIZE for x in range(GRID_SIZE)]
COMP_GUESS_BRD = [[BLUE + "~" + END_COLOR] * GRID_SIZE for x in range(GRID_SIZE)]

# Converts letters to number/ position 
letters_to_numbers = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, 
                      "G" : 6, "H" : 7}

# Creating functions we need:

RULES = """
Welcome to Battleships {{vara}}!
There are 5 Ships to Hit, and 10 turns.
Hit ships will show" + red + " X" + end_color + "
Missed ships will show" + yellow + " O" + end_color + "
"""

def print_rules():
    """
    Prints rules of game to terminal 
    "Do you want to proceed Y/N" Text input to check
    if user wants to continue 
    """
    username = input(GREEN + "Please enter your username: " + END_COLOR)
    print(RULES.format(vara=f"{YELLOW + username.upper() + END_COLOR}"))
    
        # unable to exit loop here, figure out how to exit game? BREAK doesn't work

    
    
    
def create_board(board):
    """
    creates player grid 
    prints grids to terminal
    """
    print("\n  A B C D E F G H") 
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
        

def create_ships(board):
    """
    Creates ships with random numbers between 0-7
    """
    for _ in range(5):
        while True:
            ship_row, ship_col = randint(0, GRID_SIZE -1 ), randint(0, GRID_SIZE -1 )
            if board[ship_row][ship_col] == GUESSED_SHIP:
                continue
            board[ship_row][ship_col] = GUESSED_SHIP


def user_input():
    """
    Allows player to take their turn
    Validates their guess, Hit or Miss.
    If a user enters an invalid input, or NO input, 
    the input will run again until a user inputs a valid input.
    """
    while True:
        try:
            row = int(input("\nPlease enter a ROW (1-8): "))
            # if row < 1 or row > GRID_SIZE:
            if row not in letters_to_numbers.values():
                raise ValueError()
        except ValueError:
            print("Invalid input.. please try again..")

    while row not in "12345678":
        print(RED + "Invalid Input. Please enter a number(1-8)\n" + END_COLOR)
        row = input("\nPlease enter a ROW (1-8): ")
    column = column = input("\nPlease enter a COLUMN (A-H): ").upper()
    while column not in "ABCDEFGH":
        print(RED + "Invalid Input. Please enter a letter(A-H)\n" + END_COLOR)
        column = input("\nPlease enter a COLUMN (A-H): ").upper()
    return int(row) - 1, letters_to_numbers[column]


def computer_turn():
    """
    Generates computer turn
    Validates the guess, Hit or Miss
    """


def count_hits(board):
    count = 0
    for row in board:
        for column in row:
            if column == RED + "X" + END_COLOR:
                count += 1
    return count


def play_game():
    """
    plays game
    creates 10 turns for a user 
    places miss and hit symbols where the user guesses
    checks if user has already made the same move and notifies them
    User only loses a turn if they miss
    """
    turns = 10
    while turns > 0:
        create_board(HIDDEN_BRD)
        print("hidden board : test")
        create_board(GUESS_BRD)
        print(GREEN + "   COMPUTER GRID" + END_COLOR)
        create_board(HIDDEN_COMP_BRD)
        print(GREEN + "    PLAYER GRID" + END_COLOR)
        row, column = user_input()
        if GUESS_BRD[row][column] == "-":
            print(YELLOW + f"\nYou've already guessed that, PLEASE TRY AGAIN\n" + END_COLOR)
        elif HIDDEN_BRD[row][column] == "X":
            print(GREEN + "\nWell done! You hit the ship!\n" + END_COLOR)
            GUESS_BRD[row][column] = red + "X" + end_color
        else:
            print(YELLOW + "\nSorry, you missed!\n" + END_COLOR)
            GUESS_BRD[row][column] = YELLOW + "O" + END_COLOR
            turns -= 1
            
        if count_hits(GUESS_BRD) == 5:
            print(YELLOW + "CONGRADULATIONS! You hit all the battleships. \n")
            print(RED + "GAME OVER" + end_color)
            break
        
        print(GREEN + "You have " + str(turns) + " turns remaining.\n" + END_COLOR)
        if turns == 0:
            print(RED
             + "No more turns. Game Over.")
            break
        


def main():
    """
    Calls all functions to start game
    """
    print_rules()
    rules = input(f"Do you wish to continue? Y/N: ").upper()
    if rules != "Y":
        print("We're sorry to see you go!")
        return

    create_ships(HIDDEN_BRD)
    create_ships(HIDDEN_COMP_BRD)
    play_game()


if __name__ == "__main__":
    main()