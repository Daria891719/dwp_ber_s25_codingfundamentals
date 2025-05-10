## 1. Create a dictionary with you 
# personal info: name, age, occupation
nationality = "German"
my_first_dictionary={
    "name":"Joselia",
    "age": 37, 
    "occupation": "Software Engineer",
}

## 2. Add your hobby to the dictionary
my_first_dictionary["hobbies"] = ["painting", "reading"]

## 3. Print your occupation (two versions: calling the key and using get() )
my_first_dictionary.get("occupation")
my_first_dictionary["occupation"]
print("using get >>>>")
print(my_first_dictionary.get("occupation"))
print("using brackets >>>>")
print(my_first_dictionary["occupation"])

## 4. Print your Nationality 
# (two versions: calling the key and using get() with parameter )
my_first_dictionary["nationality"] = "Brazilian"
print(my_first_dictionary)
print("+++++", my_first_dictionary.get("nationality"))
print(">>>>>", my_first_dictionary["nationality"])


## 5. Print your Nationality, if not found print “Unknown”

if "nationality" in my_first_dictionary:
    print(my_first_dictionary.get("nationality"))
    
else:
    print("Unknown")



# ## 6. Print only the keys of the dictionary
print(my_first_dictionary.keys())

## 7. Print only the values of the dictionary
print(my_first_dictionary.values())

# ## 8. Update your occupation
my_first_dictionary["occupation"] = "Volunteer"

# my_first_dictionary["hobbies"].append("cooking") 
print(my_first_dictionary.values())


# ## 9. Remove your age from the dictionary
my_first_dictionary.pop("age")
print(my_first_dictionary)

# ## 10. Check if the key "Favorite Color" is in the dictionary
if "favorite_color" in my_first_dictionary:
    print(my_first_dictionary.get("favorite_color"))
else:
    print("Your favorite color is not on the dictionary yet")
