import calculator_art

def main():
    calculator()


def calculator():
    print(calculator_art.logo)
    to_continue = True
    operations ={
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide,
        }

    num1 = int(input("What is the first number? : "))

    # Print operations
    for key in operations:
        print(key)
    
    op = input("Pick an operation : ")
    num2 = int(input("What is the second number?: "))

    selected_func = operations[op]
    answer = selected_func(num1, num2)
    print(f"{num1} {op} {num2} = {answer}")

    while to_continue:
        cont = input("Type 'y' to continue ").lower()
        
        if cont == 'y':
            num3 = int(input("What is the next number? : "))
            for key in operations:
                print(key)

            op = input("Pick an operation: ")    
            selected_func = operations[op]
            answer2 = selected_func(answer, num3)

            print(f"{answer} {op} {num3} = {answer2}")
        else:
            to_continue = False

            # Recursion
            calculator()
    

def add(a1, a2):
    return a1 + a2

def subtract(s1, s2):
    return s1 - s2

def multiply(m1,m2):
    return m1 * m2

def divide(d1,d2):
    return d1 / d2
    
if __name__ =="__main__":
    main()