# Rename this file to the name of your game and delete this comment
# Names: Nymphaea, jah, Christine, Dylan, Brendan, Daniella
# Date: 7/26/2023
#start

# Import statements
from card import Card
import random


def create_deck(): # This creates a shuffled deck
    deck = Card.new_deck()
    return deck

def player_move(user_hand, comp_hand, the_deck): # This is what happens when it is the player's turn
    print("These are the cards in your hand: " + user_hand)
    for value in user_hand:
        number = input("What card do you want to ask for? ") # Takes in the number the player wants to ask the computer about
        if value[0] != number: # This is to check if the inputted number is in the player's hand
            print("Choose from the values that you have.")
        else: # This checks if the computer has the number card
            for index in range(len(comp_hand)):
                if comp_hand[index][0] == value: # This is if it does have it
                    print("The computer has that card!")
                    card = comp_hand.pop(index) # This takes the card out of the computer's hand
                    user_hand.append(card) # This puts it in the players hand
                else: # This is if the computer doesn't have it
                    print("The computer doesn't have that card! Go fish!!")
                    fish = the_deck.pop() # This takes the last card in the deck out
                    user_hand.append(fish) # This appends it to the player's hand



def comp_move(com_hand, use_hand, deck_hand): # The same thing as player_move except on the computer's side
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
    # Use a dictionary, run over the list and check for each number
    # If any of the dict values are equal to 4
    dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
    for card in hand:
       dict[card.value] += 1
    for x in dict.value(): # This checks if the value of the dictionary is equal to 4 (if the hand has 4 of the same card)
        if x == 4:
            return x # Returns the number that is a quartet

def remove_quartets(quartet, hand):
    value = check_for_quartet(hand)
    for i in len(hand - 1):
        if i.value == value:
            hand.pop(i)
            quartet += 1
    

def go_fish(deck): # This is the main function 
    user_quartet = 0
    comp_quartet = 0
    deck = create_deck()
    # Splitting up the deck 3 times, 2 is the hands being played, 1 for the rest of the deck
    user = deck[0:7] # This is the user's hand (7 cards)
    THECOMP = deck[7:14] # This is the computer's hand (7 cards)
    the_deck = deck[14:52] # This is the deck that cards will be taken from
    while len(user) != 0:
        player_move(user, THECOMP, the_deck)
        comp_move(THECOMP, user, the_deck)
        check_for_quartet(user)
        check_for_quartet(THECOMP)


# Code that runs when script is called from terminal
# ex: python my_card_game.py
    if __name__ == "__main__":
        go_fish()
