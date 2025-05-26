# robot/terrain.py
from .robot import Robot

class Terrain:
    def __init__(self, numberOfRows, numberOfColumns):
        self.rows = numberOfRows
        self.cols = numberOfColumns
        self.robotsById = {}       
        self.gridOccupancy = {}    

    def placeRobotOnGrid(self, robotId):
        # Check-duplicate robot id
        if robotId in self.robotsById:
            raise Exception(f"Robot ID {robotId} is already placed on the grid")
        
        robot = Robot(robotId)
        self.robotsById[robotId] = robot
        if (0, 0) not in self.gridOccupancy:
            self.gridOccupancy[(0, 0)] = robotId
        else:
            raise Exception("The starting spot (0, 0) is already taken!")

    def sendMoveCommand(self, robotId, movementCommand):
        if robotId not in self.robotsById:
            raise Exception("No robot with that ID exists")

        if len(movementCommand) < 2 or not movementCommand[1:].isdigit():
            raise ValueError("Invalid movement command format")

        robot = self.robotsById[robotId]
        direction = movementCommand[0]
        steps = int(movementCommand[1:])

        moveX, moveY = 0, 0
        if direction == 'N':
            moveY = -1
        elif direction == 'S':
            moveY = 1
        elif direction == 'E':
            moveX = 1
        elif direction == 'W':
            moveX = -1
        else:
            raise ValueError("Thats not a valid direction")

        for _ in range(steps):
            nextX = robot.x + moveX
            nextY = robot.y + moveY

            if not (0 <= nextX < self.cols and 0 <= nextY < self.rows):
                break
            if (nextX, nextY) in self.gridOccupancy:
                break

            del self.gridOccupancy[(robot.x, robot.y)]
            robot.x, robot.y = nextX, nextY
            self.gridOccupancy[(robot.x, robot.y)] = robotId

    def whereIsMyRobot(self, robotId):
        if robotId not in self.robotsById:
            raise Exception("Robot not found on the terrain")
        return self.robotsById[robotId].currentLocation()
