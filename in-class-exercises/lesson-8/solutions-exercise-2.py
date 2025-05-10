my_dictionary = {
    "name": "Rapunzel", "age": 19, "hobbies": ["paiting", "singing", "reading"]
}

for key in my_dictionary.keys():
    print(key)

for lalala in my_dictionary.values():
    print(lalala)

for k, v in my_dictionary.items():
    print(k, v)


## Exercise 2.1
## From the dictionary below, calculate the total household income:

incomes = {
    "Adult 1": 3600.00, 
    "Adult 2": 2500.00, 
    "Children": 500.00 
}

accumulator = 0
for income in incomes.values():
    accumulator = accumulator + income

# print(accumulator)
    



## Exercise 2.2
# Using the dictionary my_dict, 
# convert the dictionary into a list of tuples using a for loop. ( hint: use the method append())
# my_list = []

# for key, val in my_dictionary.items():
#     my_list.append((key, val))
# print(my_list)

## Exercise 2.3
## Create dictionaries similar to the Rapunzel one for you and 2 of your friends. 
## Create a list of dictionaries  with both information 
# myList = [ my_dict, my_friend_dict_1 , my_friend_dict_2]
## Calculate the average of all your ages.

#  average formula: 
# total_sum / total_items

my_personal_dictionary = {
    "name": "Joselia",
    "hobbies": ["cooking, riding"],
    "age": 37
}
my_friend_dictionary = {
    "name": "Laia",
    "hobbies": ["cycling", "playing games"],
    "age": 40
}

my_friendship_list = [
    my_personal_dictionary, 
    my_friend_dictionary
]

total_sum = 0
for item in my_friendship_list:
    total_sum += item.get("age")
    # total_sum = total_sum + dictionary.get("age")

average = total_sum / len(my_friendship_list)

print(">>>>>", average)
