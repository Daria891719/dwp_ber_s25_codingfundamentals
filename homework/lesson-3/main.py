# class. Assesment of results
# score=95
# if score>90:
#    print("You score is A")
# elif score>80 and score<=90:
#    print("You score is B")
# elif score>=60 and score<=80:
#    print("You score is C")
# else:
#    print("You score is D")
# while-loop
# number=1
# while number<=100:
#     print(number)
#    number=number+1

 
# for number in range (0, 101):
#   if number % 2 != 0:
#      print(number)
 
 # input function
# name=input("Please, write down your name :")
# family=input("Please, write down your family :")
# age=input("Please, write down your age :")
# print("Hello ", name, " ",family, age, " ages old")

# Lesson 3 Homework
# Basic Arithmetic Operations
a=input ("Please, write down the first number: ")
b=input ("Please, write down the second number: ")
a=int(a)
b=int(b)
print("The result of addition is ",a + b)
if a<b:
    c=b-a
    print("The result of subtraction is -", c)
else:
    print("The result of subtraction is ", a-b)
print("The result of multiplication is ",a*b)
if b!=0:
    print("The result of division is ", a/b)
else:
    print("You cannot divide by 0, try again")
#  Modulus and Exponentiation
if b!=0:
    print("The result of modulus operation is ", a%b)
else:
    print("The second number was 0. You cannot divide by zero, try again")
print("The result of number raised to the power of is ",a**b)
# Odd or Even
if a%2==0:
    print ("The first number ",a," is even" )
else:
    print ("The first number ",a," is odd" )
if b%2==0:
    print ("The second number ",b," is even" )
else:
    print ("The second number ",b," is odd" )
# Compare Two Numbers
if a<b:
    print (a," less than ",b)
elif a>b:
    print (a," more than ",b)
else: 
    print ("Both numbers are equal")
# Print Numbers 1 to 10
n=1
while n<11:
    print (n)
    n=n+1
# Multiplication Table
v=input("Write down number for creation multiplication table: ")
v=int(v)
print ("Multiplication table for number ",v)
m=1
while m<=10:
    print (v,"*",m,"=",m*v)
    m=m+1
# FizzBuzz
print("Table from 1 to 20 with substitutions")
m=1
while m<=20:
    if m%3==0:
        print("Fizz")
    elif m%5==0:
        print("Buzz")
    else:
        print (m)
    m=m+1
# Leap year
year=input("write a number of each year for checking whether it is leap: ")
year=int(year)
if year % 4==0 and year%100!=0:
    print ("This year is leap!")
elif year%4==0 and year%100==0 and (year%400!=0):
   print ("This year is not leap")
else:
    print ("This year is not leap")

# A year that is divisible by 400 is always a leap year. 
# A year that is divisible by 100 but not by 400 is not a leap year.
# A year that is divisible by 4 but not by 100 is a leap year. Any other year is not a leap year.
