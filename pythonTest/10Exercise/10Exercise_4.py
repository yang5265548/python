# This exercise continues the previous car race exercise from the last exercise set.
# Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race.
# The class has an initializer that receives the name, kilometers,
# and car list as parameters and sets their values to the corresponding properties in the class.
# The class has the following methods:
#
# hour_passes, which performs the operations done once per hour in the original exercise:
# generates a random change of speed for each car and calls their drive method.
# print_status, which prints out the current information of each car as a clear, formatted table.
# race_finished, which returns True if any of the cars has reached the finish line,
# meaning that they have driven the entire distance of the race.
# Write a main program that creates an 8000-kilometer race called Grand Demolition Derby.
# The new race is given a list of ten cars similarly to the earlier exercise.
# The main program simulates the progressing of the race by calling the hour_passes in a loop,
# after which it uses the race_finished method to check if the race has finished.
# The current status is printed out using the print_status method every ten hours and then once more at the end of the race.

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
class Race:
    def __init__(self,name,distance,cars):
        self.name=name
        self.distance=distance
        self.cars=cars
    def hour_passes(self):
        for car in self.cars:
            car.accerelate(randint(-10, 15))
            car.dirve(1)

    def print_status(self):
        tableItem = []
        for i, car in enumerate(self.cars):
            tableItem.append((i, car.regisNum, car.maxSpeed, car.currSpeed, car.travelDis))
        data = tableItem
        headers = ["num", "regisNum", "maxSpeed", "currSpeed", "travelDis"]

        table = tabulate(data, headers, tablefmt="pipe")

        print(table)
    def race_finished(self):
        while True:

            # print(F"the {i} hour")
            disList = []
            for car in self.cars:
                disList.append(car.travelDis)

            if max(disList) > self.distance:
                print(f"the max distance is :{max(disList)}")
                return  True
            else:
                return False


if __name__ == '__main__':
    cars=[]
    for i in range(10):
        car=Car(f"ABC-{i+1}",randint(100,200))
        cars.append(car)
    race=Race("Grand Demolition Deby",8000,cars)
    i=1
    while True:


        disList = []
        for car in cars:
            disList.append(car.travelDis)

        if max(disList) > race.distance:
            print(f"the max distance is :{max(disList)}")
            break
        else:
             race.hour_passes()
        i+=1
        if i%10==0:
            print(F"the {i} hour")
            race.print_status()
            print("  ")

    race.print_status()




