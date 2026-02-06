import random

def main():
    attempts = 0
    difficulty = ""
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number I'm thinking between 1 and 100")
    
    answer = random.randint(1,100)
    print(f"Answer is {answer}")

    while not (difficulty == 'easy') and not (difficulty == 'hard'):
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
        if difficulty == 'easy':
            attempts = 10
        elif difficulty == 'hard':
            attempts = 5
        else:
            print("Please enter easy or hard only!...")
    
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a Guess : "))

        if answer == guess:
            print("You Guess Correctly!!! You Win!!")
            break
        elif answer < guess:
            attempts -= 1
            print("Too High")
        elif answer > guess:
            attempts -= 1
            print("Too Low")
        else:
            print("Please enter a number ... ")
        
        print("Guess Again")

    if attempts == 0:
        print("You have used up all attempts! You LOSE!!")
    


if __name__ == "__main__":
    main()