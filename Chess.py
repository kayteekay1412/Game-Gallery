# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 23:36:44 2023

@author: ktk
"""

import chess
import chess.svg

# #Single Player
# def play_chess():
#     board = chess.Board()
#     while not board.is_game_over():
#         print(board)
#         move = input("Enter your move (e.g., 'e2e4'): ")
#         try:
#             chess.Move.from_uci(move)
#             if chess.Move.from_uci(move) in board.legal_moves:
#                 board.push(chess.Move.from_uci(move))
#             else:
#                 print("Invalid move. Try again.")
#         except ValueError:
#             print("Invalid move format. Try again.")
#     print("Game Over")
#     if board.is_checkmate():
#         print("Checkmate!")
#     elif board.is_stalemate():
#         print("Stalemate!")
#     elif board.is_insufficient_material():
#         print("Insufficient material to checkmate!")
#     elif board.is_seventyfive_moves():
#         print("Draw (75-move rule)!")
#     elif board.is_fivefold_repetition():
#         print("Draw (fivefold repetition)!")
#     elif board.is_variant_draw():
#         print("Draw (variant-specific rule)!")
#     else:
#         print("Game result: " + board.result())
# if __name__ == "__main__":
#     play_chess()

# #Vs AI
# def play_chess():
#     board = chess.Board()

#     while not board.is_game_over():
#         if board.turn:  # Player's turn
#             print(board)
#             move = input("Enter your move (e.g., 'e2e4'): ")
#             try:
#                 if chess.Move.from_uci(move) in board.legal_moves:
#                     board.push(chess.Move.from_uci(move))
#                 else:
#                     print("Invalid move. Try again.")
#             except ValueError:
#                 print("Invalid move format. Try again.")
#         else:  # AI's turn
#             import random
#             legal_moves = list(board.legal_moves)
#             ai_move = random.choice(legal_moves)
#             print(f"AI plays: {ai_move.uci()}")
#             board.push(ai_move)
#     print("Game Over")
#     if board.is_checkmate():
#         print("Checkmate!")
#     elif board.is_stalemate():
#         print("Stalemate!")
#     elif board.is_insufficient_material():
#         print("Insufficient material to checkmate!")
#     elif board.is_seventyfive_moves():
#         print("Draw (75-move rule)!")
#     elif board.is_fivefold_repetition():
#         print("Draw (fivefold repetition)!")
#     elif board.is_variant_draw():
#         print("Draw (variant-specific rule)!")
#     else:
#         print("Game result: " + board.result())
# if __name__ == "__main__":
#     play_chess()