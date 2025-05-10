import random
#
#
#       OO O o o o...      ______________________ _________________
#      O     ____          |                    | |               |
#     ][_n_i_| (   ooo___  |                    | |               |
#    (__________|_[______]_|____________________|_|_______________|
#      0--0--0      0  0      0       0     0        0        0


# Exercise 1
# Draw a wagon in the terminal using 3 print operations
# This is what a wagon looks like:
#
#       ----
#      |    |
#      ------


# Exercise 2
# Define a variable train_size and give it a number of wagons
# Then, draw the train using loops and the train_size variable
# Hint: you can print stuff without a newline by using the print function as shown below
# print("Hello", end="")
# print("World", end="")
# Example:
#
#   ----  ----  ----  ----  ----  ----  ----  ----  ----  ----
#  |    ||    ||    ||    ||    ||    ||    ||    ||    ||    |
#  ------------------------------------------------------------


# Exercise 3
# Draw a passenger with 'o' in each odd wagon
# and 'x' in the even wagons
#   ----  ----  ----  ----
#  |  x ||  o ||  x ||  o |
#  ------------------------


# Exercise 4
# Put the previous code in a function
# It takes the train size as an argument
# and draws the train


# Given a function that returns the character 'x' with 10% probability
# and 'o' with 90% probability called "get_random_passenger"
def get_random_passenger():
  r = random.randint(0, 100)
  if r <= 10:
    return 'x'
  else:
    return 'o'
  

# Exercise 5
# Change the train function so that each wagon carries a passenger with 90% probability


# Exercise 6
# After drawing the train,
# ask the user if they want to clear the screen:
# "would you like to clear the screen? (y/n)"
#
# import os
# os.system('cls' if os.name == 'nt' else 'clear')
#


# Exercise 7
# Before actually clearing the screen, wait for 3 seconds
#
# import time
# time.sleep(3)


# Exercise 8
# Let's observe the randomness by redrawing the train over and over again
# Use an infinite loop (while True)
# In the loop, draw a train of size 10, wait for 1 sec and clear the screen


# Exercise 9
# And finally, let's animate our train, choo choo!
# animate the train by using the two previously introduced functions (clear and sleep)
# you can start by drawing a train of size 10, clear, wait, draw a train of size 9, etc
# until it completely disappears from the screen