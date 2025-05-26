# Robot Terrain Simulator 

This is a small Python project to simulate robots moving on a 2D grid. Robots can move north, south, east, or west using simple commands like `E2` (move east by 2). The grid prevents robots from going out of bounds or colliding with each other.

## Features

- Create multiple robots
- Assign each robot a unique ID
- Move robots on a grid using direction commands
- Prevent robots from moving into occupied or out-of-bound cells
- Track the current location of each robot

## Getting Started

1. Add a robot with `placeRobotOnGrid(robotId)`
2. Move it using `sendMoveCommand(robotId, 'DIRECTION+STEPS')`
3. Find out where it is using `whereIsMyRobot(robotId)`

## Steps to run the program

1. Clone the project:  
    ```bash
    git clone https://github.com/SrinidhiGanesan7711/RobotMovementGridTask.git
    cd RobotMovementGridTask
    ```

2. Update the Program (Optional):  
    You can give the necessary robot ID and direction+steps (e.g., E3, S2, N1, W4) in the `main.py` file like this:  
    ```python
    terrain.placeRobotOnGrid(1)
    terrain.sendMoveCommand(1, 'S2')
    print(terrain.whereIsMyRobot(1))  # Output: (0, 2)
    ```

3. Run the program:  
    ```bash
    python main.py
    ```

4. Run the test cases:  
    ```bash
    python -m unittest testRobot.py
    ```