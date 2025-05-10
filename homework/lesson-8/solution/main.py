european_cities = [("Istanbul", [15460000, "Kebab", "Hagia Sophia"]),
                   ("Moscow", [12678079, "Borscht", "Red Square"]),
                   ("London", [8982000, "Fish and Chips", "Big Ben"]),
                   ("St. Petersburg", [5383890, "Blini", "Hermitage Museum"]),
                   ("Berlin", [3669491, "Currywurst", "Brandenburg Gate"]),
                   ("Madrid", [3348536, "Paella", "Royal Palace of Madrid"]),
                   ("Kiev", [2884000, "Borscht", "Saint Sophia's Cathedral"]),
                   ("Paris", [2140526, "Croissant", "Eiffel Tower"])]

# 1. Create an empty dictionary: `european_cities_info`
european_cities_info = {}
# ----------------------------------------------------------- #

# 2. Loop over the `european_cities` and unpack each tuple
for city, info in european_cities:
    european_cities_info[city] = info
# ----------------------------------------------------------- #

# 3. Print dictionary with the format City --> [Population, Dish, Landmark]
for city in european_cities_info:
    print(city + " --> " + str(european_cities_info[city]))
# ----------------------------------------------------------- #

# 4. Sort the `european_cities_info` dictionary alphabetically by city (use sorted)
for city in sorted(european_cities_info):
    print(city + " --> " + str(european_cities_info[city]))
# ----------------------------------------------------------- #

# 5. Safely print the 'Berlin' info from the `european_cities_info` dictionary
print(european_cities_info.get("Berlin"))
# ----------------------------------------------------------- #

# 6. Safely print the type of 'London' from the `european_cities_info` dictionary
print(type(european_cities_info.get("London")))
# ----------------------------------------------------------- #

# 7. Safely print 'Barcelona' from the `european_cities_info` dictionary or 'Not Found'
print(european_cities_info.get("Barcelona", "Not Found"))
# ----------------------------------------------------------- #

# 8. Add new city `("Rome", [2870500, "Pasta", "Colosseum"])`
european_cities_info["Rome"] = [2870500, "Pasta", "Colosseum"]
# ----------------------------------------------------------- #

# 9. Remove "Madrid" from `european_cities_info`
european_cities_info.pop("Madrid")
# ----------------------------------------------------------- #

# 10. Check to see if Amsterdam is in `european_cities_info` and print whether it is there or not
if "Amsterdam" in european_cities_info:
    print("Amsterdam is in the dictionary.")
else:
    print("Amsterdam is not in the dictionary.")
# ----------------------------------------------------------- #

# Bonus:
dishes = ["Pizza", "Sauerkraut", "Paella", "Hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

dish_country = dict(zip(countries, dishes))
print(dish_country)