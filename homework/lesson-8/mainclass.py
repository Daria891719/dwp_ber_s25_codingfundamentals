## 1. Create a dictionary with you personal info: name, age, occupation
## 2. Add your hobby to the dictionary
## 3. Print your occupation (two versions: calling the key and using get() )
## 4. Print your Nationality (two versions: calling the key and using get() with parameter )
## 5. Print your Nationality, if not found print “Unknown”
## 6. Print only the keys of the dictionary
## 7. Print only the values of the dictionary
## 8. Update your occupation
## 9. Remove your age from the dictionary
## 10. Check if the key "Favorite Color" is in the dictionary
info={"name":"Daria", "age":"36", "occupation":["learner"] }
info["hobby"] = ["be a mother", "programmer"]
print ("Your hobby is", info["hobby"])
print (info.get("nationality"))
def information(key_u):
    if key_u in info:
        key_find =info.get(key_u)
        print(key_find)
    else: 
        print ("Unknown")
printquest=information("hobby")
print ("Keys are ", info.keys())
print ("Values are ", info.values())
info["occupation"]="cook"
info["hobby"].append("painting")
print("You new occupation is",info["occupation"])
info.pop("age")
print ("New keys are ", info.keys())
print ("New values are ", info.values())
printquest=information("Favorite Color")
print(info.get("Favorite Color"))
## Exercise 2.1
## From the dictionary below, calculate the total household income:

incomes = {"Adult 1": 3600.00, "Adult 2": 2500.00, "Children": 500.00 }
numbers=0
for age in incomes.values():
    numbers=numbers+age
print(numbers) 
## Exercise 2.2
# Using the dictionary my_dict, 
# convert the dictionary into a list of tuples using a for loop. ( hint: use the method append())
my_dict=[]
## for key in incomes.keys():
#    key
# for value in incomes.values():
#    value
for key, val in incomes.items():
    my_dict.append((key, val))
print (my_dict)

## Exercise 2.3
## Create dictionaries similar to the Rapunzel one for you and 2 of your friends. 
## Create a list of dictionaries  with both information 
# myList = [ my_dict, my_friend_dict_1 , my_friend_dict_2]
## Calculate the average of all your ages.
my_dict_me = {"name":"Daria",
              "age":"67",
              "hobby":"cooking"
              }
my_dict_friend={"name":"Alexsandr",
              "age":"3",
              "hobby":"playing"
              }
my_frienship_list=[my_dict_me, my_dict_friend]
total_sum=0
for dictionary in my_frienship_list:
    total_sum+=int(dictionary.get("age"))
total_items=len(my_frienship_list)
average=total_sum/total_items
print (average)