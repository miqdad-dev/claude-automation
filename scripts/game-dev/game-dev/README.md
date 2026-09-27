# Mini-hard Game Dev Project - Snake Game

This project is a simple implementation of the popular game "Snake". The snake moves in a grid, and the player scores points by eating apples that randomly appear on the grid. The game ends when the snake collides with itself.

## How it Works

The game uses JavaScript for the logic and HTML5 Canvas for rendering. The snake is represented as an array of grid cells, where each cell is an object with x and y properties that represent its position on the grid.

The snake moves by adding a new head to the front of the array and removing the tail. When the snake eats an apple, the tail is not removed, effectively increasing the length of the snake.

## How to Run

You can run the game by opening index.html in your web browser.

## Example Usage

Use the arrow keys to direct the snake towards the apples.

## Architecture & Tradeoffs

The game uses a simple game loop that updates the game state and renders the game at a set interval. This makes the implementation straightforward but it also means that the game speed is tied to the frame rate.

For a more complex game, a better approach might be to use delta timing to ensure consistent game speed regardless of the frame rate.

The game does not currently handle window resizing or high DPI displays. This could be improved in a future version.