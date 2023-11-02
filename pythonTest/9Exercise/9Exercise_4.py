# Now we will program a car race.
# The travelled distance of a new car is initialized as zero.
# At the beginning of the main program,
# create a list that consists of 10 car objects created using a loop.
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
# The registration numbers are created as follows: "ABC-1", "ABC-2" and so on.
# Now the race begins.
# One per every hour of the race, the following operations are performed:
#
# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
# This is done using the accerelate method.
# Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers.
# Finally, the properties of each car are printed out formatted into a clear table.
from random import random, randint

from tabulate import tabulate


class Car:
    def __init__(self,regisNum,maxSpeed,currSpeed=0,travelDis=0):
        self.regisNum=regisNum
        self.maxSpeed=maxSpeed
        self.currSpeed=currSpeed
        self.travelDis=travelDis
    def accerelate(self,speed):
        self.currSpeed+=speed
        if self.currSpeed>self.maxSpeed:
            self.currSpeed=self.maxSpeed
        elif self.currSpeed<0:
            self.currSpeed=0
    def currtSpeed(self):
        print(f"the current speed is :{self.currSpeed} km/h")

    def dirve(self,drivingTime):
        self.travelDis+=self.currSpeed*drivingTime
    def currentDis(self):
        print(f"the current distence is :{self.travelDis} km")



if __name__ == '__main__':
    cars=[]
    for i in range(10):
        car=Car(f"ABC-{i+1}",randint(100,200))
        cars.append(car)
    i=1
    while True:

        # print(F"the {i} hour")
        disList=[]
        for car in cars:
            disList.append(car.travelDis)

        if max(disList)>10000:
            print(f"the max distance is :{max(disList)}")
            break
        else:
            for car in cars:
                car.accerelate(randint(-10,15))
                car.dirve(1)
        i += 1
    tableItem=[]
    for i,car in enumerate(cars):
        tableItem.append((i,car.regisNum,car.maxSpeed,car.currSpeed,car.travelDis))
    data=tableItem
    headers = ["num", "regisNum", "maxSpeed","currSpeed","travelDis"]

    table = tabulate(data, headers, tablefmt="pipe")

    print(table)


