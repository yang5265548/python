# Extend the program again by adding a method fire_alarm that
# does not receive any parameters and moves all elevators to the bottom floor.
# Continue the main program by causing a fire alarm in your building.

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.currentFloor = bottom

    def goToFloor(self, floorNum):
        if floorNum >= self.bottom and floorNum != self.currentFloor and floorNum < self.top:
            print(f"your current floor is {self.currentFloor},the elevator will move to floor {floorNum}~~~")
            if floorNum > self.currentFloor:
                for i in range(floorNum - self.currentFloor):
                    self.floorUp()

            elif floorNum < self.currentFloor:
                for i in range(self.currentFloor - floorNum):
                    self.floorDown()
        elif floorNum < self.bottom or floorNum > self.top:
            print("you enter  the wrong floor num ")
        else:
            print("you are on the right floor")

    def floorUp(self):
        if self.currentFloor < self.top:
            self.currentFloor += 1
            print(f"the current floor is {self.currentFloor}")
        else:
            print("you are on the top floor")

    def floorDown(self):

        if self.currentFloor > self.bottom:
            self.currentFloor -= 1
            print(f"the current floor is {self.currentFloor}")
        else:
            print("you are on the bottom floor")

    def goTOBottom(self):
        if self.currentFloor != self.bottom:
            print("the elevator will go to the bottom~~~")
            print("ku~~~ku~~~ku~~~")
            self.currentFloor = self.bottom
            print("now the elevator has go to the bottom~~~")
        else:
            print("now the elevator has go to the bottom~~~")


class Building:
    def __init__(self, bottom, top, nums):
        self.bottom = bottom
        self.top = top
        self.numsElevators = nums
        self.elevators = []
        for i in range(nums):
            elevator = Elevator(bottom, top)
            self.elevators.append(elevator)

    def run(self, num, desFloor):
        print(f"you choose the {num} elevator.")
        elevator = self.elevators[num-1]
        elevator.goToFloor(desFloor)

    def fireAlarm(self):
        print("the firealarm is ring~~~~~~ring~~~")
        for num,elevator in enumerate(self.elevators):
            print(f"the {num+1} elevator will go to the bottom floor~~~")
            elevator.goTOBottom()
        print("now all elevators are on the bottom floor")
if __name__ == '__main__':
    building = Building(1, 10, 3)
    building.run(3, 3)
    building.run(1,7)
    building.run(2,4)
    building.fireAlarm()



