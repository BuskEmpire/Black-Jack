import random
deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "Knight", "Knight", "Knight", "Knight", "Queen", "Queen", "Queen", "Queen", "King", "King", "King", "King", "Ace", "Ace", "Ace", "Ace"]
player_hand = []
house_hand = []
def PlayerHandValue(player_hand):
    player_hand_value = 0
    for card in player_hand:
        if isinstance(card, str) and not (card == "Ace"):
            player_hand_value += 10
            #return player_hand_value
        elif isinstance(card, int):
            player_hand_value += card
    return player_hand_value
def HouseHandValue(house_hand):
    house_hand_value = 0
    for card in house_hand:
        if isinstance(card, str) and not (card == "Ace"):
            house_hand_value += 10
        elif isinstance(card, int):
            player_hand_value += card
    return house_hand_value
def ace(player_hand_value):
    if player_hand_value + 11 > 21:
        ace = 1
        return ace + player_hand_value
    else:
        ace = 11
        return ace + player_hand_value
print("Welcome to Black Jack Betting!!")
play = input("Do you want to play?: ").lower()
while play == "yes":
    random.shuffle(deck)
    while len(player_hand) < 2:
        player_hand.append(deck.pop(0))
    while len(house_hand) < 1:
        house_hand.append(deck.pop(0))
    print("Your hand:",player_hand)
    print("Hand value:",PlayerHandValue(player_hand))
    hit_stand = input("Hit or stand?: ").lower()
    while hit_stand == "hit":
        player_hand.append(deck.pop(0))
        if PlayerHandValue(player_hand) > 21:
            print("Bust")
            hit_stand = "bust"
        print("Your hand:", player_hand)
        print("Hand value:", PlayerHandValue(player_hand))
        if hit_stand == "bust":
            # bust gör ...
        else:
            # inte bust
            hit_stand = input("Hit or stand?: ").lower()
    # om inte bust
    
    print("House hand:", house_hand)
    print("House hand value:", HouseHandValue(house_hand))
    while house_hand_value < player_hand_value and house_hand_value != 17:
        house_hand.append(deck.pop(0))
        print("House hand:", house_hand)
        print("House hand value:", HouseHandValue(house_hand))
    if house_hand_value > player_hand_value:
        print("Dealer wins")
    if house_hand_value == 17:
        print("Soft 17")
        if player_hand_value > house_hand_value:
            print("Player wins")
        elif house_hand_value > player_hand_value:
            print("Dealer wins")
        elif house_hand_value == player_hand_value:
            print("Draw")
    if house_hand_value > 21:
        print("Dealer bust, player wins")
    
    
    
print(ace(16))
