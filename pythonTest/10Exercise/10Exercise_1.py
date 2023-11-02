# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
# The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor.
# If you make elevator h for example the method call h.go_to_floor(5),
# the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
# The methods run the elevator one floor up or down and tell what floor the elevator is after each move.
# Test the class by creating an elevator in the main program,
# tell it to move to a floor of your choice and then back to the bottom floor.

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


if __name__ == '__main__':
    elevator = Elevator(1, 8)

    elevator.goToFloor(10)
    elevator.goToFloor(4)
    elevator.goToFloor(7)
    elevator.goToFloor(0)
    elevator.goTOBottom()



