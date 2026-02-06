# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February. 

# Leap year happens on every year that is evenly divisible by 4 
#   **except** every year that is evenly divisible by 100 
#       **unless** the year is also evenly divisible by 400

#######################################################################
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    # Divisible by 4 
    if year % 100 == 0:
        # For end of century years

        if year % 400 == 0:
            # End of century years need to divide by 400 to be considered leap years
            print("Leap Year")
        else:
            # Unable to divide by 400 so not leap year
            print("Not Leap Year")
    else:
        # Not end of century but divisible by 4, so leap year
        print("Leap Year")
else:
    # Not divisible by 4
    print("Not Leap Year")
