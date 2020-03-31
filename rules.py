import numpy as np


def count_neighbors(world):
    """
    count the neighbors for each cell, for edge cells the circulation isn't assumed
    :param world: ndarry
    :return: ndarry of number of neighbors for each cell
    """
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
    """
    A generator for each generation of the game
    :param world: ndarry
    :return: ndarry: next generation
    """
    while True:
        neighbors = count_neighbors(world)

        world &= (neighbors == 2)
        world |= (neighbors == 3)

        yield world


def find_ones(world):
    """
    find the indices of live cells, represented as ones
    :param world:
    :return:
    """
    return np.dstack(np.where(world == 1))


def pos_relative_origin(origin: [int, int], point: [int, int]):
    """
    Get the relative position of a point from the origin of the grid.
    Grid origin is the top left corner
    :param origin: coordinates of grid origin
    :param point: coordinates of the point
    :return:
    """
    return origin[0] + point[0], origin[1] - point[1]


if __name__ == "__main__":
    pass
