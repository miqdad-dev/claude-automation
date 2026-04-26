# Mini Snake Game

This is a simple, console-based implementation of the classic "Snake" game in Python. The game is played on a grid, where the player controls a snake that grows in length as it eats apples. The game ends when the snake collides with itself or the edge of the grid.

## How it Works

The game uses a simple 2D list to represent the grid, with different values representing the snake, apples, and empty spaces. The snake is controlled using the arrow keys, and the game is updated in real-time using a game loop.

## How to Run

1. Ensure you have Python 3 installed on your machine.
2. Clone this repository: `git clone <repo_url>`
3. Navigate to the project directory: `cd game-dev`
4. Run the game: `python snake_game.py`

## Example Usage

After running the game, you will see a grid displayed in your console. Use the arrow keys to control the snake and try to eat as many apples as you can. The game ends when the snake collides with itself or the edge of the grid.

## Architecture & Tradeoffs

The game is designed to be simple and easy to understand, with a minimal number of external dependencies. The main tradeoff is that the game uses a console-based interface, which is less visually appealing than a graphical interface. However, this choice keeps the implementation simple and portable.