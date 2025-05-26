from robot.terrain import Terrain

terrain = Terrain(numberOfRows=7, numberOfColumns=5)

terrain.placeRobotOnGrid(1)
terrain.sendMoveCommand(1, 'E2')
terrain.sendMoveCommand(1, 'W1')

terrain.placeRobotOnGrid(2)
terrain.sendMoveCommand(2, 'E3')
terrain.sendMoveCommand(2, 'S6')

terrain.placeRobotOnGrid(3)
terrain.sendMoveCommand(3, 'S3')
terrain.sendMoveCommand(3, 'E4')

print("Robot 1 is now at", terrain.whereIsMyRobot(1))
print("Robot 2 is now at", terrain.whereIsMyRobot(2))
print("Robot 3 is now at", terrain.whereIsMyRobot(3))
