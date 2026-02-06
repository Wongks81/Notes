# You are going to write a program that adds to a travel_log. 
# You can see a travel_log which is a List that contains 2 Dictionaries.

# Write a function that will add the entry for Russia to the travel_log.

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia 2 times.

# You've been to Moscow and Saint Petersburg.

# DO NOT modify the travel_log directly. You need to create a function that modifies it.
##############################################################
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def main():
    add_new_country(country="Russia", visited_times=2, cities=["Moscow", "Saint Petersburg"])
    print(travel_log)

    # Pinpoint to 1 element
    print(travel_log[0]["cities"][1])

def add_new_country(country,visited_times,cities):
    new_entry = {
        "country": country,
        "visits": visited_times,
        "cities": cities,
    }
    
    travel_log.append(new_entry)

if __name__=="__main__":
    main()
