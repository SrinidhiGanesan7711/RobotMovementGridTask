# Robot Terrain Simulator 

This is a small Python project to simulate robots moving on a 2D grid. Robots can move north, south, east, or west using simple commands like `E2` (move east by 2). The grid prevents robots from going out of bounds or colliding with each other.

## Getting Started

1. Add a robot with `placeRobotOnGrid(robotId)`
2. Move it using `sendMoveCommand(robotId, 'DIRECTION+STEPS')`
3. Find out where it is using `whereIsMyRobot(robotId)`

## Quick Example

```python
terrain.placeRobotOnGrid(1)
terrain.sendMoveCommand(1, 'S2')
print(terrain.whereIsMyRobot(1))  # Should print: (0, 2)