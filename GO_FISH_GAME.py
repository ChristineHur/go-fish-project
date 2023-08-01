# Rename this file to the name of your game and delete this comment
# Names: Nymphaea, jah, Christine, Dylan, Brendan, Daniella
# Date: 7/26/2023
#start

# Import statements
from card import Card
import random


# Program your game here!
# Name is either player or Computer
# Hand is the cards that the user has 
# Quartets are basically points


#shows the structure of the player
# class Player():
#     def __init__(self, name, hand, quartets=0):
#         self.name = name
#         self.hand = hand
#         self.quartets = quartets


# Human and their move
# class Human(Player):
#      def move(self):
#         print("These are the cards in your hand: " + self.hand)
#         number = input("What card do you want to ask for? ")
#         for value in self.hand:
#             if value != number:
#                 print("Choose from the values that you have.")

def create_deck():
    deck = Card.new_deck()
    return deck

# Give each player 7 cards to start with
# Splice deck into 3 lists, 7 card per hand with 2 players (1 user and 1 computer), and last will be the actual "deck"
def give_hand(deck):
    user = deck[0:7]
    THECOMP = deck[7:14]
    the_deck = deck[14:52]

def player_move(user_hand, comp_hand, the_deck):
    print("These are the cards in your hand: " + user_hand)
    for value in user_hand:
        number = input("What card do you want to ask for? ")
        if value[0] != number:
            print("Choose from the values that you have.")
        else:
            for index in range(len(comp_hand)):
                if comp_hand[index][0] == value:
                    print("The other has that card!")
                    card = comp_hand.pop(index)
                    user_hand.append(card)
                else:
                    print("The other doesn't have that card! Go fish!!")
                    fish = the_deck.pop()
                    user_hand.append(fish)



def comp_move(com_hand, use_hand, deck_hand):
    random_num = random.randint(len(com_hand))
    number = com_hand[random_num][0]
    print("The computer wants to know if you have " + number)
    for index in range(len(use_hand)):
        if use_hand[index][0] == number:
            print("You have that card!")
            card = use_hand.pop(index)
            com_hand.append(card)
        else:
            print("Go fish! The computer has to pick up a card.")
            ran = deck_hand.pop()
            com_hand.append(ran)



def check_for_quartet(hand): # Check to see if there is a quartet
    for i in hand:
        
        return None

def is_quartet(hand):
    return None
    

def go_fish(deck): # This is the main function 
    user_quartet = 0
    comp_quartet = 0

# Code that runs when script is called from terminal
# ex: python my_card_game.py
    if __name__ == "__main__":
        go_fish()
