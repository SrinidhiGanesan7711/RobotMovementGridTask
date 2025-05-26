# robot/robot.py
class Robot:
    def __init__(self, robotId):
        self.robotId = robotId
        self.x = 0
        self.y = 0

    def currentLocation(self):
        return (self.x, self.y)
