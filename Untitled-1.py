def check_for_quartet(hand): # Check to see if there is a quartet
    # Use a dictionary, run over the list and check for each number
    # If any of the dict values are equal to 4
    dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
    for card in hand:
       dict[card.value] += 1
    for x in dict.values(): # This checks if the value of the dictionary is equal to 4 (if the hand has 4 of the same card)
        if x == 4:
            return x # Returns the number that is a quartet