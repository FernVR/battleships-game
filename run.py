from random import randint
import random


# Generates 8 empty slots for game board
HIDDEN_BRD = [["~"] * 8 for x in range(8)]
GUESS_BRD = [["~"] * 8 for x in range(8)]

# Converts letters to number/ position 
letters_to_numbers = {"A": 0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}

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

def create_board(board):
    """
    creates player grid 
    prints grids to terminal
    """
    print("  ///////////////")
    print("  A B C D E F G H")
    print("  ---------------")

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
    print("W E L C O M E // T O // B A T T L E S H I P!\n")
    create_ships(HIDDEN_BRD)
    create_board(HIDDEN_BRD)
    create_board(GUESS_BRD)

play_game = play()


