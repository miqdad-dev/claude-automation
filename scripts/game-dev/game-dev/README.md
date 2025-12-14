# Mini Snake Game

This is a simple implementation of the classic game Snake, using Python's built-in `curses` library for text-based user interfaces.

## What it Does

The game starts with a small snake in the middle of the screen, moving in a random direction. The snake can be controlled by the arrow keys. There is a piece of food randomly placed on the screen. When the snake eats the food, it grows longer and the score increases. The game ends when the snake runs into the screen border or into itself.

## How it Works

The game logic is handled by the `SnakeGame` class. This class holds the state of the game and handles user input and game updates.

The game screen is drawn using `curses` library functions. The snake is represented as a deque of coordinates on the screen, and the food as a single coordinate.

On each game update, the snake moves in the current direction. If the new position of the snake's head is the same as the food's position, the food is eaten and a new piece of food is placed. If the new position is outside the screen border or in the snake's body, the game ends.

## How to Run

This game requires Python 3.5+ and the `curses` library. To play the game, clone this repository and run `python snake_game.py`.

## Example Usage

Here is a typical game session: