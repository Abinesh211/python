import unittest

from robot_movement import Robot, Terrain

class TestRobotMovement(unittest.TestCase):
    def setUp(self):
        self.terrain = Terrain(5, 5)
        self.robot1 = Robot(1, self.terrain)
        self.robot2 = Robot(2, self.terrain)
    
    def test_initial_position(self):
        self.assertEqual(self.robot1.get_position(), (0, 0))
        self.assertEqual(self.robot2.get_position(), (0, 0))
    
    def test_move_robot1_east(self):
        self.robot1.move("E3")
        self.assertEqual(self.robot1.get_position(), (0, 3))
    
    def test_move_robot2_north(self):
        self.robot2.move("N2")
        self.assertEqual(self.robot2.get_position(), (2, 0))
    
    def test_collision(self):
        self.robot1.move("E3")
        self.robot2.move("N2")
        self.robot2.move("E1")  # Should collide with robot1
        self.assertEqual(self.robot2.get_position(), (2, 0))  # Should stop at (2, 0)

    def test_out_of_bounds(self):
        self.robot1.move("N5")  # Should stop at the top row
        self.assertEqual(self.robot1.get_position(), (0, 0))  # Should remain at (0, 0)

if __name__ == '__main__':
    unittest.main()
