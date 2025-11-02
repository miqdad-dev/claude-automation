const readlineSync = require('readline-sync');

class Game {
    constructor() {
        this.maze = [];
        this.playerPosition = { x: 1, y: 1 };
        this.endPosition = { x: 5, y: 5 };
        this.generateMaze();
    }

    generateMaze() {
        for (let i = 0; i < 7; i++) {
            this.maze[i] = [];
            for (let j = 0; j < 7; j++) {
                if (i === 0 || j === 0 || i === 6 || j === 6) {
                    this.maze[i][j] = '#';
                } else {
                    this.maze[i][j] = '.';
                }
            }
        }
        this.maze[this.playerPosition.y][this.playerPosition.x] = 'S';
        this.maze[this.endPosition.y][this.endPosition.x] = 'E';
    }

    printMaze() {
        for (let i = 0; i < 7; i++) {
            let row = '';
            for (let j = 0; j < 7; j++) {
                row += this.maze[i][j] + ' ';
            }
            console.log(row);
        }
    }

    move(direction) {
        this.maze[this.playerPosition.y][this.playerPosition.x] = '.';
        if (direction === 'up') {
            this.playerPosition.y--;
        } else if (direction === 'down') {
            this.playerPosition.y++;
        } else if (direction === 'left') {
            this.playerPosition.x--;
        } else if (direction === 'right') {
            this.playerPosition.x++;
        }
        this.maze[this.playerPosition.y][this.playerPosition.x] = 'S';
    }

    checkWin() {
        return this.playerPosition.x === this.endPosition.x && this.playerPosition.y === this.endPosition.y;
    }

    start() {
        while (!this.checkWin()) {
            this.printMaze();
            const direction = readlineSync.question('Enter a direction (up, down, left, right): ');
            this.move(direction);
        }
        console.log('You won!');
    }
}

const game = new Game();
game.start();