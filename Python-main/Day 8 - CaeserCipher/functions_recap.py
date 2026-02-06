def main():
    greet_with_name("KS")
    print("-----------------------------------------")
    greet_with_2_arguements(location="Changi", name="KS")


def greet_with_name(name):
    print(f"Hello {name}")
    print("This is printed from inside the function")

def greet_with_2_arguements(name,location):
    print("Function with 2 arguements")
    print(f"Hi {name}")
    print(f"I am currently in {location}")

if __name__ == "__main__":
    main()