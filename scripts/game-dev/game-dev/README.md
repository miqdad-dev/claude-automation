# Mini Puzzle Game

This is a simple puzzle game made with HTML, CSS, and JavaScript. The game consists of 8 numbered tiles and an empty space. The goal is to arrange the tiles in ascending order from the top left corner.

## How It Works

The game is built using pure JavaScript. The tiles are created and assigned a position on the game board. An event listener is added to each tile, which moves the tile to the empty space when clicked, if the tile is adjacent to the empty space.

## How to Run

1. Clone this repository.
2. Open the `index.html` file in a web browser.

## Example Usage

Click on a tile that is adjacent to the empty space to move it. Try to arrange the tiles in ascending order.

## Notes on Architecture & Tradeoffs

This game is implemented using vanilla JavaScript, which keeps the dependencies to a minimum. The tradeoff is that the code may not be as concise or as easy to read as it would be if a game development library were used. There are also no animations or transitions, which could make the game more visually appealing. However, the focus of this project is on the game logic rather than the visuals.