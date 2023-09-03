# 1.Write a program that asks your name and then greets you by your name: Examples:
#
# If you enter Viivi as your name, the program will greet you with Hello, Viivi!.
# If you enter Ahmed as your name, the program will greet you with Hello, Ahmed!.

name=input("What is your name? ")
print(f"Hello ,{name}")

# 2.Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

pi=3.1415926
radius=float(input("put the radius of the circle: "))
print(f"the area of the circle is {pi*radius*radius}")



# 3.Write a program that asks the user for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides.

width=float(input("put the width of the rectangle: "))
lengh=float(input("put the lengh of the rectangle: "))
area=width*lengh
perimeter=2*(width+lengh)
print(f"the area of the rectangle is {area}")
print(f"the perimeter of the rectangle is {perimeter}")

# 4.Write a program that asks the user for three integer numbers.
# The program prints out the sum, product, and average of the numbers.

firstIntNum=int(input("Please put the first int number: "))
secondIntNum=int(input("Please put the second int number: "))
thirdIntNum=int(input("Please put the third int number: "))
sum=firstIntNum+secondIntNum+thirdIntNum
product=firstIntNum*secondIntNum*thirdIntNum
average=sum/3
print(f"the sum is {sum},the product is {product},the average is {average} ")

# 5.Write a program that asks the user to enter a mass in medieval units:
# talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user:
#
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.

talents=float(input("Enter talents: "))
pounds=float(input("Enter pounds: "))
lots=float(input("Enter lots: "))
changeTalents2grams=talents*20*32*13.3
changePounds2grams=pounds*32*13.3
changeLots2grams=lots*13.3
total=changeTalents2grams+changePounds2grams+changeLots2grams
kgUnit=total/1000
gramsUnit=total-int(kgUnit)*1000
print("The weight in modern units:")
print(f"{int(kgUnit)} kilograms and {round(gramsUnit,3)}  grams. ")

#6. Write a program that draws two random combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.

import  random

threeDigitCode="".join(map(lambda x: str(random.randint(0,9)),range(3)))
fourDigitCode="".join(map(lambda x: str(random.randint(1,6)),range(4)))
print("The 3-digit code is : ",threeDigitCode," and The 4-digit code is : ",fourDigitCode)

# a=str(random.randint(0,9))
# b=str(random.randint(0,9))
# c=str(random.randint(0,9))
# d=str(random.randint(1,6))
# e=str(random.randint(1,6))
# f=str(random.randint(1,6))
# g=str(random.randint(1,6))
#

# print("The 3-digit code is : ",a+b+c," and The 4-digit code is : ",d+e+f+g)



