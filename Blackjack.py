# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 23:21:39 2023

@author: ktk
"""

#AI Blackjack
import random
# Define card ranks, suits, and values
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
# Create a deck of cards
deck = [{"Rank": rank, "Suit": suit, "Value": value} for rank in ranks for suit in suits for value in values]
# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = sum(card["Value"] for card in hand)
    if value > 21 and any(card["Rank"] == "Ace" for card in hand):
        value -= 10  # Adjust for the value of Aces
    return value
# Function to display a player's hand
def display_hand(hand):
    for card in hand:
        print(f"{card['Rank']} of {card['Suit']}")
# Initialize player and dealer hands
player_hand = [random.choice(deck), random.choice(deck)]
dealer_hand = [random.choice(deck), random.choice(deck)]
# Main game loop
while True:
    print("\nPlayer's Hand:")
    display_hand(player_hand)
    player_value = calculate_hand_value(player_hand)
    print(f"Total Value: {player_value}")
    if player_value == 21:
        print("Blackjack! You win!")
        break
    elif player_value > 21:
        print("Bust! You lose.")
        break
    action = input("Do you want to 'Hit' or 'Stand'? ").strip().lower()
    if action == 'hit':
        player_hand.append(random.choice(deck))
    elif action == 'stand':
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(random.choice(deck))
        print("\nDealer's Hand:")
        display_hand(dealer_hand)
        dealer_value = calculate_hand_value(dealer_hand)
        print(f"Total Value: {dealer_value}")
        if dealer_value > 21:
            print("Dealer busts! You win!")
        elif dealer_value >= player_value:
            print("Dealer wins.")
        else:
            print("You win!")
        break
    else:
        print("Invalid choice. Please enter 'Hit' or 'Stand'.")
