'''
EXERCISE 1

Write a function `greeting` that takes 2 arguments (first_name and last_name) and prints the following message using the given arguments:
    "Hello, Alice Smith, are you ready for some fun coding today?"
'''

# solution for exercise 1 👇🏽

def greeting(first_name, last_name):
    print ("Hello, ",first_name, last_name,", are you ready for some fun coding today?")
greeting ("Alice", "Smith")

'''
EXERCISE 2

Write a function `repeat_character` that takes a character and a number as arguments and prins a string,
where the character is repeated the specified number of times. 
The number has a default value of 2.
For example, if the character is 'X' and the number is 4, the function should return "XXXX."
'''

# solution for exercise 2 👇🏽
def repeat_character (character, repeat_times):
#    list=[]
#    if x<=number:
#      list_fin= list.append(character)
    print(character*repeat_times)
print(repeat_character ("Z",10))

'''
EXERCISE 3

Copy and paste your solution from exercise 2. 
This time, modify the function so that, if the given number is bigger than 10, it will print out "Sorry, too long!"
'''

def repeat_character (character, repeat_times):
    if repeat_times<=10:
        print(character*repeat_times)
    else:
        print ("Sorry, too long!")
print(repeat_character ("Z",11))



# solution for exercise 3 👇🏽