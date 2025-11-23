import unittest
from unittest.mock import patch, MagicMock
import robot

class TestRobot(unittest.TestCase):
    @patch('robot.GPIO')
    def test_robot_forward(self, mock_GPIO):
        r = robot.Robot(5, 6)
        r.forward(2)
        mock_GPIO.output.assert_any_call(5, mock_GPIO.HIGH)
        mock_GPIO.output.assert_any_call(6, mock_GPIO.HIGH)
        mock_GPIO.output.assert_any_call(5, mock_GPIO.LOW)
        mock_GPIO.output.assert_any_call(6, mock_GPIO.LOW)

    @patch('robot.GPIO')
    def test_robot_turn_right(self, mock_GPIO):
        r = robot.Robot(5, 6)
        r.turn_right(2)
        mock_GPIO.output.assert_any_call(5, mock_GPIO.HIGH)
        mock_GPIO.output.assert_any_call(6, mock_GPIO.LOW)
        mock_GPIO.output.assert_any_call(5, mock_GPIO.LOW)

    @patch('robot.GPIO')
    def test_robot_turn_left(self, mock_GPIO):
        r = robot.Robot(5, 6)
        r.turn_left(2)
        mock_GPIO.output.assert_any_call(5, mock_GPIO.LOW)
        mock_GPIO.output.assert_any_call(6, mock_GPIO.HIGH)
        mock_GPIO.output.assert_any_call(6, mock_GPIO.LOW)

    @patch('robot.GPIO')
    def test_robot_stop(self, mock_GPIO):
        r = robot.Robot(5, 6)
        r.stop()
        mock_GPIO.output.assert_any_call(5, mock_GPIO.LOW)
        mock_GPIO.output.assert_any_call(6, mock_GPIO.LOW)

    @patch('robot.GPIO')
    def test_robot_cleanup(self, mock_GPIO):
        r = robot.Robot(5, 6)
        r.cleanup()
        mock_GPIO.cleanup.assert_called_once()

if __name__ == '__main__':
    unittest.main()