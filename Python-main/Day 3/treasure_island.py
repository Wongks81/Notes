# Treasure island text game

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
direction = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")

if direction != "left":
    print("You have fallen into the hole.\nGame over")
    exit

isSwim = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")

if isSwim != "wait":
    print("You are attacked by trout.\nGame Over")
    exit

door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")

if door == "Yellow":
    print("You Win!!")
elif door == "Red":
    print("Burned by fire\nGame Over")
elif door == "Blue":
    print("Eaten by beasts\nGame Over")
else:
    print("Game Over")




