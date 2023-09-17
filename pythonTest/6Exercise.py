# 1.Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters. Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.
#
import random
def roll():
      num=random.randint(1,6)
      print(f"this time the dice is {num}")
      return  num
num=0
while num!=6:
   num=roll()















# 2.Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.
# The difference to the last exercise is that the dice rolling in the main program continues
# until the program gets the maximum number on the dice, which is asked from the user at the beginning.
#

import random
def roll(num1):
      num=random.randint(1,num1)
      print(f"this time the dice is {num}")
      return  num
num=0
num1=int(input("please enter the num of the sides: "))
while num!=num1:
   num=roll(num1)













# 3.Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function.
# Conversions continue until the user inputs a negative value.
#
def gallon_convert_to_liter(gallonsNum):
    liter=gallonsNum*3.785
    return liter
gallonsNum =0
liter=0
while True:
    gallonsNum = float(input("please enter the num of gallons: "))
    if gallonsNum>=0:
       liter=gallon_convert_to_liter(gallonsNum)
       print(f"{gallonsNum} gallons = {liter} liters")
    else:
        print("the gallonsNum is a negative value")
        break











# 4.Write a function that gets a list of integers as a parameter.
# The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list, call the function, and print out the value it returned.
#

def sum_list(list,sum):
    for i in list:
        sum+=i
    return  sum

sum=0
list=[]
while True:
    num=input("please enter the num: ")
    if num!="" :
        list.append(int(num))
    else:
        break
sum=sum_list(list,sum)
print(f"the sum of enter number is {sum}")











# 5.Write a function that gets a list of integers as a parameter.
# The function returns a second list that is otherwise the same as the original list except that all
# uneven numbers have been removed. For testing, write a main program where you create a list,
# call the function, and then print out both the original as well as the cut-down list.
#


#
def removeTheUnevenNum(list):
    newList=[]
    for i in list:
        if i%2==0:
            newList.append(i)
    return newList
# list=[1,2,3,4,5,6,7]
list=[]
while True:
    num=input("please enter the num: ")
    if num!="" :
        list.append(int(num))
    else:
        break
newlist=removeTheUnevenNum(list)
print(f"the orginal list:{list}")
print(f"the cut_down list:{newlist}")

#
#





# 6.Write a function that receives two parameters: the diameter of a round pizza in centimeters
# and the price of the pizza in euros. The function calculates and
# returns the unit price of the pizza per square meter.
# The main program asks the user to enter the diameter and price of two pizzas
# and tells the user which pizza provides better value for money (which of them has a lower unit price).
# You must use the function you wrote for calculating the unit prices.
#
def calculatePizzaUnitPrice(diameter,price):
    unitPrice=price/(3.1415926*((diameter/100)**2))
    return unitPrice
firstSize=float(input("please enter the first pizza diameter: "))
firstPrice=float(input("please enter the first pizza price: "))
secondSize=float(input("please enter the second pizza diameter: "))
secondprice=float(input("please enter the second pizza price: "))
firstUnitPrice=round(calculatePizzaUnitPrice(firstSize,firstPrice),4)
secondUnitPrice=round(calculatePizzaUnitPrice(secondSize,secondprice),4)
if firstUnitPrice<secondUnitPrice:
    print(f"the first pizza is more cheaper,the unit price is {firstUnitPrice} euros")
elif firstUnitPrice>secondUnitPrice:
    print(f"the second pizza is more cheaper,the unit price is {secondUnitPrice} euros")
else:print(f"the tow pizza are same unit price {firstUnitPrice} euros")



