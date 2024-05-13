# Import libraries
from random import randint
import random
import time
import sys

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

# Grid size variable can be adjusted 
GRID_SIZE = 8

# Generates 8 empty slots for game board
HIDDEN_BRD = [[CYAN + "~" + WHITE] * GRID_SIZE for x in range(GRID_SIZE)]
GUESS_BRD = [[CYAN + "~" + WHITE] * GRID_SIZE for x in range(GRID_SIZE)]

# Computer board for computer guess ?
HIDDEN_COMP_BRD = [[CYAN + "~" + WHITE] * GRID_SIZE for x in range(GRID_SIZE)]
COMP_GUESS_BRD = [[CYAN + "~" + WHITE] * GRID_SIZE for x in range(GRID_SIZE)]

# Converts letters to number/ position 
letters_to_numbers = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, 
                      "G" : 6, "H" : 7}

# Functions

def print_rules():
    """
    Prints rules of game to terminal 
    "Do you want to proceed Y/N" Text input to check
    if user wants to continue 
    """
    username = input(WHITE + "Please enter your username: " + CYAN)
    rules = input(WHITE + f"Welcome to Battleships {YELLOW + username.upper() + WHITE}!\nThere are 5 Ships to Hit, and 10 turns.\nHit ships will show" + RED + " X" + WHITE + "\nMissed ships will show" + YELLOW + " O" + WHITE + "\nDo you wish to continue? Y/N: ").upper()
    if rules != "Y":
        print(CYAN + "We're sorry to see you go!" + WHITE)
        exit_game()

    
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
    for ship in range(5):
        ship_row, ship_col = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_col] == "X":
            ship_row, ship_col = randint(0, 7), randint(0, 7)
        board[ship_row][ship_col] = "X"


def user_input():
    """
    Allows player to take their turn
    Validates their guess, Hit or Miss.
    If a user enters an invalid input, or NO input, 
    the input will run again until a user inputs a valid input.
    """
    row = input("\nPlease enter a ROW (1-8): ")
    # Letters to numbers.values() didn't work without creating errors
    while row not in "12345678":
        print(RED + "Invalid Input. Please enter a number(1-8)\n" + WHITE)
        row = input("\nPlease enter a ROW (1-8): ")
    column = input("\nPlease enter a COLUMN (A-H): ").upper()
    # letters to numbers works here??
    while column not in letters_to_numbers.keys():
        print(RED + "Invalid Input. Please enter a letter(A-H)\n" + WHITE)
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
            if column == RED + "X" + WHITE:
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
        print(GREEN + "   COMPUTER GRID" + WHITE)
        create_board(HIDDEN_COMP_BRD)
        print(GREEN + "    PLAYER GRID" + WHITE)
        row, column = user_input()
        if GUESS_BRD[row][column] == "O":
            print(YELLOW + f"\nYou've already guessed that, PLEASE TRY AGAIN\n" + WHITE)
        elif HIDDEN_BRD[row][column] == "X":
            print(GREEN + "\nWell done! You hit the ship!\n" + WHITE)
            GUESS_BRD[row][column] = RED + "X" + WHITE
        else:
            print(YELLOW + "\nSorry, you missed!\n" + WHITE)
            GUESS_BRD[row][column] = YELLOW + "O" + WHITE
            turns -= 1
        
        if count_hits(GUESS_BRD) == 5:
            print(YELLOW + "CONGRADULATIONS! You hit all the battleships. \n")
            print(RED + "GAME OVER" + WHITE)
            break
        print(GREEN + "You have " + str(turns) + " turns remaining.\n" + WHITE)
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
    create_ships(HIDDEN_BRD)
    create_ships(HIDDEN_COMP_BRD)
    play_game()

    # Don't know how to fix?
    while user_input(row) or user_input(column) == "$":
        print("see you later!")
        exit_game
        


if __name__ == "__main__":
    main()