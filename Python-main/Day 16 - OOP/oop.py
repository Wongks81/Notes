# Object and classes refresh in python
# Day 16 - part 147 video

def turtle_graphics():

    # turtle graphics module
    # Turtle docs https://docs.python.org/3/library/turtle.html
    from turtle import Turtle, Screen

    # Object  =  Class
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.color("red")
    timmy.forward(100)

    my_screen = Screen()
    my_screen.canvheight = 300
    my_screen.canvwidth = 300
    my_screen.exitonclick()

def pretty_table():
    # Pretty table module 
    # https://pypi.org/project/prettytable/
    from prettytable import PrettyTable

    table = PrettyTable()
    table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"])
    table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])
    table.align = "l"
    print(table)

def main():
    pretty_table()

if __name__ == "__main__":
    main()