from Classes.shape import Shape


class Tetris:
    def __init__(self, height, width):
        self.level = 2
        self.score = 0
        self.state = "start"
        self.field = []
        self.height = 0
        self.width = 0
        self.x = 100
        self.y = 60
        self.zoom = 20
        self.shape = None

        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"

        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        self.shape = Shape(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.shape.image():
                    if i + self.shape.y > self.height - 1 or \
                            j + self.shape.x > self.width - 1 or \
                            j + self.shape.x < 0 or \
                            self.field[i + self.shape.y][j + self.shape.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.shape.y += 1
        self.shape.y -= 1
        self.freeze()

    def go_down(self):
        self.shape.y += 1
        if self.intersects():
            self.shape.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.shape.image():
                    self.field[i + self.shape.y][j + self.shape.x] = self.shape.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def go_side(self, dx):
        old_x = self.shape.x
        self.shape.x += dx
        if self.intersects():
            self.shape.x = old_x

    def rotate(self):
        old_rotation = self.shape.rotation
        self.shape.rotate()
        if self.intersects():
            self.shape.rotation = old_rotation
