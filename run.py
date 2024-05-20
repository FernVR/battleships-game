# Import libraries
from random import randint
import random
import time
import sys
import string

# ANSI Escape codes
BLUE = "\u001b[34m"
GREEN = "\u001b[32m"
RED = "\u001b[31m"
YELLOW = "\u001b[33m"
CYAN = "\u001b[36m"
WHITE = "\u001b[37;1m" # "BRIGHT/BOLD White"

# LEGEND 
# "X" for placing battleship and hit battleship
# "~" for available space
# "O" for missed shot

HIT = RED + "X" + WHITE
MISS = YELLOW + "O" + WHITE
AVAILABLE = CYAN + "~" + WHITE

# Grid size and No. of ships can be adjusted 
GRID_SIZE = 7
MAX_SHIPS = 5

create_empty_board = lambda: [[AVAILABLE] * GRID_SIZE for _ in range(GRID_SIZE)]

# Generates 8 empty slots for game board
HIDDEN_BRD = create_empty_board()
GUESS_BRD = create_empty_board()

# Computer board for computer guess ?
HIDDEN_COMP_BRD = create_empty_board()
COMP_GUESS_BRD = create_empty_board()

# Converts letters to number/ position 
BOARD_ROW_TO_COLUMNS_MAP = dict(zip(string.ascii_uppercase[0: GRID_SIZE], range(GRID_SIZE)))

# CONST Variables
USERNAME = input(WHITE + "Please enter your username: " + CYAN)
if USERNAME == "":
    USERNAME = "PLAYER"

RULES = f"""
        Welcome to Battleships, {YELLOW + USERNAME.upper() + WHITE}!
        --------------------------------
        Rules are as follows:
        1. You will be looking for hidden ships on the computer's grid.
        2. The computer will guess for the ships on your grid.
        3. You will be asked for row(1-8) and column(A-H) inputs.
        4. The winner is the player that guesses all the ships first!
        5. To EXIT the game, type the letter "Q" (CAPITALIZE IT!)
           into any input, and you will exit the game.
        """

# Functions

def print_rules():
    """
    Prints rules of game to terminal 
    "Do you want to proceed Y/N" Text input to check
    if user wants to continue 
    """
    print(WHITE + RULES)
    print("Do you wish to continue?")
    rules_input= input("Press" + YELLOW + " Y " + WHITE + "to play\nOr any key to exit game: ")
    if rules_input != "y":
        print(CYAN + "We're sorry to see you go!" + WHITE)
        exit_game()

    
def print_board(board):
    """
    creates player grid 
    prints grids to terminal
    """
    alphabets = " ".join(list(string.ascii_uppercase[0: GRID_SIZE]))
    print(f"\n  {alphabets}") 
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
        

def place_ships(board):
    """
    Creates ships with random numbers from grid size
    """
    for ship in range(MAX_SHIPS):
        ship_row, ship_col = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)
        while board[ship_row][ship_col] == "X":
            ship_row, ship_col = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE -1)
        board[ship_row][ship_col] = "X"


def user_input():
    """
    Allows player to take their turn
    Validates their guess, Hit or Miss.
    If a user enters an invalid input, or NO input, 
    the input will run again until a user inputs a valid input.
    """
    row = input("\nPlease enter a ROW (1-8): ")
    if row == "Q":
        exit_game()
    while row not in ["1", "2", "3", "4", "5", "6", "7", "8"] or row == "":
        print(RED + "Invalid Input. Please enter a number(1-8)\n" + WHITE)
        row = input("\nPlease enter a ROW (1-8): ")
    column = input("\nPlease enter a COLUMN (A-H): ").upper()
    if column == "Q":
        exit_game()
    while column not in BOARD_ROW_TO_COLUMNS_MAP.keys():
        print(RED + "Invalid Input. Please enter a letter(A-H)\n" + WHITE)
        column = input("\nPlease enter a COLUMN (A-H): ").upper()
    return int(row) - 1, BOARD_ROW_TO_COLUMNS_MAP[column]


def count_hits(board):
    count = 0
    for row in board:
        for column in row:
            if column == HIT:
                count += 1
    return count

# to be deleted?
def computer_input():
    """
    Generates two random integars 
    """
    return random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)


def play_game():
    """
    plays game
    creates 10 turns for a user 
    places miss and hit symbols where the user guesses
    checks if user has already made the same move and notifies them
    User only loses a turn if they miss
    """
    turns = 65
    while turns > 0:
        print_board(HIDDEN_BRD)
        print("hidden player board : test")
        print_board(HIDDEN_COMP_BRD)
        print(GREEN + f"   {USERNAME.upper()}'S GRID" + WHITE)
        print_board(GUESS_BRD)
        print(GREEN + "  COMPUTER'S GRID" + WHITE)
        row, column = user_input()
        if GUESS_BRD[row][column] == MISS:
            print(YELLOW + f"\nYou've already guessed that, PLEASE TRY AGAIN\n" + WHITE)
        elif HIDDEN_BRD[row][column] == "X":
            print(GREEN + "\nWell done! You hit the ship!\n" + WHITE)
            GUESS_BRD[row][column] = HIT
        else:
            print(YELLOW + "\nSorry, you missed!\n" + WHITE)
            GUESS_BRD[row][column] = MISS
            turns -= 1
        
        # Computer Turn
        row, column = computer_input()
        while HIDDEN_COMP_BRD[row][column] == HIT or HIDDEN_COMP_BRD[row][column] == MISS:
            row, column = computer_input()
        if HIDDEN_COMP_BRD[row][column] == "X":
            HIDDEN_COMP_BRD[row][column] = HIT
            print(RED + "Computer HIT Ship" + WHITE)
        else:
            HIDDEN_COMP_BRD[row][column] = MISS
            print(YELLOW + "Computer MISSED Ship" + WHITE)
        
        if count_hits(HIDDEN_COMP_BRD) == MAX_SHIPS:
            print(RED + "SORRY... COMPUTER Hit all the ships. YOU LOSE")
            print(RED + "GAME OVER" + WHITE)
            break
        if count_hits(GUESS_BRD) == MAX_SHIPS:
            print(YELLOW + "CONGRADULATIONS! You hit all the battleships. \n")
            print(RED + "GAME OVER" + WHITE)
            break
        # print(GREEN + "You have " + str(turns) + " turns remaining.\n" + WHITE)
        if turns == 0:
            print(RED + "No more turns. Game Over.")
            break
        

def exit_game():
    """
    exits program
    """
    print(RED + "Exiting the program..." + WHITE)
    sys.exit(0)


def main():
    """
    Calls all functions to start game
    """
    print_rules()
    place_ships(HIDDEN_BRD)
    place_ships(HIDDEN_COMP_BRD)
    play_game()

        
if __name__ == "__main__":
    main()

# NB: figure out how to exit game during game run 
# get rid of turns
# create a clear terminal function and clear terminal with each turn
