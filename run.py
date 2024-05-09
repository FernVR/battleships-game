from random import randint
import random

# LEGEND 
# "X" for placing battleship and hit battleship
# "~" for available space
# "-" for missed shot


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
    username = input("Please enter your username: ")
    rules = input(f"Welcome to Battleships {username}! \n There are 5 Ships to Hit, and 10 turns. Do you wish to continue? Y/N: ")
    if rules == "n":
        print("We're sorry to see you go!")
    else: 
        pass
    
def create_board(board):
    """
    creates player grid 
    prints grids to terminal
    """
    print("\n  A B C D E F G H")
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

def user_input():
    """
    Allows player to take their turn
    Validates their guess, Hit or Miss.
    """
    row = input("\nPlease enter a ROW (1-8): ")
    while row not in "12345678":
        print("Invalid Input. Please enter a number(1-8)\n")
        row = input("\nPlease enter a ROW (1-8): ")
    column = input("\nPlease enter a COLUMN (A-H): ").upper()
    while column not in "ABCDEFGH":
        print("Invalid Input. Please enter a letter(A-H)\n")
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
            if column == "X":
                count += 1
    return count

def play():
    """
    function to start game
    """
    print_rules()
    create_ships(HIDDEN_BRD)
    create_board(HIDDEN_BRD)

    turns = 10
    while turns > 0:
        create_board(GUESS_BRD)
        row, column = user_input()
        if GUESS_BRD[row][column] == "-":
            print(f"\nYou've already guessed that, PLEASE TRY AGAIN\n")
        elif HIDDEN_BRD[row][column] == "X":
            print("\nWell done! You hit the ship!\n")
            GUESS_BRD[row][column] = "X"
            turns -= 1
        else:
            print("\nSorry, you missed!\n")
            GUESS_BRD[row][column] = "O"
            turns -= 1
        
        if count_hits(GUESS_BRD) == 5:
            print("CONGRADULATIONS! You hit all the battleships. \n")
            print("GAME OVER")
            break
        print("You have " + str(turns) + " turns remaining.\n")
        if turns == 0:
            print("No more turns. Game Over.")
            break
        



play_game = play()


