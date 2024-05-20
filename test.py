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

SYMBOL_HIT = RED + "X" + WHITE
MISS = YELLOW + "O" + WHITE
AVAILABLE = CYAN + "~" + WHITE

# Grid size variable can be adjusted 
GRID_SIZE = 6
MAX_SHIPS = 5

create_empty_board = lambda: [[CYAN + AVAILABLE + WHITE] * GRID_SIZE for _ in range(GRID_SIZE)]


# Generates 8 empty slots for game board
HIDDEN_BRD = create_empty_board()
GUESS_BRD = create_empty_board()

# Computer board for computer guess ?
HIDDEN_COMP_BRD = create_empty_board()
COMP_GUESS_BRD = create_empty_board()

# Converts letters to number/ position 
# letters_to_numbers = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, 
#                       "G" : 6, "H" : 7}

BOARD_ROW_TO_COLUMNS_MAP = dict(zip(string.ascii_uppercase[0: GRID_SIZE], range(GRID_SIZE)))

# CONST Variables
USERNAME = input(WHITE + "Please enter your username: " + CYAN)
if USERNAME == "":
    USERNAME = "PLAYER"

RULES = f"""
        Welcome to Battleships, {YELLOW + USERNAME.upper() + WHITE}!
        --------------------------------
        Rules are as follows:
        1. 
        2.
        3.
        4.
        5.
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

import string
    
def create_board(board):
    """
    creates player grid 
    prints grids to terminal
    """
    alphabets = "   ".join(string.ascii_uppercase[0: GRID_SIZE].split())
    print(f"\n {alphabets}") 
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
        

def create_ships(board):
    """
    Creates ships with random numbers from grid size
    """
    for _ in range(MAX_SHIPS):
        while True:
            ship_row, ship_col = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)
            if board[ship_row][ship_col] != SYMBOL_HIT:
                board[ship_row][ship_col] = SYMBOL_HIT
                break

        # while board[ship_row][ship_col] == "X":
        #     ship_row, ship_col = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE -1)
        


"At any time during the game press e to exit"
def user_input():
    """
    Allows player to take their turn
    Validates their guess, Hit or Miss.
    If a user enters an invalid input, or NO input, 
    the input will run again until a user inputs a valid input.
    """
    try:
        
        while True:
            row = input("\nPlease enter a ROW (1-8): ")
            if row == "exit":
                exit_game()
            
            row = int(row)
            if row in BOARD_ROW_TO_COLUMNS_MAP.values():
                break
            raise ValueError()
    except ValueError:
        print(RED + "Invalid Input. Please enter a number(1-8)\n" + WHITE)

    column = input("\nPlease enter a COLUMN (A-H): ").upper()
    if column == "exit":
        exit_game()
        
    while column not in BOARD_ROW_TO_COLUMNS_MAP.keys():
        print(RED + "Invalid Input. Please enter a letter(A-H)\n" + WHITE)
        column = input("\nPlease enter a COLUMN (A-H): ").upper()
    return int(row) - 1, BOARD_ROW_TO_COLUMNS_MAP[column]


def count_hits(board):
    count = 0
    for row in board:
        for column in row:
            if column == RED + SYMBOL_HIT + WHITE:
                count += 1
    return count

# to be deleted?
def computer_input():
    """
    Generates computer turn
    Validates the guess, Hit or Miss
    """
    return random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)

def print_info(msg):
    print(WHITE + f"\n{msg}\n" + WHITE)

NO_MOVE = 1
HIT = 2
MISS = 3

def make_move(board, user:bool, row, column):
    if board[row][column] == SYMBOL_MISS:
        if user:
            print_info(f"You've already guessed that, PLEASE TRY AGAIN")
        return NO_MOVE
    
    if board[row][column] == SYMBOL_HIT:
        if user:
            print(GREEN + "\nWell done! You hit the ship!\n" + WHITE)
        board[row][column] = RED + SYMBOL_HIT + WHITE
        return HIT
    
    else:
        if user:
            print(YELLOW + "\nSorry, you missed!\n" + WHITE)
        board[row][column] = YELLOW + MISS + WHITE
        return MISS

def game_over():
    user_hits = count_hits(GUESS_BRD)
    computer_hits = count_hits(COMPTER_BRD)

    if user_hits == MAX_SHIPS and computer_hits == MAX_SHIPS:
        print("its a tie")
        return True

    if user_hits == MAX_SHIPS:
        print("user won")
        return True

    return False

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
        create_board(HIDDEN_BRD)
        print("hidden player board : test")
        create_board(HIDDEN_COMP_BRD)
        print(GREEN + f"   {USERNAME.upper()}'S GRID" + WHITE)
        create_board(GUESS_BRD)
        print(GREEN + "  COMPUTER'S GRID" + WHITE)
        while True:
            row, column = user_input()
            # if GUESS_BRD[row][column] == SYMBOL_MISS:
            #     print(YELLOW + f"\nYou've already guessed that, PLEASE TRY AGAIN\n" + WHITE)
            # elif HIDDEN_BRD[row][column] == "X":
            #     print(GREEN + "\nWell done! You hit the ship!\n" + WHITE)
            #     GUESS_BRD[row][column] = RED + SYMBOL_HIT + WHITE
            # else:
            #     print(YELLOW + "\nSorry, you missed!\n" + WHITE)
            #     GUESS_BRD[row][column] = YELLOW + MISS + WHITE
            #     turns -= 1
            move_made = make_move(GUESS_BRD, True, row, column)
            if move_made != NO_MOVE:
                break

        
        # Computer Turn
        while True:
            row, column = computer_input()
            move_made = make_move(HIDDEN_COMP_BRD, False, row, column)

            if move_made == NO_MOVE:
                continue

            if HIT:
                print(RED + f"Computer SYMBOL_HIT Ship at: " + str(row) + "," + str(column) + WHITE)
                break
            if MISS:
                print(YELLOW + f"Computer MISSED Ship at: " + str(row) + "," + str(column) + WHITE)
                break


        # while HIDDEN_COMP_BRD[row][column] == RED + SYMBOL_HIT + WHITE or HIDDEN_COMP_BRD[row][column] == YELLOW + MISS + WHITE:
        #     row, column = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        # if HIDDEN_COMP_BRD[row][column] == "X":
        #     HIDDEN_COMP_BRD[row][column] = RED + SYMBOL_HIT + WHITE
        #     print(RED + f"Computer SYMBOL_HIT Ship at: " + str(row) + "," + str(column) + WHITE)
        # else:
        #     HIDDEN_COMP_BRD[row][column] = YELLOW + MISS + WHITE
        #     print(YELLOW + f"Computer MISSED Ship at: " + str(row) + "," + str(column) + WHITE)

        # if count_hits(HIDDEN_COMP_BRD) == 5:
        #     print(RED + "SORRY... COMPUTER Hit all the ships. YOU LOSE")
        #     print(RED + "GAME OVER" + WHITE)
        #     break

        
        if game_over():
            sys.exit()

        # if count_hits(GUESS_BRD) == MAX_SHIPS:
        #     print(YELLOW + "CONGRADULATIONS! You hit all the battleships. \n")
        #     print(RED + "GAME OVER" + WHITE)
        #     break
        # # print(GREEN + "You have " + str(turns) + " turns remaining.\n" + WHITE)
        # if turns == 0:
        #     print(RED + "No more turns. Game Over.")
        #     break
        

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
    create_ships(HIDDEN_BRD)
    create_ships(HIDDEN_COMP_BRD)
    play_game()

        
if __name__ == "__main__":
    main()