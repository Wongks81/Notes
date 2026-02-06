import random
import blackjack_art
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def main():
    is_game_over = False
    while not is_game_over:
        player_cards = []
        dealer_cards = []
        get_player_card = True
        player_score = 0
        dealer_score = 0
        print(blackjack_art.logo)

        # Deal 2 cards for the first round using a for loop 
        for card in range(0,2):
            deal_card(player_cards)
            deal_card(dealer_cards)

        # Check if either user or dealer has a blackjack
        if sum(player_cards) == 21 and len(player_cards) == 2:
            print(f"Your cards : {player_cards}")
            print("BlackJack!! You Win!!")
            is_game_over = True
        elif sum(dealer_cards) == 21 and len(dealer_cards) == 2:
            print(f"Dealer's cards : {dealer_cards}")
            print("Dealer has BlackJack... You lose....")
            is_game_over = True
        else:
            # While loop to loop player to continue getting cards
            while get_player_card:
                # No player has blackjack, display cards
                print(f"Your cards : {player_cards}, current score : {sum(player_cards)}")
                print(f"Dealer first card is : {dealer_cards[0]}")

                if input("Press 'y' if you want to draw a card : ").lower() == 'y':
                    deal_card(player_cards)
                    if card_points(player_cards) > 21:
                        is_game_over = True
                        get_player_card = False
                    else:
                        continue
                else:
                    # For any other keys press besides Y/y
                    get_player_card = False

                # store player score 
                player_score = card_points(player_cards)

            # While loop for dealer
            while sum(dealer_cards) < 17 and not is_game_over:
                deal_card(dealer_cards)
                
            dealer_score = card_points(dealer_cards)  
            
            print(f"\n##############################################################\n")
            print(f"Your cards : {player_cards}, Final score : {sum(player_cards)}")
            print(f"Dealer's cards : {dealer_cards}, Final score : {sum(dealer_cards)}")
            print(compare_score(player_score, dealer_score))
        
        if input("Press 'y' if you want to play again...").lower() == 'y':
            is_game_over= False
        else:
            is_game_over = True
  
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
    if 11 in user_list and sum(user_list) >21:
        # convert the Ace card from 11 to 1 if it is over 21
        user_list.remove(11)
        user_list.append(1)

    total = sum(user_list)

    return total

def compare_score(player_score, dealer_score):
    '''
        compare the scores and output the results
    '''
    if player_score > 21 :
        return "You Busted!! You LOSE!!"
    elif dealer_score > 21:
        return "Dealer Busted!! You WIN!!!"
    elif player_score == dealer_score:
        return "Draw"
    elif player_score > dealer_score:
        return "You WIN!!!"
    elif player_score < dealer_score:
        return "You LOSE!!!"

if __name__ == "__main__":
    main()