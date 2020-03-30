import turtle


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


if __name__ == '__main__':
    screen = turtle.getscreen()
    t = turtle.Turtle()
    t.ht()
    t.speed(10)
    change_pos(screen)
    live_cell()
