# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

#############################################
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine_string = (name1 + name2).upper()

points_true = combine_string.count("T") + combine_string.count("R") + combine_string.count("U") + combine_string.count("E") 

points_love = combine_string.count("L") + combine_string.count("O") + combine_string.count("V") + combine_string.count("E") 

total_points = int(str(points_true) + str(points_love))

if total_points < 10 or total_points > 90:
    print(f"Your score is {total_points}, you go together like coke and mentos")
elif total_points >= 40 and total_points <= 50:
    print(f"Your score is {total_points}, you are alright together")
else:
    print(f"Your score is {total_points}")


