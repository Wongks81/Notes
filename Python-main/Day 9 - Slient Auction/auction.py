import auction_art
import os
auction_bid ={}

def main():
    bidding_finish = False
    win_value = 0
    print(auction_art.logo)
    print("Welcome to the secret auction program.")
    
    while not bidding_finish:
        name = input("What is your name? : ")
        bid = int(input("What is your bid? : $"))
        auction_bid[name] = bid
        other_bidders = input("Are there any other bidders? Type 'yes' for new bidders.\n").lower()
        if other_bidders == "no":
            bidding_finish = True

        # Clears console screen
        os.system('cls')
    
    for name, bid in auction_bid.items():
        if bid > win_value:
            win_value = bid

            # Clear the old values and add the new {name:bid}
            win_bid = {}
            win_bid[name] = bid
            
        elif bid == win_value:
            # Add the name to the dictonary as both bids are same
            win_bid[name] = bid

    # Use for loop in the event there is multiple same bid
    for name,bid in win_bid.items():
        print(f"Winning person is {name} with bid price of ${bid}")

    

if __name__ =="__main__":
    main()