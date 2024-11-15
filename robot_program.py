# robot_movement.py

class Terrain:
    def __init__(self, rows, cols):
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def is_within_bounds(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def is_occupied(self, x, y):
        return self.grid[x][y] is not None

    def place_robot(self, robot):
        x, y = robot.position
        self.grid[x][y] = robot.robot_id

    def move_robot(self, robot, new_x, new_y):
        x, y = robot.position
        self.grid[x][y] = None  # Clear previous position
        robot.position = (new_x, new_y)
        self.grid[new_x][new_y] = robot.robot_id  # Update new position


class Robot:
    def __init__(self, robot_id, terrain):
        self.robot_id = robot_id
        self.terrain = terrain
        self.position = (0, 0)
        terrain.place_robot(self)

    def move(self, command):
        direction, steps = command[0], int(command[1])
        x, y = self.position

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
                break

            x, y = new_x, new_y

        self.terrain.move_robot(self, x, y)

    def get_position(self):
        return self.position


# Unit Tests
import unittest

class TestRobotMovement(unittest.TestCase):
    def setUp(self):
        self.terrain = Terrain(5, 5)
        self.robot1 = Robot(1, self.terrain)
        self.robot2 = Robot(2, self.terrain)

    def test_initial_position(self):
        self.assertEqual(self.robot1.get_position(), (0, 0))
        self.assertEqual(self.robot2.get_position(), (0, 0))

    def test_move_robot(self):
        self.robot1.move("E3")
        self.assertEqual(self.robot1.get_position(), (0, 3))

    def test_collision_avoidance(self):
        self.robot1.move("E3")
        self.robot2.move("E3")  # Robot 2 should stop at (0, 2)
        self.assertEqual(self.robot2.get_position(), (0, 2))

    def test_out_of_bounds(self):
        self.robot1.move("N2")
        self.assertEqual(self.robot1.get_position(), (0, 0))

if __name__ == '__main__':
    unittest.main()
