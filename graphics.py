import turtle
from time import sleep

from configuration import grid_size, block_size


class Graphics:
    def __init__(self):
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
    def closest_number(num: int, divider: int):
        """
        Get the closets number divisible by a divider
        """
        q = num // divider
        n1 = divider * q

        if(num * divider) > 0:
            n2 = (divider * (q + 1))
        else:
            n2 = (divider * (q - 1))

        if abs(num - n1) < abs(num - n2):
            return n1

        return n2

    def get_grid_size(self):
        """
        calculate the size of grid based on the screen DIMs
        :return: dimensions of the gird
        """
        min_dim = min(self.screen.window_width(), self.screen.window_height())
        return (self.closest_number(min_dim, self.block_size) // self.block_size) - 5

    def draw_grid(self):
        """
        :return: the grid origin
        """
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
        """
        render the live cells for a world
        :param cells: indices for live cells
        """
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
        """
        draw a live cell
        :param edge_size: cell edge size
        :return:
        """
        self.turtle.begin_fill()
        for i in range(7):
            self.turtle.fd(edge_size) if i % 2 == 0 else self.turtle.rt(90)
        self.turtle.end_fill()
