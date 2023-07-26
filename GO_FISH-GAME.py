# Rename this file to the name of your game and delete this comment
# Names: Nymphaea, Fahad, Christine, Yiisam, Dylan, Brendon, Daniella
# Date: 7/26/2023

# Import statements
from card import Card
import random


# Program your game here!
# Name is either player or Computer
# Hand is the cards that the user has 
# Quartets are basically points

#REPRESENTS THE PLAYERS PLAY STRUCTURE 
class Player():
    def __init__(self, name, hand, quartets=0):
        self.name = name
        self.hand = hand
        self.quartets = quartets

# Computer player and their mover
# REPRESENTS THE COMPUTER ANF THEIR MOVEMENTS 
class Computer(Player):
    def move(self, deck):
            return None

# Human /you and their move
class Human(Player):
    def move(self, deck):
# TODO: Take in user input
        return None
    
def go_fish():
    deck = Card.new_deck()
    print(deck)
    user = 

# Give each player 7 cards to start with

def give_hand():
    return None
# Splice deck into 5 lists, 4 is the hands of each player, and last will be the actual "deck"

def next_turn(current_turn):
    print("The turn right now is: " + current_turn)
    if current_turn == "user":
        return "THE COMP"
    if current_turn == "THE COMP":
        return "SecondaryComp"
    if current_turn == "Secondary omp":
        return "The last comp :("
    if current_turn == "The last comp :(":
        return "user"
 
# Code that runs when script is called from terminal
# ex: python my_card_game.py
if __name__ == "__main__":
    go_fish()
