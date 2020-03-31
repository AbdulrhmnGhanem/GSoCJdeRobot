from functools import partial

import numpy as np

import graphics
import rules


g = graphics.Graphics(10)
pos_relative_origin = partial(rules.pos_relative_origin, g.origin)

world = np.random.randint(0, 2, (g.grid_size, g.grid_size))
gens = rules.generations(world)


# game loop
while True:
    # reset for new iteration
    g.turtle.reset()

    # get the next generation
    gen = next(gens)
    ones = rules.find_ones(gen)
    live_cells_indices = np.fliplr((ones * g.block_size)[0])
    live_cells_pos = np.apply_along_axis(pos_relative_origin,
                                         1, live_cells_indices)
    # rendering
    g.draw_grid()
    g.render_cells(live_cells_pos)
