import curses
from snake_game import SnakeGame

def test_snake_game():
    screen = curses.initscr()
    game = SnakeGame(screen)
    assert game.snake is not None
    assert game.food is not None
    assert game.direction is not None
    assert game.update() == True