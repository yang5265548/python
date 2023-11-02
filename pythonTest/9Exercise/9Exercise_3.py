#3. Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km.
# The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to 2090 km.
#
class Car:
    def __init__(self,registationNum,maxSpeed,currSpeed=0,travelDis=0):
        self.registationNum=registationNum
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
    car1=Car("SPN-913",140,60,1000)
    car1.dirve(1.7)
    car1.currentDis()


