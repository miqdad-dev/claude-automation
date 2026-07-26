class Robot:
    def __init__(self):
        self.position = (0, 0)

    def move(self, direction):
        x, y = self.position
        if direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
        self.position = (x, y)
        print(f"Position: {self.position}")


if __name__ == "__main__":
    robot = Robot()
    while True:
        command = input()
        robot.move(command)