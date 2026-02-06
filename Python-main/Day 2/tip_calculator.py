# Tip Calculator
print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage of tip would you like to give? "))
num_ppl = int(input("How many people should we split the bill? "))


tip_amt = total_bill * (tip_percent/100)
amt_to_pay = (total_bill + tip_amt) / num_ppl

print("Each person should pay $" + str(round(amt_to_pay,2)))
