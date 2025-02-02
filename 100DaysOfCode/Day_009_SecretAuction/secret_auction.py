bids = {}  # Dictionary to store bids: {name: bid_amount}
bidding = True

while bidding:
    auction = input("Would you like to start a bid (y/n): ").strip().lower()
    if auction == 'y':
        while True: # Loop for name input validation
            name = input("What's your name: ").strip().lower()
            if name.isalpha():
                break  # Exit the loop if the name is valid
            else:
                print("Invalid Input. Only use alphabetic characters.")

        while True: # Loop for bid input validation
            try:
                bid = int(input("How much would you like to bid: "))
                if bid > 0: # Ensure bid is positive
                    bids[name] = bid  # Store the bid
                    break # exit the loop if bid input is valid
                else:
                    print("Bid must be greater than 0")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif auction == 'n':
        bidding = False
        print("Auction ended.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# After the auction ends, you can process the bids to find the winner (example):
if bids:
    highest_bidder = max(bids, key=bids.get)
    highest_bid = bids[highest_bidder]
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
else:
    print("No bids were placed.")