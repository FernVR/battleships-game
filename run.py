# Import libraries
from random import randint
import random
import time
import sys
import os
import string

# ANSI Escape codes
BLUE = "\u001b[34m"
GREEN = "\u001b[32m"
RED = "\u001b[31m"
YELLOW = "\u001b[33m"
CYAN = "\u001b[36m"
WHITE = "\u001b[37;1m"  # "BRIGHT/BOLD White"

# LEGEND 
# "X" for placing battleship and hit battleship
# "~" for available space
# "O" for missed shot

HIT = RED + "X" + WHITE
MISS = YELLOW + "O" + WHITE
AVAILABLE = CYAN + "~" + WHITE

# Grid size and No. of ships can be adjusted 
GRID_SIZE = 6
MAX_SHIPS = 5

# creates empty board using grid size and available symbols
create_empty_board = lambda: [[AVAILABLE] * GRID_SIZE for _ in range(GRID_SIZE)]

# Creates boards for player guesses
HIDDEN_BRD = create_empty_board()
COMPUTER_BRD = create_empty_board()

# Computer board for computer guesses
PLAYER_BRD = create_empty_board()

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
        \n1. You will be looking for hidden ships on the computer's grid. 
        \n2. The computer will guess for the ships on your grid.
        \n3. You will be asked for a row (a NUMBER) and a column (a LETTER).
        \n4. The winner is the player that guesses all the ships first!
        \n5. You have 20 guesses. The winner will be the player with the most hits at the end.
        \n6. To EXIT the game, type the letter "Q" (CAPITALIZE IT!)
           into any input, and you will exit the game.

           <<<<-------- HAVE FUN!!! --------->>>>
        """

# Functions

def exit_game():
    """
    exits program
    """
    print(BLUE + "Thanks for playing!")
    print(RED + "Exiting the program..." + WHITE)
    sys.exit(0)


def clear_terminal():
    """
    clears terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


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
    while True:
        try:
            row = input("\nPlease enter a ROW (1-6): ")
            if row == "Q":
                exit_game()
            # this secion explained bug in readme
            if row not in ["1", "2", "3", "4", "5", "6"] or row == "":
                raise ValueError
            if row in ["1", "2", "3", "4", "5", "6"]:
                row = int(row) - 1
                break
        except ValueError:
            print(RED + "Invalid Input. Please enter a number(1-6)\n" + WHITE)

    while True:
        try:
            column = input("\nPlease enter a COLUMN (A-F): ").upper()
            if column == "Q":
                exit_game()
            if column not in BOARD_ROW_TO_COLUMNS_MAP.keys():
                raise KeyError
            if column in BOARD_ROW_TO_COLUMNS_MAP.keys():
                column = BOARD_ROW_TO_COLUMNS_MAP[column]
                break
        except KeyError:
            print(RED + "Invalid Input. Please enter a letter(A-F)\n" + WHITE)
    return row, column


def count_hits(board):
    """
    counts hits on board and increments count
    """
    count = 0
    for row in board:
        for column in row:
            if column == HIT:
                count += 1
    return count


def computer_input():
    """
    Generates two random integars 
    """
    return random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)


def play_game():
    """
    plays game
    creates 20 turns for a user 
    places miss and hit symbols where the user guesses
    checks if user has already made the same move and notifies them
    """
    turns = 20
    while turns > 0:
        # print_board(HIDDEN_BRD)
        # print("hidden player board : test")
        print_board(PLAYER_BRD)
        print(GREEN + f" {USERNAME.upper()}'S GRID" + WHITE)
        print_board(COMPUTER_BRD)
        print(GREEN + "COMPUTER'S GRID" + WHITE)
        row, column = user_input()
        if COMPUTER_BRD[row][column] == MISS:
            print(YELLOW + f"\nYou've already guessed that, PLEASE TRY AGAIN" + WHITE)
        elif HIDDEN_BRD[row][column] == "X":
            print(GREEN + "\nWell done! You hit the ship!" + WHITE)
            COMPUTER_BRD[row][column] = HIT
            turns -= 1
        else:
            print(YELLOW + "\nSorry, you missed!" + WHITE)
            COMPUTER_BRD[row][column] = MISS
            turns -= 1
        
        # Computer Turn
        row, column = computer_input()
        while PLAYER_BRD[row][column] == HIT or PLAYER_BRD[row][column] == MISS:
            row, column = computer_input()
        if PLAYER_BRD[row][column] == "X":
            PLAYER_BRD[row][column] = HIT
            print(RED + "Computer HIT Ship" + WHITE)
        else:
            PLAYER_BRD[row][column] = MISS
            print(YELLOW + "Computer MISSED Ship" + WHITE)
        
        # If 5 ships are hit from either player the game will end
        if count_hits(PLAYER_BRD) == MAX_SHIPS:
            print(RED + "\nSORRY... COMPUTER Hit all the ships. YOU LOSE")
            print(RED + "\nGAME OVER" + WHITE)
            break
        if count_hits(COMPUTER_BRD) == MAX_SHIPS:
            print(YELLOW + "\nCONGRADULATIONS! You hit all the battleships.")
            print(RED + "\nGAME OVER" + WHITE)
            break
        print(BLUE + "You have " + str(turns) + " turns remaining." + WHITE)

        # When turns = 0 the game ends and the results are printed
        if turns == 0:
            player_hits = count_hits(COMPUTER_BRD)
            computer_hits = count_hits(PLAYER_BRD)

            if player_hits > computer_hits:
                print(GREEN + "\nCongratulations! You win with",  player_hits, "hits!")
            elif computer_hits > player_hits:
                print(BLUE + "\nSorry, the computer wins with", computer_hits, "hits!")
            else:
                print(YELLOW + "\nIt's a tie! Both have", player_hits, "hits.")

            print(RED + "\nNo more turns. GAME OVER.")
            break
    

def main():
    """
    Calls all functions to start game
    """
    print_rules()
    place_ships(HIDDEN_BRD)
    place_ships(PLAYER_BRD)
    play_game()

        
if __name__ == "__main__":
    main()

