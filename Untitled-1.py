def player_move(user_hand, comp_hand, the_deck):
    print("These are the cards in your hand: " + user_hand)
    number = input("What card do you want to ask for? ")
    for value in user_hand:
        if value != number:
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
