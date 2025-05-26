import unittest
from robot.terrain import Terrain


class TestRobotMovement(unittest.TestCase):

    def testRobotStarting(self):
        terrain = Terrain(5, 5)
        terrain.placeRobotOnGrid(1)
        self.assertEqual(terrain.whereIsMyRobot(1), (0, 0))

    def testMoveSouthAndEast(self):
        terrain = Terrain(5, 5)
        terrain.placeRobotOnGrid(1)
        terrain.sendMoveCommand(1, 'S2')
        terrain.sendMoveCommand(1, 'E1')
        self.assertEqual(terrain.whereIsMyRobot(1), (1, 2))

    def testMoveEastAndWest(self):
        terrain = Terrain(2,3)
        terrain.placeRobotOnGrid(1)
        terrain.sendMoveCommand(1,'E2')
        terrain.sendMoveCommand(1,'W1')
        self.assertAlmostEqual(terrain.whereIsMyRobot(1),(1,0))

    def testRobotBlockedByAnother(self):
        terrain = Terrain(5, 5)

        terrain.placeRobotOnGrid(1)
        terrain.sendMoveCommand(1, 'S1')
        terrain.placeRobotOnGrid(2)
        terrain.sendMoveCommand(2,'S1')
        
        with self.assertRaises(Exception):
            terrain.placeRobotOnGrid(2)  

    def testRobotHitsWall(self):
        terrain = Terrain(5, 5)
        terrain.placeRobotOnGrid(1)
        terrain.sendMoveCommand(1, 'N2')  # Should stop at wall
        self.assertEqual(terrain.whereIsMyRobot(1), (0, 0))

    # 👎 Negative Cases
    def testDuplicateRobotId(self):
        terrain = Terrain(5, 5)
        terrain.placeRobotOnGrid(1)
        with self.assertRaises(Exception):
            terrain.placeRobotOnGrid(1)

    def testMoveNonExistentRobot(self):
        terrain = Terrain(5, 5)
        with self.assertRaises(Exception):
            terrain.sendMoveCommand(99, 'S1')

    def testGetPositionNonExistentRobot(self):
        terrain = Terrain(5, 5)
        with self.assertRaises(Exception):
            terrain.whereIsMyRobot(5)

    def testInvalidDirection(self):
        terrain = Terrain(5, 5)
        terrain.placeRobotOnGrid(1)
        with self.assertRaises(ValueError):
            terrain.sendMoveCommand(1, 'G3')  

    def testInvalidCommandFormat(self):
        terrain = Terrain(5, 5)
        terrain.placeRobotOnGrid(1)
        with self.assertRaises(ValueError):
            terrain.sendMoveCommand(1, 'E')   
        with self.assertRaises(ValueError):
            terrain.sendMoveCommand(1, 'Sx')  

if __name__ == '__main__':
    unittest.main()
