number1=10
number2=5
print(number1>=number2)
number3=30
number4=45
print(number3==number4)
pi = 3.14
print(pi==3.14)
#page 75 of the presentation
name="Mustermann"
surname="Gabler"
vorname="Erika"
date_of_birthday="12.08.1964"
gender="F"
nationality="Deutsch"
place_of_birth="Berlin"
date_of_issue="01.03.2017"
date_of_expiry="28.02.2027"
authority="Stadt Köln"
print(name," ",surname, " ",vorname)
print("Date of birthday ",date_of_birthday,";","Gender ",gender,"; Nationality ",nationality,"; Place of birth ",place_of_birth)
print("Date of issue ",date_of_issue,";","Date of expiry ",date_of_expiry,"; Authority ",authority)


# Variables and Basic Data Types
my_number=10
my_string="Hello, Python!"
my_float=3.14
print (my_number)
print (my_string)
print (my_float)
print (" ")
# Working with Different Data Types
first_name="Daria"
last_name="Zdorik"
full_name=last_name+first_name
print (full_name)
print (" ")
a = 5 
b = 3
add_result=a+b
sub_result=a-b
mult_result=a*b
div_result=a/b
print (add_result)
print (sub_result)
print (mult_result)
print (div_result)
print (" ")
# Booleans and Comparisons
is_greater=a>b
is_equal=a==b
is_smaller=a<b
print ("It is ",is_greater, "that ", a, "greater than",b)
print ("It is ",is_equal, "that ", a, "equal",b)
print ("It is ",is_smaller, "that ", a, "smaller than",b)
print (" ")

bool1 = True 
bool2 = False
print(((type (a) and type (b))==int)==bool1)
tempreture_yesterday=8
tempreture_today=9
tempreture_tomorrow=10
weather_forecast=9
dif1=tempreture_today-tempreture_yesterday
dif2=tempreture_tomorrow-tempreture_today
for_today=weather_forecast-tempreture_today
if dif1>=0 and dif2>=0:
    print("The weather is getting warmer") 
if (dif1>=0 and dif2<=0) or  (dif1<=0 and dif2>=0):
    print("The weather is unstable") 
if dif1<=0 and dif2<=0:
    print("The weather is getting colder")
if for_today>0 or for_today<0:
    print("The Weather forecast was ", bool2)
if for_today==0:
    print("The Weather forecast was ",bool1)
if not for_today:
    print ("There is not difference in the forecast and real temterature")
print (" ")
# Type checking and conversion
pi = 3.14
pi_pi = '3.14'
pi_pi_pi = "3.14"
print(type(pi))
print(type(pi_pi))
print(type(pi_pi_pi))
print (" ")
my_str = "123"
my_int =123
my_float_converted=12.3
# Challenge
celsius=13
fahrenheit=(celsius * 9/5) + 32 
print("temperature is ",celsius, "celsius and ", fahrenheit, "fahrenheit")
