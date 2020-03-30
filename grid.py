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


def grid_size(screen: turtle._Screen, block_size: int):
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
    t.forward(N*LENGTH)
    t.left(180)
    screen.update()


if __name__ == '__main__':
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed('fastest')

    LENGTH = 10  # each grid element will be LENGTH x LENGTH pixels
    N = grid_size(screen, LENGTH)  # N by N grid

    # center the grid
    t.penup()
    t.goto(-N * LENGTH/2, -N * LENGTH/2)
    t.pendown()

    grid(t, N, LENGTH, screen)

    screen.exitonclick()
