import turtle
from time import sleep


class Graphics:
    def __init__(self, block_size: int, grid_size: int = None):
        self.screen = turtle.Screen()
        self.turtle = turtle.Turtle()
        self.turtle.speed('fastest')
        self.turtle.ht()

        self.block_size = block_size
        if grid_size:
            self.grid_size = grid_size
        else:
            self.grid_size = self.get_grid_size()

        self.origin = self.draw_grid()

    @staticmethod
    def closest_number(n: int, m: int):
        q = n // m
        n1 = m * q

        if(n * m) > 0:
            n2 = (m * (q + 1))
        else:
            n2 = (m * (q - 1))

        if abs(n - n1) < abs(n - n2):
            return n1

        return n2

    def get_grid_size(self):
        min_dim = min(self.screen.window_width(), self.screen.window_height())
        return (self.closest_number(min_dim, self.block_size) // self.block_size) - 5

    def draw_grid(self):
        self.screen.tracer(0, 0)
        self.turtle.penup()
        self.turtle.goto(-self.grid_size * self.block_size / 2, -self.grid_size * self.block_size / 2)
        self.turtle.pendown()
        sign = 1
        for _ in range(2):

            for _ in range(self.grid_size):
                self.turtle.forward(self.block_size * self.grid_size)
                self.turtle.left(sign * 90)
                self.turtle.forward(self.block_size)
                self.turtle.left(sign * 90)
                sign = 0 - sign

            self.turtle.forward(self.block_size * self.grid_size)
            [self.turtle.right, self.turtle.left][self.grid_size % 2](90)
            sign = 0 - sign

        # go to the upper left corner
        self.turtle.forward(self.grid_size*self.block_size)
        self.turtle.left(180)
        self.screen.update()

        return self.turtle.position()

    def render_cells(self, cells):
        self.screen.tracer(0, 0)
        for cell in cells:
            self.turtle.penup()
            self.turtle.goto(cell)
            self.turtle.pendown()
            self.turtle.seth(0)
            self.live_cell()
        self.screen.update()
        sleep(0.1)

    def live_cell(self, edge_size: int = 10):
        self.turtle.begin_fill()
        for i in range(7):
            self.turtle.fd(edge_size) if i % 2 == 0 else self.turtle.rt(90)
        self.turtle.end_fill()
