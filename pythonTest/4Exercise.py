# 1.Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
i=1
while i<=1000:
    if i%3==0:
        print(i)
    i=i+1


# 2.Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
#
inches=int(input("please input the inches: "))
while inches>=0:
      centimeters=inches*2.54
      print(inches," inches converts to  ",centimeters," centimeters")
      inches = int(input("please input the inches: "))
print("the ends")





#
# 3.Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.
#

smallest=0
largest=0
inputNum=input("please enter the number: ")
while inputNum!="":
    if int(inputNum)>largest:
        largest=int(inputNum)
    elif int(inputNum)<smallest:
        smallest=int(inputNum)
    inputNum = input("please enter the number: ")
print("the largest is  ",largest," and the smallest is ",smallest)


# 4.Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.
#

import random
randomInt=random.randint(1,10)
print(randomInt)
guessNum=int(input("please input your num: "))
while guessNum!=randomInt:
    if guessNum>randomInt:
        print("Too high")
        guessNum=int(input("please input your num: "))
    else:
        print("Too low")
        guessNum = int(input("please input your num: "))
print("Correct")








# 5.Write a program that asks the user for a username and password.
#     If either or both are incorrect, the program ask the user to enter the username and password again.
#     This continues until the login information is correct or wrong credentials have been entered five times.
#     If the information is correct, the program prints out Welcome.
#     After five failed attempts the program prints out Access denied. The correct username is python and password rules.
#

cUsername="python"
cPassword="rules"
username=input("username: ")
password=input("password: ")
times=1
while  times<5 and (password!=cPassword or username!=cUsername):
    print("please log again")
    username = input("username: ")
    password = input("password: ")
    times=times+1
if times ==5:
    print("Access denied")
else:print("Welcome")



# 6.Implement an algorithm for calculating an approximation for the value of pi (π).
# Let's assume that A is a unit circle.
# A unit circle has the radius of one and it is centered at the origin (0,0).
# Smallest possible square B is drawn around the unit circle so that circle A is completely inside the square.
# The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1).
# If a large number of random points are scattered inside the square,
# the fraction of points that fall inside the circle A correlates with the fraction of the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4.
# This can be used as a simple method for calculating an approximation of the value of pi:
# Let's generate a large number of random points, such as one million, inside square B.
# Let N be the total number of random points. Each point inside the square is tested for whether it resides inside circle A.
# Let n be the total number of points that fall inside circle A.
# Now we have n/N≈π/4, and from that we get π≈4n/N.
# Write a program that asks the user how many random points to generate, and then calculates the approximate value of pi using the method explained above.
# At the end, the program prints out the approximation of pi to the user.
# (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).
import random
N=int(input("please enter the NUM: "))
i=1
n=0
while i<N:
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x*x+y*y<1:
       n+=1
    i+=1
print("π≈ ",4*n/N)