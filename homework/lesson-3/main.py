# class. Assesment of results
score=95
if score>90:
    print("You score is A")
elif score>80 and score<=90:
    print("You score is B")
elif score>=60 and score<=80:
    print("You score is C")
else:
    print("You score is D")
# while-loop
# number=1
# while number<=100:
#     print(number)
#    number=number+1

 
for number in range (0, 101):
   if number % 2 != 0:
      print(number)
 
 # input function
name=input("Please, write down your name :")
family=input("Please, write down your family :")
age=input("Please, write down your age :")
print("Hello ", name, " ",family, age, " ages old")