# A- What is the name of a built-in function in "random" package which can generates random integers?
# Answer randint()
# B- Programming: Using the function in section A, generate 10 integers that are between 1 and 100. Create a list. Call it rand_numbers. Use this list to save the generated integers. Print the list. Calculate the average of the numbers in rand_numbers and display the result. (Feel free to write a function for this calculation.) C- Is there any built-in function in Python that can calculate average of numbers? If "yes" use that function to calculate the average of rand_numbers and display the result. D- Is the result of section B and C the same?
from random import randint
rand_numbers=[]
def generation_numbers ():
    c=0
    while c<10:
        rand_numbers.append(randint(0,100))
        c+=1
    print ("We created the list: ", rand_numbers)
    return rand_numbers
rand_numbers1=generation_numbers ()
# Calculate the average of the numbers in rand_numbers and display the result.
sum=sum(rand_numbers1)
len=len(rand_numbers1)
print ("The average of the numbers in the list is ", sum/len)
# version 2
import statistics
average =statistics.mean(rand_numbers1) 
print ("The average using of function is ", average)
print ("The difference between 2 methods is ", round(sum/len)-round (average))
# Create a Calculator that can perform four basic operations: addition, subtraction, multiplication, and division! Your program asks the user to input the operation they want to perform and input two numbers. Then it performs the operation and display the result.
#def calculator (d,e):
#    print ("The sum of ", d," and ", e, " is ", d+e)
#    print ("The subtraction of ", d," and ", e, " is ", d-e)
#    print ("The multiplication of ", d," and ", e, " is ", d*e)
#    if e!=0:
#        print ("The division of ", d," and ", e, " is ", d/e)
#    else:
#        print ("You cannot divide by 0. Please try again")
# d=int(input("Write down the first number: "))
# e=int(input("Write down the second number: "))
# res=calculator (d,e)
print ("Mathematical function")
def add (d,e):
    print ("The sum of ", d," and ", e, " is ", d+e)
def sub (d,e):
    print ("The subtraction of ", d," and ", e, " is ", d-e)
def mul (d,e):
    print ("The multiplication of ", d," and ", e, " is ", d*e)
def div (d,e):
    if e!=0:
        print ("The division of ", d," and ", e, " is ", d/e)
    else:
        print ("You cannot divide by 0. Please try again")
def result(d, e, operation):
    if operation=="+":
        res_add=add(d,e)
    elif operation=="-":    
        res_sub=sub(d,e)
    elif operation=="*":    
        res_mul=mul(d,e)
    elif operation=="/":    
        res_div=div(d,e) 
    else:
        print ("You chose an incorrect action")  
try:
    d=int(input("Write down the first number: "))
    e=int(input("Write down the second number: "))
    operation=str(input("Choose what do you want to do with numbers: + - * /: "))
    result(d, e, operation)
except ValueError:
    print("You entered invalid characters. Please enter only integers.")
#Create "Guess the Number" game! Your program generates a random number between 1 and 100. Then asks the user to guess the random number. The user have 5 times to guess the number. If they cannot guess it correctly during this 5 rounds, they loose. Each round that the user guess the number wrong, your program gives the user a hint like "Too low!" or "Too high!". If the guess is correct it should print "Correct!" and prints the number of tries.
# Instructions: Write a function to generate a random number. Write a function to ask the user for their guess. Write a function to check if the guess is correct, too high, or too low. Write a main function that loops until the user guesses correctly and provides feedback.
print ("Guess the number between 0 and 100. You have 5 attempts! ")
from random import randint
def com ():
    return randint(0,100)
def user():
    while True:
        try:
            user_attemt=int(input("Write a number from 0 to 100 "))
            return user_attemt
        except ValueError:
            print("You entered invalid characters. Please enter only integers.")
def play ():
    com_chooce=int(com())
    attempt=1
    while attempt <=5:
        user_chooce=user()
        if com_chooce==user_chooce:
            print ("Well done! You win!!!")
            print(f"You guessed it in {attempt} tries.")
            return
        else: 
            if com_chooce>user_chooce:
                print ("Too low!")
            elif com_chooce<user_chooce:
                print ("Too high!")
            attempt+=1
    print ("Sorry, you lose!")    
    print ("The number that had to be guessed was ", com_chooce)
start_play=play ()

