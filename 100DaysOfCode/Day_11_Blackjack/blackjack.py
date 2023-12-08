import random
# face_card_dict = {
#     "A": [1, 11],
#     "K": 10,
#     "Q": 10,
#     "J": 10,
# }

def deal_cards():
    return [random.choice(cards), random.choice(cards)]

def add_card():
    return random.choice(cards)

def dealer_hit_16(dealer_hand):
    while sum_hand(dealer_hand) < 17:
        dealer_hand.append(add_card())
    return dealer_hand

def sum_hand(hand):
    total = sum(hand)
    aces_count = hand.count(11)

    while total > 21 and aces_count:
        total -= 10 
        aces_count -= 1

    return total


def is_bust(hand):
    return sum_hand(hand) > 21

def play_blackjack():
    player_hand = deal_cards()
    dealer_hand = deal_cards()
    print(f"Your Cards: {player_hand}")
    print(f"Dealer's Cards: [{dealer_hand[0]}, Hidden]")

    while True:
        if sum_hand(player_hand) == 21:
            return "Blackjack! You win!"

        choice = input("Type 'hit' or 'stay': ").lower()
        if choice == 'hit':
            player_hand.append(add_card())
            print(f"Your Cards: {player_hand}")
            if is_bust(player_hand):
                return "Busted! Sorry, you lost."
        else:
            break

    print(f"Dealer's Cards: {dealer_hand}")
    dealer_hand = dealer_hit_16(dealer_hand)
    if is_bust(dealer_hand):
        return f"Dealer busts. You win! Your hand: {player_hand}"

    if sum_hand(player_hand) > sum_hand(dealer_hand):
        return f"You win! Your hand: {player_hand}, Dealer's hand: {dealer_hand}"
    elif sum_hand(player_hand) == sum_hand(dealer_hand):
        return f"Draw! Your hand: {player_hand}, Dealer's hand: {dealer_hand}"
    else:
        return f"You lost! Your hand: {player_hand}, Dealer's hand: {dealer_hand}"

# cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10s and face cards are all worth 10, 11 for Aces
cards = [11, 11]  # 10s and face cards are all worth 10, 11 for Aces


print("Welcome to Blackjack!")
while True:
    print(play_blackjack())
    if input("Play again? (y/n): ").lower() != 'y':
        break