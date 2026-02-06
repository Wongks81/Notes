# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. 
# e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Warning you should convert the result to a whole number.

#######################################################

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(float(weight) /(float(height)*float(height)))
print("Your BMI is : " + str(bmi))

if bmi < 19:
    print("You are underweight")
elif bmi >=19 and bmi <23:
    print("You weight is healthy")
elif bmi >= 23 and bmi < 30:
    print("You are overweight!!")
else:
    print("You are too heavy!! Time to diet!")

