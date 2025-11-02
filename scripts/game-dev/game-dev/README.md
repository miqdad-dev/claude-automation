# Mini Hard Game Project: 2D Array Maze Game

This is a simple command-line game where a player needs to navigate through a 2D maze from start point (S) to end point (E). The game uses Node.js for implementation.

## What it does

The game presents a randomly generated 2D maze where a player starts at position (S) and the goal is to reach the end (E). The player can move either up, down, left, or right. Walls are represented with `#` and open paths are represented with `.`.

## How it works

The game uses a Depth-first search (DFS) algorithm to generate the maze. The player's position is tracked and updated after each move. The game ends when the player reaches the end point (E).

## How to run

1. Clone the repository.
2. Navigate to the root directory.
3. Run `npm install` to install dependencies.
4. Run `node game.js` to start the game.

## Example Usage

The game will display the current state of the maze after each move. Here is an example of the game: