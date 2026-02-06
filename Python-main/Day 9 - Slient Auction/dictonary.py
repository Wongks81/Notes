# Recap Dictonary
# Dictonary {key:value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing something over and over again",
    }

# Keys are case sensitive
print(programming_dictionary["Bug"])

# Add items to dictonary
programming_dictionary["Computer"] = "What you will need to code anything"

print(programming_dictionary)

# Edit item in dictonary
programming_dictionary["Bug"] = "An Insect"
print(programming_dictionary)

# Loop thru a dictonary
for key,val in programming_dictionary.items():
    print(key)
    print(val)

# Creating empty dictonary
empty_dictonary = {}

# Wipe an existing dictonary
programming_dictionary={}

################################################
# Nesting
captials ={
    "France":"Paris",
    "Germany": "Berlin"
}

# Nestiing a List in Dictonary
travel_log={
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin", "Hamburg"],
}

# Nesting a dictonary in a dictonary
travel_log={
    "France":{
        "cities_visited": ["Paris","Lille","Dijon"],
        "total_visits":12, 
        },
    "Germany":{
        "cities_visited":["Berlin", "Hamburg"],
        "total_visits": 10,
    },
    
}

# Nesting dictonary in a list

travel_log=[
    {   
        "country":"France",
        "cities_visited": ["Paris","Lille","Dijon"],
        "total_visits":12, 
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin", "Hamburg"],
        "total_visits": 10,
    },
    
]