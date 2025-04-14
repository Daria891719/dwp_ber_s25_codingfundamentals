# Write an if statement which checks if a value is above a given quota. If the
# value is greater or equal to the quota, print "Done". Otherwise print "Not done"
quota=1000
sum=int(input("Please, write you sum: "))
if sum>=quota:
    print ("Done")
else:
    print ("Not done")
# Copy/paste your code above and slightly tweak it to change what is being printed
# If the value is greater or equal to the quota, print 0 (zero)
# Otherwise print the result of: quota - value
if sum>=quota:
    print ("0")
else:
    print ("The sum is ", sum, ", the quota is", str(quota))
#Create/define a function called 'fruits_remaining' which takes two parameters:
#'fruits_picked' and 'fruits_quota' and return the remainder of fruits to pick:
# - 0 if the fruits_picked is greater or equal to the fruits_quota, otherwise
# fruits_quota - fruits_picked.
def fruits_remaining (fruits_picked, fruits_quota):
    if fruits_quota<=fruits_picked:
        fruits_to_pick=0
    else:
        fruits_to_pick=fruits_quota-fruits_picked
    return fruits_to_pick
f=fruits_remaining (3,10)
print ("You need to pick additional fruits ",f)
# Call your function with a few different combination of values, and then print
# the result returned by your function.
def count (a,b):
    res_mult=a*b
    return res_mult
a=1
b=2
res_mult=count(a,b)
print(f"{a} * {b} = {res_mult}")
       