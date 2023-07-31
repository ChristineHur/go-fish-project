# Rename this file to the name of your game and delete this comment
# Names: Nymphaea, Fahad, Christine, Yiisam, Dylan, Brendan, Daniella
# Date: 7/26/2023

# Import statements
from card import Card
import random


# Program your game here!
# Name is either player or Computer
# Hand is the cards that the user has 
# Quartets are basically points


#shows the structure of the player
class Player():
    def __init__(self, name, hand, quartets=0):
        self.name = name
        self.hand = hand
        self.quartets = quartets

# Computer player and their mover
#
class Computer(Player):
    def move(self, deck):
# TODO: Automatically determine a move based on the current hand
# Randomly determine a player to target
            return None

# Human and their move
class Human(Player):
    def move(self, deck):
# TODO: Take in user input twice
# First time to ask who to ask about the card you want to ask about
# Second input will be the card number you want to ask about
        return None
    
def create_deck():
    deck = Card.new_deck()
    return deck

# Count the number of human / computer players
def human_count():
    bean_count = input("Please enter the number of human players you would like to play against (0-4)")
    if bean_count > 4 or bean_count < 0:
        print("Error: Invalid Input")
    else:
        return bean_count

def computer_count():
    comp_count = input("Please enter the number of computer players you would like to play against (1-4)")
    if comp_count > 4 or comp_count < 1:
        print("Error: Invalid Input")
    else:
        return comp_count
    
# Give each player 7 cards to start with
# Splice deck into 5 lists, 4 is the hands of each player, and last will be the actual "deck"
def give_hand(deck):
    user = deck[0:7]
    THECOMP = deck[7:14]
    SecondaryComp = deck[14:21]
    TheLastComp = deck[21:28]
    Actualdeck = deck[28:52]
    
def first_turn(current_turn):
    current_turn == "user"
#

def next_turn(current_turn):
    print("The turn right now is: " + current_turn)
    if current_turn == "user":
        return "user"
    if current_turn == "THECOMP":
        return "THECOMP"
    if current_turn == "THECOMP":
        return "SecLastComp"
    if current_turn == "SecLastComp":
        return "TheLastComp"
    if current_turn == "TheLastComp":
        return "user"
    print("The next turn will be: " + current_turn)

def check_for_quartet(self):
    for suit,value in self.hand.items(): 
        if value == 4: # Create variable for number of cards
            self.quartets.append(value)
            print '%s completed the book of %s\'s.' % (self.name,value)
            self.quartets += 1
            del self.hand[value]
    self.emptyCheck()
 
def player_move():
    if 
    

def go_fish(): # This is the main function return eNone


# Code that runs when script is called from terminal
# ex: python my_card_game.py
    if __name__ == "__main__":
        go_fish()
