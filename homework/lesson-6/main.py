# A- What is the name of a built-in function in "random" package which can generates random integers?
# Answer randint()
# B- Programming: Using the function in section A, generate 10 integers that are between 1 and 100. Create a list. Call it rand_numbers. Use this list to save the generated integers. Print the list. Calculate the average of the numbers in rand_numbers and display the result. (Feel free to write a function for this calculation.) C- Is there any built-in function in Python that can calculate average of numbers? If "yes" use that function to calculate the average of rand_numbers and display the result. D- Is the result of section B and C the same?
from random import randint
rand_numbers=[]
def generation_numbers ():
    c=0
    while c<=10:
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