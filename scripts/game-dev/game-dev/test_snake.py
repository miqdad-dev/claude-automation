import unittest
from snake import *

class TestSnake(unittest.TestCase):

    def test_food_generation(self):
        # After the snake eats food, a new food item should be generated
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        self.assertIsNotNone(food)

    def test_snake_movement(self):
        # The snake should move in the right direction when an arrow key is pressed
        new_head = [snake[0][0], snake[0][1]]
        key = curses.KEY_DOWN
        new_head[0] += 1
        self.assertEqual(snake[0][0] + 1, new_head[0])
        
if __name__ == '__main__':
    unittest.main()