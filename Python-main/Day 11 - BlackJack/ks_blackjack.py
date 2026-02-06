import random
import blackjack_art
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []

def main():
    get_card = True
    get_dealer_card = True
    
    print(blackjack_art.logo)

    # Deal 2 cards for the first round using a for loop 
    for card in range(0,2):
        deal_card(player_cards)
        deal_card(dealer_cards)

    # Continue to add card to list when get_card is true
    while get_card:
        os.system("cls")
        # Print out the player's list of cards
        print(f"Your Cards: {player_cards}")
        print(f"Dealer's first card {dealer_cards[0]}")

        # Do a check on player's total card points
        player_total = card_points(player_cards)
        print(f"Total points is : {player_total}")
        
        if player_total <= 16:
            print("Total less than 16, issuing card...")
            deal_card(player_cards)
        elif player_total > 21:
            print("You have exceeded 21! BUSTED!")
            get_card = False
        else:
            get_another = input("Type 'y' to get another card :") or 'n'
            if get_another.lower() == 'y':
                deal_card(player_cards)
            else:
                get_card = False

    # while loop for dealer card
    while get_dealer_card:
        dealer_total = card_points(dealer_cards)
        if dealer_total > 21:
            print(f"Dealer's Cards: {dealer_cards}")
            print(f"Dealer hand is Busted with {dealer_total} points")
            get_dealer_card = False
        elif dealer_total <= 17 or dealer_total < player_total:
            deal_card(dealer_cards)
        else:
            print(f"Dealer's Cards: {dealer_cards}")
            print(f"Dealer wins with {dealer_total}")
            get_dealer_card = False
  
def deal_card(user_list):
    '''
        Function to deal only 1 card.
        user_list refers to which user it should deal the card to
    '''
    index = random.randint(0,12)
    user_list.append(cards[index])
    
def card_points(user_list):
    '''
        Check if the cards are below 16 to force a draw 
        or over 21 to tell user the hand is busted
    '''
    total = 0
    for card in user_list:
        total += card
    
    if 11 in user_list and total >21:
        # convert the Ace card from 11 to 1 if it is over 21
        total = total - 10

    return total

if __name__ == "__main__":
    main()