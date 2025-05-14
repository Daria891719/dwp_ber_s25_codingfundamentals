
# Exercise 1: Student Grouping
# Imagine you are a teacher who needs to group their students into pairs or small groups. Given the following list of dictionaries, create random pairs or groups of students – each pair has to have the same project choice.
import random 
students = [
    {
        "name": "Jane",
        "choice": "Project B"
    },
    {
        "name": "Janet",
        "choice": "Project A"
    },
    {
        "name": "Jack",
        "choice": "Project A"
    },
    {
        "name": "Jimmy",
        "choice": "Project B"
    },
    {
        "name": "Jean",
        "choice": "Project A"
    },
    {
        "name": "Juan",
        "choice": "Project B"
    },
    {
        "name": "Juanita",
        "choice": "Project B"
    },
    {
        "name": "Janine",
        "choice": "Project A"
    },
    {
        "name": "Jill",
        "choice": "Project B"
    },
    {
        "name": "John",
        "choice": "Project B"
    },]
def pick_random_name(not_in_list):
    random_name = random.choice(not_in_list)
    return random_name
students_names_project_a=[]
students_names_project_b=[]
for student in students:
    name = student["name"]
    choice = student["choice"]
    if choice=="Project A":
        students_names_project_a.append(name)
    else:
        students_names_project_b.append(name)
print ("Project A: ", students_names_project_a)
print ("Project B: ", students_names_project_b)


# def pair (list_names):
#     pair_pro=[]
#     i=0
#     while i<2:
#         name_choisen=pick_random_name(list_names)
#         if name_choisen not in pair_pro:
#             pair_pro.append(name_choisen)
#             i+=1
#         else:
#             i=i
#     return pair_pro
def pair (list_names):
    pairs = []
    not_in_list=list_names.copy()
    while len(not_in_list)>=2:
        name1 = pick_random_name(not_in_list)
        not_in_list.remove(name1)
        name2 = pick_random_name(not_in_list)
        not_in_list.remove(name2)
        pairs.append([name1, name2])
    if len(not_in_list)==1:
        pairs.append([not_in_list[0]])
    return pairs
list_names=pair(students_names_project_a)
print ("Students will work in pairs on the project A: ", list_names)
list_names=pair(students_names_project_b)
print ("Students will work in pairs on the project B: ", list_names)


# Exercise 2: Meal cost calculator
# Preparation
# Run the following code a few times to understand what is happening. The 'inquire' function will ask 3 questions for each person. You don't need to understand how the 'inquire' function works, you just need to use it. You will be able to select one of two options for each question asked. You will then need to do some calculations based on the result created by the 'inquire' function.

import inquirer
import random

def inquire(name):
  breakfast_base = random.randint(2, 6)
  lunch_base = random.randint(10, 21)
  dinner_base = random.randint(30, 51)
  questions = [
      inquirer.List(
          "breakfast",
          message=f"How much did {name} pay for breakfast? 🥐 ☕",
          choices=[f"${breakfast_base}", f"${breakfast_base + 2}"],
      ),
      inquirer.List(
          "lunch",
          message=f"How much did {name} pay for lunch? 🍔",
          choices=[f"${lunch_base}", f"${lunch_base + 7}"],
      ),
        inquirer.List(
          "dinner",
          message=f"How much did {name} pay for dinner? 🍽️",
          choices=[f"${dinner_base}", f"${dinner_base + 15}"],
      ),
  ]
  
  transactions = inquirer.prompt(questions)
  return {name: transactions}


def convert_dollars(value):
    number_value = int(value.replace("$", ""))
    return number_value

people = ["John", "Jane", "Janet"] 
result = [inquire(person) for person in people]
print("Result: ")
for person in result:
    for name, costs in person.items(): 
        total=0
        for cost in costs.values():
            cost=int(convert_dollars(cost))
            total += cost
        print(f"{name} sum: ${total}")

# Exercise 3: Meal cost game
# Run this code a few times and try to understand how the game works to then be able to try and win the game. Slightly change the low and high limit range to make the game easier to win.

def play_game():
    name = "ReDi"
    lower_limit = 42 
    higher_limit = 102
    meals = inquire(name)[name] 
    total = 0


    for meal_value in meals.values(): 
        total += convert_dollars(meal_value) 
    if (lower_limit > total or higher_limit < total): 
        print("You lost.. try again!") 
    else: 
        print("Congrats! You won 👏")
play_game()

# Exercise 4: Credit Card Masking
# Complete the mask_credit_card_number function that takes in a 16-digit credit card number and masks all but the last 4 digits.

# sample_credit_card_number = '1234567890987654'
# expected_credit_card_result = 'XXXXXXXXXXXX7654'

# def mask_credit_card_number(credit_card_number):
#     masked_credit_card_number = sample_credit_card_number
#     number=0
#     for i in range (0,12):
#         number+=x
#     for i in range (12,16):
#         number+=i
#     masked_credit_card_number=number
#     return masked_credit_card_number
# sample_credit_card_number = "1234567890987654"
# masked_credit_card_number=mask_credit_card_number (sample_credit_card_number)
# # Uncomment the lines below to test your answer 👇👇👇
# # print('Expected result: ', expected_credit_card_result)
# # result = mask_credit_card_number(sample_credit_card_number)
# print('Created new mask number is:', masked_credit_card_number)


def mask_credit_card_number(credit_card_number):
    masked_last_4number = credit_card_number[-4:]
    masked_credit_card_number="X"*12+masked_last_4number
    return masked_credit_card_number
sample_credit_card_number = "125455490987654"
masked_credit_card_number=mask_credit_card_number (sample_credit_card_number)
print('Created new mask number is:', masked_credit_card_number)
