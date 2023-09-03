# 1.Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit,
# the program instructs to release the fish back into the lake and notifies the user of
# how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.
#

length=float(input("how long is the zander? "))
if length<42:
    print("please release the fish back to lake,the fish less than ",42-length)
else:print("you get a big fish,the length is ",length)


# 2.Write a program that asks the user to enter the cabin class of a cruise ship and
# then prints out a written description according to the list below.
# You must use an if/elif/else structure in your solution.
# LUX: upper-deck cabin with a balcony.
# A: above the car deck, equipped with a window.
# B: windowless cabin above the car deck.
# C: windowless cabin below the car deck.
# If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.
#

userCabin=input("please enter your cabin class: ")
if userCabin=="LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif userCabin=="A":
    print("A: above the car deck, equipped with a window.")
elif userCabin=="B":
    print("B: windowless cabin above the car deck.")
elif userCabin=="C":
    print("C: windowless cabin below the car deck.")
else:print("You enter the worng cabin class")




# 3.Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.
# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.

gender=input("what is your gender: ")
hemoglobin=float(input("what is the value of your hemoglobin :"))
if gender=="male" or gender=="man":
    if hemoglobin<134:
        print("your hemoglobin value is low ")
    elif hemoglobin>167:
        print("your hemoglobin value is high ")
    else:print("your hemoglobin value is normal  ")
elif gender=="female" or gender=="woman":
    if hemoglobin<117:
        print("your hemoglobin value is low ")
    elif hemoglobin>155 :
        print("your hemoglobin value is high ")
    else:print("your hemoglobin value is normal  ")
else:print("you put the wrong information")



# 4.Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four.
# However, years divisible by 100 are leap years only if they are also divisible by 400.
year=int(input("please enter a year: "))
if year%4==0:
    print("the year is a leap year")
elif year%100==0 and year%400==0:
    print("the year is a leap year")
else:print("the year is not a leap year")