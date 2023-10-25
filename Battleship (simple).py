# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15

@author: ktk
"""

import random
# Initialize the game board
board = []
# Create the game board
for _ in range(5):
    board.append(["O"] * 5)
# Function to display the game board
def print_board(board):
    for row in board:
        print(" ".join(row))
# Function to generate random coordinates for the AI battleship
def random_row(board):
    return random.randint(0, len(board) - 1)
def random_col(board):
    return random.randint(0, len(board[0]) - 1)
# AI battleship location
ai_ship_row = random_row(board)
ai_ship_col = random_col(board)
print("Welcome to Battleship!")
print_board(board)
# Main game loop
for turn in range(4):
    print(f"Turn {turn + 1}")
    # Player's guess
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Col: ")) - 1
    if guess_row == ai_ship_row and guess_col == ai_ship_col:
        print("Congratulations! You sank the AI's battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed the AI's battleship!")
            board[guess_row][guess_col] = "X"
        print_board(board)
    if guess_row == ai_ship_row and guess_col == ai_ship_col:
        break
    # AI's turn
    ai_guess_row = random_row(board)
    ai_guess_col = random_col(board)
    if ai_guess_row == ai_ship_row and ai_guess_col == ai_ship_col:
        print("The AI sunk your battleship! Game over.")
        break
    else:
        if board[ai_guess_row][ai_guess_col] == "X":
            print("The AI guessed that one already.")
        else:
            print("The AI missed your battleship!")
            board[ai_guess_row][ai_guess_col] = "X"
        print_board(board)
if ai_guess_row != ai_ship_row or ai_guess_col != ai_ship_col:
    print("The AI ran out of turns. You win!")

