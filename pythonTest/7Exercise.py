# Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.
#




seasonTuple=(("spirng",3,4,5),("summer",6,7,8),("autumn",9,10,11),("winter",12,1,2))
month=int(input("please enter the num of the month: "))
for  a in enumerate(seasonTuple):

    if month == a[1][1] or month == a[1][2] or month == a[1][3] :
        print(f"the {month} month is {a[1][0]}  ")

















# Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or Existing name depending on whether the name was entered
# for the first time. Finally, the program lists out the input names one by one, one below another in any order.
# Use the set data structure to store the names.
#

a=set()
str=input("please enter a name : ")
while str!="":
    if not a.issuperset({str}):
        print(f"it's a new name {str}")
        a.add(str)
    else:print(f"it's a exist name {str}")
    str = input("please enter a name : ")
print("all name:")
for i in range(a.__len__()):
    print(a.pop())
















# Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit. If the user chooses to enter a new airport,
# the program asks the user to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead,
# the program asks for the ICAO code of the airport and prints out the corresponding name.
# If the user chooses to quit, the program execution ends.
# The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport. For example,
# the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)

def getRequest():
    print("1.enter a new airport")
    print("2.fetch the information of a airport")
    print("3.quit")
    request=input("please entter your request 1/2/3 : ")
    return request


airport={}
request=getRequest()
while int(request)!=3:
    if int(request)==1:
        airportName=input("please enter the name of the airport: ")
        ICAO=input("please enter the ICAO code of the airport: ")
        airport[ICAO]=airportName
        request = input("please entter your request 1/2/3 : ")
    elif int(request)==2:
        ICAO=input("please enter the ICAO code of the airport: ")
        if airport.__contains__(ICAO):
           print(airport[ICAO])
        else:print("there is no information of the airport~~")
        request = input("please entter your request 1/2/3 : ")
    else:
        print("you enter the wrong selection code~~")
        request=input("please enter your request 1/2/3 : ")

print("bye bye")