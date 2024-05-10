# Import libraries
from random import randint
import random
import time

# ANSI Escape codes
blue = "\033[94m"
green = "\033[92m"
red = "\033[91m"
yellow = "\033[93m"
end_color = "\033[0m"

# LEGEND 
# "X" for placing battleship and hit battleship
# "~" for available space
# "O" for missed shot

# Generates 8 empty slots for game board
HIDDEN_BRD = [[blue + "~" + end_color] * 8 for x in range(8)]
GUESS_BRD = [[blue + "~" + end_color] * 8 for x in range(8)]

# Converts letters to number/ position 
letters_to_numbers = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, 
                      "G" : 6, "H" : 7}

# Creating functions we need:

def print_rules():
    """
    Prints rules of game to terminal 
    "Do you want to proceed Y/N" Text input to check
    if user wants to continue 
    """
    username = input(green + "Please enter your username: " + end_color)
    rules = input(f"Welcome to Battleships {yellow + username.upper() + end_color}!\nThere are 5 Ships to Hit, and 10 turns.\nHit ships will show" + red + " X" + end_color + "\nMissed ships will show" + yellow + " O" + end_color + "\nDo you wish to continue? Y/N: ").upper()
    if rules != "y":
        print("We're sorry to see you go!")
        # unable to exit loop here, figure out how to exit game?

    
    
    
    
def create_board(board):
    """
    creates player grid 
    prints grids to terminal
    """
    print("\n  A B C D E F G H")
    print("  ________________")

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
    while row not in "12345678":
        print(red + "Invalid Input. Please enter a number(1-8)\n" + end_color)
        row = input("\nPlease enter a ROW (1-8): ")
    column = input("\nPlease enter a COLUMN (A-H): ").upper()
    while column not in "ABCDEFGH":
        print(red + "Invalid Input. Please enter a letter(A-H)\n" + end_color)
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
            if column == red + "X" + end_color:
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
        create_board(GUESS_BRD)
        row, column = user_input()
        if GUESS_BRD[row][column] == "-":
            print(yellow + f"\nYou've already guessed that, PLEASE TRY AGAIN\n" + end_color)
        elif HIDDEN_BRD[row][column] == "X":
            print(green + "\nWell done! You hit the ship!\n" + end_color)
            GUESS_BRD[row][column] = red + "X" + end_color
        else:
            print(yellow + "\nSorry, you missed!\n" + end_color)
            GUESS_BRD[row][column] = yellow + "O" + end_color
            turns -= 1
            
        if count_hits(GUESS_BRD) == 5:
            print(yellow + "CONGRADULATIONS! You hit all the battleships. \n")
            print(red + "GAME OVER" + end_color)
            break
        print(green + "You have " + str(turns) + " turns remaining.\n" + end_color)
        if turns == 0:
            print(red + "No more turns. Game Over.")
            break
        


def main():
    """
    Calls all functions to start game
    """
    print_rules()
    create_ships(HIDDEN_BRD)
    create_board(HIDDEN_BRD)
    play_game()


start = main()