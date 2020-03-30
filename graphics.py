import turtle


def closest_number(n, m):
    q = n // m
    n1 = m * q

    if((n * m) > 0):
        n2 = (m * (q + 1))
    else:
        n2 = (m * (q - 1))

    if (abs(n - n1) < abs(n - n2)):
        return n1

    return n2


def get_grid_size(screen: turtle._Screen, block_size: int):
    min_dim = min(screen.window_width(), screen.window_height())
    return (closest_number(min_dim, block_size) // block_size) - 5


def grid(turtle: turtle.Turtle, n: int, length: int, screen: turtle._Screen):
    screen.tracer(0, 0)
    sign = 1
    for _ in range(2):

        for _ in range(n):
            turtle.forward(length * n)
            turtle.left(sign * 90)
            turtle.forward(length)
            turtle.left(sign * 90)
            sign = 0 - sign

        turtle.forward(length * n)
        [turtle.right, turtle.left][n % 2](90)
        sign = 0 - sign

    # go to the upper left corner
    t.forward(n*length)
    t.left(180)
    screen.update()


def change_pos(screen: turtle.TurtleScreen):
    x, y = screen.window_width(), screen.window_height()
    t.penup()
    t.setpos(-x/2, y/2)
    t.pendown()


def dead_cell(edge_size: int = 10):
    for i in range(7):
        t.fd(edge_size) if i % 2 == 0 else t.rt(90)


def live_cell(edge_size: int = 10):
    t.begin_fill()
    dead_cell(edge_size)
    t.end_fill()


# main
screen = turtle.Screen()
t = turtle.Turtle()
t.speed('fastest')
t.ht()

LENGTH = 10  # each grid element will be LENGTH x LENGTH pixels
grid_size = get_grid_size(screen, LENGTH)  # grid_size x grid_size grid

if __name__ == '__main__':
    # center the grid
    t.penup()
    t.goto(-grid_size * LENGTH/2, -grid_size * LENGTH/2)
    t.pendown()

    # draw the grid
    grid(t, grid_size, LENGTH, screen)

    live_cell()
    screen.exitonclick()
