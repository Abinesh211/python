#Robot Program Simulator
This program simulates robots moving on a grid-based terrain according to directional commands. Each robot has a unique ID and moves in response to inputs like "N4" (North 4 steps) or "E3" (East 3 steps). The program ensures that robots don’t move out of bounds or collide by entering cells occupied by other robots.

How to Run
Setup:

Ensure Python 3.x is installed.
Open the project folder in your terminal or Visual Studio Code.
Run the Program:

Run the following command to execute the unit tests:
bash
Copy code
python -m unittest robot_program.py
This command will check the robot’s initial positions, their movement in various directions, collision avoidance, and boundary checks.
Output:

After running, you should see test results that confirm whether each test case passed.
Example Command
To move a robot east by 3 steps, a command like "E3" can be used within the code.
This completes the basic setup and usage instructions for the Robot Program Simulator.
