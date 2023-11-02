# Extend the previous program by creating a Building class.
# The initializer parameters for the class are the numbers of the bottom and top floors and the number of
# elevators in the building. When a building is created, the building creates the required number of elevators.
# The list of elevators is stored as a property of the building.
# Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters.
# In the main program, write the statements for creating a new building and running the elevators of the building.

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


if __name__ == '__main__':
    building = Building(1, 10, 3)
    building.run(3, 3)
    building.run(3,7)
    building.run(3,1)



