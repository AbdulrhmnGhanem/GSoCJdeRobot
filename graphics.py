import turtle


screen = turtle.getscreen()
t = turtle.Turtle()
t.ht()
t.speed(1000)


def dead_cell(edge_size=10):
    for i in range(7):
        t.fd(edge_size) if i % 2 == 0 else t.rt(90)


def live_cell(edge_size=10):
    t.begin_fill()
    dead_cell(edge_size)
    t.end_fill()
