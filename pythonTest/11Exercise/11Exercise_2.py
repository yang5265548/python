#Extend the previosly written Car class by adding two subclasses:
# ElectricCar and GasolineCar.
# Electric cars have the capacity of the battery in kilowatt-hours as their property.
# Gasoline cars have the volume of the tank in liters as their property.
# Write initializers for the subclasses.
# For example, the initializer of electric cars receives the registration number,
# maximum speed and battery capacity as its parameter.
# It calls the initializer of the base class to set the first two properties and then sets its capacity.
# Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh)
# and one gasoline car (ACD-123, 165 km/h, 32.3 l).
# Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.
class Car:
    def __init__(self,registationNum,maxSpeed,currSpeed=0,travelDis=0):
        self.registationNum=registationNum
        self.maxSpeed=maxSpeed
        self.currSpeed=currSpeed
        self.travelDis=travelDis
    def carInfo(self):
        print(f"the car registationNum :{self.registationNum},maxSpeed:{self.maxSpeed},currSpeed:{self.currSpeed},travelDis:{self.travelDis} ")
    def accerelate(self,speed):
        self.currSpeed+=speed
        if self.currSpeed>self.maxSpeed:
            self.currSpeed=self.maxSpeed
        elif self.currSpeed<0:
            self.currSpeed=0
    def currtSpeed(self):
        print(f"{self.registationNum} the current speed is :{self.currSpeed} km/h")

    def dirve(self,drivingTime):
        self.travelDis+=self.currSpeed*drivingTime
    def currentDis(self):
        print(f"{self.registationNum}  the current distence is :{self.travelDis} km")
class ElectricCar(Car):
    def __init__(self,registationNum,maxSpeed,capacity):
        super().__init__(registationNum,maxSpeed)
        self.capacity=capacity
class GasolineCar(Car):
    def __init__(self,registationNum,maxSpeed,volume ):
        super().__init__(registationNum,maxSpeed)
        self.volume =volume
if __name__ == '__main__':
    ecar=ElectricCar("ABC-15",180,52.5)
    gcar=GasolineCar("ACD-123",165 ,32.3 )
    ecar.accerelate(80)
    gcar.accerelate(50)
    ecar.dirve(3)
    gcar.dirve(3)
    ecar.currentDis()
    gcar.currentDis()