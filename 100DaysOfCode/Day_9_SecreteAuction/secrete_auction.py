def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder, bid in bids.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    return winner, highest_bid

auction_bids = {}

print("Welcome to the Secret Auction!")

while True:
    name = input("What is your name?: ").strip().lower()

    try:
        bid_amount = int(input("What is your bid?: $"))
    except ValueError:
        print("Please enter a valid number for your bid.")
        continue

    auction_bids[name] = bid_amount
    # print(f"Bid of ${bid_amount} accepted from {name.title()}.")

    other_bids = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
    if other_bids != 'yes':
        break

winner, highest_bid = find_highest_bidder(auction_bids)
print(f"\nThe winner is {winner.title()} with a bid of ${highest_bid}.")
