# By using Google, find a function that gives you current date and time and print the current date and time
from datetime import datetime
print(datetime.now())
# Write a function that counts number of letters in a string you input.
# The function will have 1 parameter, the string that's letters you want to count.
# Try both variants - print the result (number of letters in the inputed string) and also store the result in the memory using return. Try to recall what is the difference between using print and return
def count (n):
    number=0
    for letter in n:
        number+=1
    return number
number_fin=count("dfshkdfjhsrwtZTvbbhdgajzs")
print ("The number of characteres in the list is: ", number_fin, " (using function)")

# Variant 2
new_list=str("dfshkdfjhsrwtZTvbbhdgajzs")
number=0
for letter in new_list:
    number+=1
print ("The number of characteres in the list is: ", number, " (using loop)")
'''
Exercise 3
Create a simple function with two parameters that returns their sum.
Call the function and save the result into a variable (name of the variable is up to you).
Create another function with one parameter that decides if the parameter can be divided by 3 and prints appropriate messages
Call the second function and use the variable that you created in the b) part as argument.
'''
# n1=int(3)
# n2=int(2)
def add1 (n1,n2):
    n_fin=n1+n2
    return n_fin
n1=2
n2=3
res=add1(n1, n2)
print (n1, " + ", n2, " = ", res)
def count2 (n_fin):
    if n_fin%3==0:
        print ("The sum of ",n1, "and ",n2, "can be divided by 3")
    else: 
        print ("The sum of ",n1, "and ",n2, "cannot be divided by 3. Try another number")
res2=count2(res)
'''
Complete the game logic inside the play_game(user_choice) function. The function should determine the outcome of the game based on the user's choice (0 for rock, 1 for paper, and 2 for scissors) and the computer's randomly generated choice.
The possible outcomes are as follows:
If the user's choice is the same as the computer's choice, it's a "Tie."
If the user wins, return "You win."
If the computer wins, return "You lose."
Test the game by calling the function with different user choices and print the results.
'''
user_ch=input("Let's play the game. Write down your choice: 0 for rock, 1 for paper, and 2 for scissors): ")
user_ch=int(user_ch)
from random import randint
def number ():
    return randint(0,2)
comp=number ()
print("The computer's number is: ", comp)
if user_ch==comp:
    print("Tie")
elif user_ch==0 and comp==2:
    print("You win")
elif user_ch>comp:
    print("You win")
else:
    print("You lose")
