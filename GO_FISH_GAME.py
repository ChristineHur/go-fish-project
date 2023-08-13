# Rename this file to the name of your game and delete this comment
# Names: Nymphaea, jah, Christine, Dylan, Daniella
# Date: 7/26/2023
#start

# Import statements
from card import Card
import random


def create_deck(): # This creates a shuffled deck
    deck = Card.new_deck()
    return deck

"""
def player_move(user_hand, comp_hand, the_deck): # This is what happens when it is the player's turn
    print(f"These are the cards in your hand: {user_hand}")
    number = int(input("What card do you want to ask for? ")) # Takes in the number the player wants to ask the computer about
    for card in user_hand:
        if number == card.value:          
            for index in range(len(comp_hand)): # This checks if the computer has the number card
                if comp_hand.value == number: # This is if it does have it
                    print("The computer has that card!")
                    card = comp_hand.pop(index) # This takes the card out of the computer's hand                        
                    user_hand.append(card) # This puts it in the players hand
                else: # This is if the computer doesn't have it
                    print("The computer doesn't have that card! Go fish!!")
                    fish = the_deck.pop() # This takes the last card in the deck out
                    user_hand.append(fish) # This appends it to the player's hand
        else: # This is to check if the inputted number is in the player's hand
            print("Choose from the values you have.")
"""

def player_move_2(user_hand, comp_hand, the_deck):
    print(f"These are the cards in your hand: {user_hand}")
    # Ask for input
    loop = True
    # If there is a card in user_hand with number as its value...
    while loop == True:
        try: number = int(input("What card do you want to ask for? "))
        except ValueError: 
            print("That's not a number, please input a number.")
            continue
        if any(card.value == int(number) for card in user_hand):
            if any(cardi.value == int(number) for cardi in comp_hand):
                print("The computer has that card!")
                for card in comp_hand:
                    if card.value == number:
                        comp_hand.pop(comp_hand.index(card))
                        user_hand.append(card)
                # Check index where computer has it, pop that index, append to card
            else:
                print("Go fish! The computer doesm't have that card.")
                gofishes = the_deck.pop()
                user_hand.append(gofishes)
                print(f"You got a {gofishes}")
                print("")
                loop = False
        else:
            print("Please choose a number that you actually have.")
            print("")




def comp_move(com_hand, use_hand, deck_hand): # The same thing as player_move except on the computer's side
    loop = True
    while loop:
        random_num = random.randint(0, len(com_hand)-1)
        number = com_hand[random_num].value
        print(f"The computer wants to know if you have {number}.")
        if any(cardi.value == number for cardi in use_hand):
            print("You have that card!")
            for card in use_hand:
                if card.value == number:
                    com_hand.append(use_hand.pop(use_hand.index(card)))
                    print("")
              # Check index where computer has it, pop that index, append to card
        else:
            print("Go fish! The computer has to pick up a card.")
            print("")
            com_hand.append(deck_hand.pop())
            loop = False
    """
    for index in range(len(use_hand)):
        if any(lambda i : i.value == number for cardi in use_hand):
            print("You have that card!")
            card = use_hand.pop(index)
            com_hand.append(card)
        else:
            print("Go fish! The computer has to pick up a card.")
            ran = deck_hand.pop()
            com_hand.append(ran)
    """

def check_for_quartet(hand): # Check to see if there is a quartet
    # Use a dictionary, run over the list and check for each number
    # If any of the dict values are equal to 4
    dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
    for card in hand:
       dict[card.value] += 1
    for key in dict.keys(): # This checks if the value of the dictionary is equal to 4 (if the hand has 4 of the same card)
        if dict[key] == 4:
            return key # Returns the number that is a quartet
    return False

def remove_quartets(quartet, hand): # This will remove quartets and up the score of the player
    thenumber = check_for_quartet(hand)
    if thenumber != False:
        quartet += 1
        print(f"{hand=}".split('=')[0] +  " got a quartet!")
        for card in hand:
            if card.value == thenumber:
                hand.pop(hand.index(card))
    return quartet



def go_fish(deck): # This is the main function 
    user_quartet = 0
    comp_quartet = 0
    deck = create_deck()
    # Splitting up the deck 3 times, 2 is the hands being played, 1 for the rest of the deck
    user = deck[:7] # This is the user's hand (7 cards)
    THECOMP = deck[7:14] # This is the computer's hand (7 cards)
    the_deck = deck[14:] # This is the deck that cards will be taken from
    print(user)
    print(THECOMP)
    print(the_deck)
    print("Welcome to go fish! Please know that if you want to select a J, Q, K or A, you will have to write the input as 11, 12, 13, or 1 respectively.")
    print("")
    while len(user) != 0:
        user_quartet = remove_quartets(user_quartet, user)
        comp_quartet = remove_quartets(comp_quartet, THECOMP)
        print(f"You currently have {user_quartet} pile(s)!")
        print("The computer currently has " + str(comp_quartet) + " pile(s)!")
        print("")
        player_move_2(user, THECOMP, the_deck)
        comp_move(THECOMP, user, the_deck)
    if user_quartet > comp_quartet:
        print("Congrats! You win!")
    else:
        print("You lost! There's always next time.")


# Code that runs when script is called from terminal
# ex: python my_card_game.py
if __name__ == "__main__":
    deck = create_deck()
    go_fish(deck)
