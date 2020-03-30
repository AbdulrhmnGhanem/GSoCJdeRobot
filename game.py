import numpy as np

from graphics import grid_size


def count_neighbors(world):
    neighbors = np.zeros(world.shape, dtype=int)

    neighbors[1:] += world[:-1]           # N
    neighbors[:-1] += world[1:]           # S
    neighbors[:, 1:] += world[:, :-1]     # W
    neighbors[:, :-1] += world[:, 1:]     # E
    neighbors[1:, 1:] += world[:-1, :-1]  # NW
    neighbors[1:, :-1] += world[:-1, 1:]  # NE
    neighbors[:-1, 1:] += world[1:, :-1]  # SW
    neighbors[:-1, :-1] += world[1:, 1:]  # SE
    return neighbors


def generations(world):
    while True:
        neighbors = count_neighbors(world)

        world &= (neighbors == 2)
        world |= (neighbors == 3)

        yield world


if __name__ == "__main__":
    world = np.random.randint(0, 2, (grid_size, grid_size))
    gen = generations(world)
