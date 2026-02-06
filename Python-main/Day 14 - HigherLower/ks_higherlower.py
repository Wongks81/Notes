from unicodedata import name
import game_data
import random
import os

def main():
    print("####################")
    print("  Higher Lower  ")
    print("####################")
    
    not_game_over = True
    score = 0
    compare_a ={}
    compare_b ={}

    # Get random choices to game data
    compare_a = generate_choices()

    while not_game_over:
        
        incorrect_input = True
        same_data = True
        # Check if the same choice are randomly generated
        while same_data:
            compare_b = generate_choices()
            if compare_a != compare_b:
                same_data = False    
        
        # Print out the data
        print("-------------------------------------------------------------")
        print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}")
        print("   VS   ")
        print(f"Compare B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']}")
        print("-------------------------------------------------------------")

        # Check if input is A or B
        while incorrect_input:
            reply = input(f"\nWho has more followers? A or B? ").upper()
            if not reply == 'A' and not reply =='B':
                print(" Please enter A or B ")
            else:
                incorrect_input = False

        # Get reply if the results of the compare is correct
        if reply == compare_followers(compare_a,compare_b):
            score += 1
            os.system("cls")
            print(f"\nYou're right! Current score is {score}")

            # Move B data to A for new comparison
            if reply == "B":
                compare_a = compare_b
        else:
            print(f"\nYou're wrong, your final score is {score}\n")
            not_game_over = False


def compare_followers(dict_a, dict_b):
    '''
        compare the followers between the 2 dictonary
    '''
    if int(dict_a['follower_count']) > int(dict_b['follower_count']):
        return "A"
    elif int(dict_a['follower_count']) < int(dict_b['follower_count']):
        return "B"
    
    
def generate_choices():
    '''
        generate a random choice
    '''
    return random.choice(game_data.data)
    

    

if __name__ == "__main__":
    main()