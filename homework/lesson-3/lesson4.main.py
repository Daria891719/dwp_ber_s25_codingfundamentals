# Exercise 1 - List
scores = [15, 19, 17, 12, 17, 13]
print(scores[0])
print(scores[5])
print(scores[len(scores) -1])
print("Max value element : ", max(scores))
print("Min value element : ", min(scores))
scores.append(21)
print("The list with a new number is ",scores)
scores.sort()
print(" The sorted list is ",scores)
while 17 in scores:
    scores.remove(17)
print("The list after removing ", scores)
# Exercise 2 - Looping
