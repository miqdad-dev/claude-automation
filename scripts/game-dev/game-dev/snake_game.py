import curses
import random
from collections import deque

class SnakeGame:
    def __init__(self, screen):
        self.screen = screen
        self.width = 20
        self.height = 10
        self.snake = deque([(5, 5)])
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        self.food = self.new_food_location()

    def new_food_location(self):
        while True:
            location = (random.randint(1, self.height), random.randint(1, self.width))
            if location not in self.snake:
                return location

    def update(self):
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        if (new_head in self.snake or
            new_head[0] < 1 or new_head[0] > self.height or
            new_head[1] < 1 or new_head[1] > self.width):
            return False

        self.snake.appendleft(new_head)
        if new_head == self.food:
            self.food = self.new_food_location()
        else:
            self.snake.pop()
        return True

    def draw(self):
        self.screen.clear()
        self.screen.border(0)
        for part in self.snake:
            self.screen.addch(part[0], part[1], '@')
        self.screen.addch(self.food[0], self.food[1], '*')

    def input(self):
        key = self.screen.getch()
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            new_direction = {
                curses.KEY_UP: (-1, 0),
                curses.KEY_DOWN: (1, 0),
                curses.KEY_LEFT: (0, -1),
                curses.KEY_RIGHT: (0, 1)
            }[key]
            if (new_direction[0] != -self.direction[0] and
                new_direction[1] != -self.direction[1]):
                self.direction = new_direction

    def run(self):
        while True:
            self.screen.timeout(100)
            self.input()
            if not self.update():
                break
            self.draw()

def main(stdscr):
    game = SnakeGame(stdscr)
    game.run()

if __name__ == "__main__":
    curses.wrapper(main)