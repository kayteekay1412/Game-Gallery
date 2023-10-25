# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14
@author: ktk
"""
#AI Rock Paper Scissors
import random
def get_user_choice():
    user_choice = input("Rock, Paper, or Scissors? ").strip().lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Please choose Rock, Paper, or Scissors: ").strip().lower()
    return user_choice
def get_ai_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def determine_winner(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and ai_choice == "scissors") or
        (user_choice == "scissors" and ai_choice == "paper") or
        (user_choice == "paper" and ai_choice == "rock")
    ):
        return "You win!"
    else:
        return "AI wins!"
while True:
    user_choice = get_user_choice()
    ai_choice = get_ai_choice()
    print(f"You chose {user_choice}, and AI chose {ai_choice}.")
    result = determine_winner(user_choice, ai_choice)
    print(result)
    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break
