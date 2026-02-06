
import calculator_art

def main():
    operations ={
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide,
        }
    
    print(calculator_art.logo)

    num1 = int(input("What is the first number? : "))

    # Print operations
    for key in operations:
        print(key)
    
    op = input("Pick an operation : ")
    num2 = int(input("What is the second number?: "))

    func = operations[op]
    print(f"{num1} {op} {num2}")
    print(func(num1, num2))
    

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