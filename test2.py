import random

cards = {
    "A": 11, 
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

card1 = None
card2 = None


def generate_card(dealer_card=False):
        if card1 != None and card1[0] == "A" and dealer_card == False: # if first card is ace, dont give jqk
            random_card = random.choice(list(cards.keys())[0:9])
        elif card1 != None and (card1[0] == "J" or card1[0] == "Q" or card1[0] == "K") and dealer_card == False: # if first card is jqk, dont give ace
            random_card = random.choice(list(cards.keys())[1:9]) # removed ace
        else:
            random_card = random.choice(list(cards.keys())) # else just do it normally 
        return (random_card, cards[random_card]) # display and val 

print(list(cards.keys())[1:])