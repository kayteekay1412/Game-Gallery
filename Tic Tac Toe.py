# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14
@author: ktk
"""
# AI Tic Tac Toe

import numpy as np
# The game board
board = np.array([[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']])
# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")
# Function to check for a win
def check_win(board, player):
    for i in range(3):
        if all(board[i] == player) or all(board[:, i] == player):
            return True
    if all(np.diag(board) == player) or all(np.diag(np.fliplr(board)) == player):
        return True
    return False
# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return -1
    elif check_win(board, 'O'):
        return 1
    elif ' ' not in board:
        return 0
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score
# AI's move using Minimax
def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move
# Main game loop
while True:
    print_board(board)
    row, col = map(int, input("Enter your move (row and column): ").split())
    row,col=row-1,col-1
    if board[row][col] == ' ':
        board[row][col] = 'X'
    else:
        print("Invalid move. Try again.")
        continue
    if check_win(board, 'X'):
        print_board(board)
        print("You win!")
        break
    if ' ' not in board:
        print_board(board)
        print("It's a draw!")
        break
    ai_row, ai_col = ai_move(board)
    board[ai_row][ai_col] = 'O'
    if check_win(board, 'O'):
        print_board(board)
        print("AI wins!")
        break
    if ' ' not in board:
        print_board(board)
        print("It's a draw!")
        break
