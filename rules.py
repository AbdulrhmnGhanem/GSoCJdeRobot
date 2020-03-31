import numpy as np


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


def find_ones(world):
    return np.dstack(np.where(world == 1))


def pos_relative_origin(origin, cord):
    return origin[0] + cord[0], origin[1] - cord[1]


if __name__ == "__main__":
    pass
