"""
print("modifying the code to make a 5×5 table!")
for column in range(1, 6):
    print(f"row {column}: ", end="")
    for row in range(1, 6):
        print(column * row, end=" | ")
    print()
"""
# Now let the user decide the size of the table
size=int(input("write a number  for which you want to create a multiplication table: "))
a=size+1
for column in range(1, a):
    print(f"row {column}: ", end="")
    for row in range(1, a):
        print(column * row, end="  |  ")
    print()

# Example
print(f"💖 nested loop for {name}")
size = int(input("table size:")) +1
for column in range(1, size):
    print(f"row {column}: ", end="") # string interpolation 
    for row in range(1, size):
        if column * row < 9:
            print(column * row, end="  |  ")
        else:
            print(column * row, end=" | ")
    print()
