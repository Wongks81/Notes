# Recap on functions with output

def my_function():
    result = 3*2
    return result

num = my_function()
print(num)

def format_name(fname,lname):
    """
    This is a docstring for the function.
    Describe in here what the function does.
    Hover over the functions below to see the effect.
    """
    if fname == "" or lname =="":
        return "Error"
    
    name = fname + " " + lname

    # .title() will capitialize the 1st letter of each word
    name = name.title()
    return name

print(format_name("KIM","SunG"))