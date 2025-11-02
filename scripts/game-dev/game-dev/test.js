const chai = require('chai');
const Game = require('./game');
const expect = chai.expect;

describe('Game', () => {
  it('should generate a 7x7 maze', () => {
    const game = new Game();
    expect(game.maze.length).to.equal(7);
    expect(game.maze[0].length).to.equal(7);
  });

  it('should start the player at position (1, 1)', () => {
    const game = new Game();
    expect(game.playerPosition.x).to.equal(1);
    expect(game.playerPosition.y).to.equal(1);
  });

  it('should set the end position at (5, 5)', () => {
    const game = new Game();
    expect(game.endPosition.x).to.equal(5);
    expect(game.endPosition.y).to.equal(5);
  });
});