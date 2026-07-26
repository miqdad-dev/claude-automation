import unittest
from robot import Robot

class TestRobot(unittest.TestCase):
    def test_move(self):
        robot = Robot()
        self.assertEqual(robot.position, (0, 0))
        robot.move('up')
        self.assertEqual(robot.position, (0, 1))
        robot.move('right')
        self.assertEqual(robot.position, (1, 1))
        robot.move('down')
        self.assertEqual(robot.position, (1, 0))
        robot.move('left')
        self.assertEqual(robot.position, (0, 0))

if __name__ == '__main__':
    unittest.main()