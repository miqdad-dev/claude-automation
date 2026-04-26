import unittest
from snake_game import SnakeGame

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.game = SnakeGame()

    def test_game_starts(self):
        self.assertEqual(self.game.state, "RUNNING")

    def test_snake_moves(self):
        initial_snake_head_position = self.game.snake[0]
        self.game.update()
        self.assertNotEqual(self.game.snake[0], initial_snake_head_position)

    def test_game_ends(self):
        self.game.snake.insert(0, self.game.snake[0])
        self.game.update()
        self.assertEqual(self.game.state, "GAME_OVER")

if __name__ == '__main__':
    unittest.main()