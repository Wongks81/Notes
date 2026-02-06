import random
import blackjack_art
import os

# Lecturer's solution

def main():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Clear the screen and print the art
    os.system("cls")
    print(blackjack_art.logo)

    # Deal 2 cards to user and dealer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # While loop for user
    while not is_game_over:    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score : {user_score}")
        print(f" Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_deal = input(" Type 'y' to get another card : ")
            if should_deal.lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # While loop for Computer
    while computer_score !=0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand : {user_cards}, final score: {user_score}")
    print(f"Dealer final hand : {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))

    if input("Do you want to play again? y/n : ").lower() == 'y':
        main()

def deal_card():
    '''
        Returns a random card from the deck
    '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''
        Take cards list and reture the score calculated
    '''
    # Check for BlackJack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Replace 11 with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Losr, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Black Jack"
    elif user_score > 21:
        return "You went over. You Lose"
    elif computer_score > 21:
        return "Dealer went over. You win"
    elif user_score > computer_score:
        return "You Win!!"
    else:
        return "You Lose...."

if __name__ == "__main__":
    main()