# Preparation
scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
print("The number of variable in the list is: ",len(scores))
# 1 Given the same list of scores, write a program that counts the number of 3s in the list
a=len(scores)//3
print("The number of thirds in the list is: ",a)
b = scores.count(3)
print("Number of 3s in the list: ", b)
# Given the same list of scores, find the maximum in the list
print("The max number in the list is: ", max(scores))
# write a program that prints the common elements
list_1 = ["foo", 2, "bar", 3, "baz", "spam", 4]
list_2 = ["1", 2, "3", 3, "4", "foo", "pasm", "bar"]
common= list(set(list_1) & set(list_2))
print("The overlaping elements are: ",common)
# Given the following list of numbers, write a program
#that goes through each number in the list
# appends it to a new list called positive_numbers if the number is positive
all_numbers = [111, 32, -9, -45, -17, 9, 85, -10]
positive_numbers = []
for positive in all_numbers:
    if positive>=0:
        positive_numbers.append(positive)
print("Only positive numbers there are: ", positive_numbers)
#Print the items of the given list in reverse
all_numbers_reversed=[]
for c in all_numbers:
    all_numbers_reversed.insert(0, c)
print ("The reversed list is: ",all_numbers_reversed)
# Convert the scores list (from Exercise 0) into a set and print its elements
set_conv=set(scores)
print(set_conv)
# Create a List of Tuples with 5 country names and their capitals, and print the list
с1= ('Russia','Moscow')
с2= ('Germany','Berlin')
с3= ('Norway','Oslo')
с4= ('France','Paris')
с5= ('Italy','Rome')
combined=с1+с2+с3+с4+с5
con=input("Write down the name of a country: ")
if con in combined:
    print("The capital of ",combined[0],"is ", combined[1])
else:
    print("The chosen country is not in the list, try again")
