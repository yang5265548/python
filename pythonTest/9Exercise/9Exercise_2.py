#2. Extend the program by adding an accerelate method into the new class.
# The method should receive the change of speed (km/h) as a parameter.
# If the change is negative, the car reduces speed. The method must change the value of the speed property of the object.
# The speed of the car must stay below the set maximum and cannot be less than zero. Extend the main program so that the speed
# of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h. Then print out the current speed of the car.
# Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
# The travelled distance does not have to be updated yet.
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


if __name__ == '__main__':
    car1=Car("SPN-913",140)
    car1.accerelate(30)
    car1.accerelate(70)
    car1.accerelate(50)
    car1.currtSpeed()
    car1.accerelate(-200)
    car1.currtSpeed()


