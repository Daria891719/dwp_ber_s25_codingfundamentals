"""Homework L8: Dictionaries 📚
We have the list of tuples:

european_cities = [("Istanbul", [15460000, "Kebab", "Hagia Sophia"]),
                   ("Moscow", [12678079, "Borscht", "Red Square"]),
                   ("London", [8982000, "Fish and Chips", "Big Ben"]),
                   ("St. Petersburg", [5383890, "Blini", "Hermitage Museum"]),
                   ("Berlin", [3669491, "Currywurst", "Brandenburg Gate"]),
                   ("Madrid", [3348536, "Paella", "Royal Palace of Madrid"]),
                   ("Kiev", [2884000, "Borscht", "Saint Sophia's Cathedral"]),
                   ("Paris", [2140526, "Croissant", "Eiffel Tower"])]
Create an empty dictionary: european_cities_info
Loop over the european_cities and unpack each tuple
Print dictionary with the format City --> [Population, Dish, Landmark]
Sort the european_cities_info dictionary alphabetically by city (use sorted)
Safely print the 'Berlin' info from the european_cities_info dictionary
Safely print the type of 'London' from the european_cities_info dictionary
Safely print 'Barcelona' from the european_cities_info dictionary or 'Not Found'
Add new city ("Rome", [2870500, "Pasta", "Colosseum"])
Remove "Madrid" from european_cities_info
Check to see if Amsterdam is in european_cities_info and print whether it is there or not
Bonus: Create a dictionary from two lists:
Use the functions dict() and zip()
dishes = ["Pizza", "Sauerkraut", "Paella", "Hamburger"] countries = ["Italy", "Germany", "Spain", "USA"
"""
european_cities = [("Istanbul", [15460000, "Kebab", "Hagia Sophia"]),
                   ("Moscow", [12678079, "Borscht", "Red Square"]),
                   ("London", [8982000, "Fish and Chips", "Big Ben"]),
                   ("St. Petersburg", [5383890, "Blini", "Hermitage Museum"]),
                   ("Berlin", [3669491, "Currywurst", "Brandenburg Gate"]),
                   ("Madrid", [3348536, "Paella", "Royal Palace of Madrid"]),
                   ("Kiev", [2884000, "Borscht", "Saint Sophia's Cathedral"]),
                   ("Paris", [2140526, "Croissant", "Eiffel Tower"])]
european_cities_info={}
# Link between city and its info
for city, info in european_cities:
    european_cities_info[city]=info
    print (f"{city}--->{info}")
# print(european_cities_info)
def info_city_all (city_name):
    info=european_cities_info.get(city_name)
    if info:
        population, dish, landmark=info
        return   f"{city_name} has population {population}, the main dish is {dish} and the main sightseeing is {landmark}"
    else:
       return f"Sorry, {city_name} is not on the list"
# Sort the european_cities_info dictionary alphabetically by city (use sorted)
print ("The sorted list of cities and information:")
for city in sorted(european_cities_info):
    info=european_cities_info.get(city)
    print (f"{city}--->{info}")
# Safely print the 'Berlin' info from the european_cities_info dictionary
print(info_city_all ("Berlin"))

#Safely print the type of 'London' from the european_cities_info dictionary
print (type(european_cities_info["London"]))

#Safely print 'Barcelona' from the european_cities_info dictionary or 'Not Found'
print(info_city_all ("Barcelona"))

european_cities_info["Rome"]=[2870500, "Pasta", "Colosseum"]
european_cities_info.pop ("Madrid")
print("The new list of cities is (Madrid was removed and Rome was added)")
for city in sorted(european_cities_info):
    info=european_cities_info.get(city)
    print (f"{city}--->{info}")

print(info_city_all ("Amsterdam"))

# Bonus: Create a dictionary from two lists:
# Use the functions dict() and zip()
dishes = ["Pizza", "Sauerkraut", "Paella", "Hamburger"] 
countries = ["Italy", "Germany", "Spain", "USA"]
print ("Dictionary: ", dict(zip(countries,dishes)))
print ("List: ", list(zip(countries,dishes)))

for country, dish in dict(zip(countries, dishes)).items():
    print(f"{country} --> {dish}")