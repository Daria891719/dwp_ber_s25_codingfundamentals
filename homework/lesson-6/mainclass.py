# Write an if statement which checks if a value is above a given quota. If the
# value is greater or equal to the quota, print "Done". Otherwise print "Not done"
quota=1000
sum1=int(input("Please, write you sum: "))
if sum1>=quota:
    print ("Done")
else:
    print ("Not done")
# Copy/paste your code above and slightly tweak it to change what is being printed
# If the value is greater or equal to the quota, print 0 (zero)
# Otherwise print the result of: quota - value
if sum1>=quota:
    print ("0")
else:
    print ("The sum is ", sum1, ", the quota is", str(quota))
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


#Let's say a fruit picker picks an amount of fruits 4 days a week.
# If they reach quota, they get Friday free, otherwise they have to work on Friday.
# Create/define a function called is_friday_off which takes parameters, a list of
# 'fruit_picks' and 'fruits_quota'. This function should return a boolean value:
# - True if the fruit picker has reached quota and gets Friday off.
# - False if the fruit picker has not reached quota and does not get Friday off.
# Call this function with the two following lists, and a quota of 880.
# fruit_picks_1 = [223, 212, 202, 234]
# fruit_picks_2 = [200, 256, 189, 240]
print ("Reaching the quota during 4 days")
def is_friday_off (quantity_fruits, quota):
    fruit_picks=sum (quantity_fruits)
    if fruit_picks>=quota:
       print ("You reached the quota. You can take friday off!")
       return True
    else:
        print ("You did not reach the quota. You cannot take Friday off! You need to pick additional quontity: ", quota-fruit_picks)
        return False
quota=880
fruit_picks_1 = [223, 212, 202, 234]
fruit_picks_2 = [200, 256, 189, 240]
print ("Case 1. Friday is off:", is_friday_off (fruit_picks_1, quota))
print ("Case 2. Friday is off:", is_friday_off (fruit_picks_2, quota))
