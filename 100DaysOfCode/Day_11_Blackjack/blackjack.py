import random as rand
face_card_dict = {
    "A": [1, 11],
    "K": 10,
    "Q": 10,
    "J": 10,
}

non_face_card = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


def deal_cards():
    first = rand.choice(non_face_card)
    second = rand.choice(non_face_card)
    return[first, second]


def add_card():
    return rand.choice(non_face_card)


def dealer_hit_16(dealer):
    hit_16_dealer_list = dealer
    dealer_total = sum(dealer)
    if dealer_total < 17:
        hit_16_dealer_list.append(add_card())
    else:
        return hit_16_dealer_list
    

def play_bj():
    player_cards = deal_cards()
    print(f"Your Cards: {player_cards}")
    dealer_cards = deal_cards()
    print(f"Dealer Cards: {dealer_cards}")
    hit_or_stay = str(input("Type either, 'hit' or 'stay': ")).strip().lower()
    if hit_or_stay == "hit": 
        add_card()
    else:
        dealer_hit_16()
        
        
print("Welcome to Blackjack!")
playing = True
while playing: 
    
    play_bj()
    play_again = str(input("Would you like to play again 'y' or 'n': ")).strip().lower()
    if play_again == "y":
        continue
    else:
        playing = False