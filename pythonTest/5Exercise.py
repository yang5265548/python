# 1.Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.
#
import random
num=int(input("how many dice do you whant to roll: "))
sum=0
nums=0
for i in range(num):
    nums=random.randint(1,6)
    sum+=nums
print(sum)






# 2.Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
#
list=[]
num=input("please enter a num: ")
while num!="":
    list.append(float(num))
    num = input("please enter a num: ")
print(list)
list.sort()
list.reverse()
if len(list)>=5:
    print(list[:5])
else:print(list)






# 3.Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
#
# For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

num=int(input("please put a integer: "))
flag=True
if num ==1:
    print("the num is not prime")
else:
    for i in range(2,num//2+1):
        if num%i==0:
           flag=False
           break
    if flag:
       print("the num is prime")
    else:
       print("the num is not prime")





# 4.Write a program that asks the user to enter the names of five cities one by on
# (use a for loop for reading the names) and stores them into a list structure.
# Finally, the program prints out the names of the cities one by one, one city per line,
# in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.
list=[]
for i in range(5):
    city=input("please enter the name of city: ")
    list.append(city)
for i in list:
    print(i)