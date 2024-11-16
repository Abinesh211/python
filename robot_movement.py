import time

# Define the grid (terrain) where robots will move
class Terrain:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        
    def is_within_bounds(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols
    
    def is_occupied(self, x, y):
        return self.grid[x][y] is not None
    
    def move_robot(self, robot, x, y):
        if self.is_within_bounds(x, y) and not self.is_occupied(x, y):
            self.grid[robot.x][robot.y] = None  # Clear the old position
            self.grid[x][y] = robot  # Assign the robot to the new position
            robot.x, robot.y = x, y  # Update robot's position

# Define the Robot class
class Robot:
    def __init__(self, robot_id, terrain):
        self.robot_id = robot_id
        self.x, self.y = 0, 0  # Robots start at position (0, 0)
        self.terrain = terrain
        terrain.grid[self.x][self.y] = self  # Place robot at starting position

    def move(self, command):
        direction, steps = command[0], int(command[1:])
        x, y = self.x, self.y

        # Define movement logic based on direction
        for _ in range(steps):
            new_x, new_y = x, y
            if direction == 'N':
                new_x -= 1
            elif direction == 'E':
                new_y += 1
            elif direction == 'S':
                new_x += 1
            elif direction == 'W':
                new_y -= 1

            if not self.terrain.is_within_bounds(new_x, new_y) or self.terrain.is_occupied(new_x, new_y):
                break  # Stop if out of bounds or if destination is occupied

            x, y = new_x, new_y

        # Move the robot to the new position
        self.terrain.move_robot(self, x, y)

    def get_position(self):
        return self.x, self.y

# Main function to simulate the program and track time
def main():
    # Initialize terrain (5x5 grid)
    terrain = Terrain(5, 5)
    
    # Create robots with unique IDs
    robot1 = Robot(1, terrain)
    robot2 = Robot(2, terrain)
    
    # Time tracking for the entire program
    start_time = time.time()
    
    # Simulate robot movements
    robot1.move("E3")  # Move robot1 3 steps to the East
    robot2.move("N2")  # Move robot2 2 steps to the North
    
    # Display the positions of the robots
    print(f"Robot 1 position: {robot1.get_position()}")
    print(f"Robot 2 position: {robot2.get_position()}")
    
    # End time tracking
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Total Program Execution Time: {execution_time:.4f} seconds")

if __name__ == "__main__":
    main()

