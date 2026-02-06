# Prime numbers are numbers that can only be cleanly divided by itself and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# Here are the numbers up to 100, prime numbers are highlighted in yellow:
# https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw
################################################################

def prime_checker(number):
    prime_list = []
    for num in range(2,number+1):
        if num % 2 == 0:
            if num == 2:
                prime_list.append(num)
        elif num % 3 == 0:
            if num == 3:
                prime_list.append(num)   
        elif num % 5 == 0:
            if num == 5:
                prime_list.append(num)    
        elif num % 7 == 0:
            if num == 7:
                prime_list.append(num)       
        elif num % 11 == 0:
            if num == 11:
                prime_list.append(num)
        else:
            prime_list.append(num)
    
    print(f"List of prime numbers : {prime_list}")


def main():
    #n = int(input("Check if this number is a prime number :"))
    #prime_checker(number=n)
    prime_checker(number=100)

if __name__ == "__main__":
    main()