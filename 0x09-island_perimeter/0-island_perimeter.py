#!/usr/bin/python3


def island_perimeter(grid):
    """count the space of the island
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (grid[row][col] == 1):
                if (grid[row][col - 1] == 0):
                    perimeter += 1
                if (grid[row - 1][col] == 0):
                    perimeter += 1
                if (grid[row][col + 1] == 0):
                    perimeter += 1
                if (grid[row + 1][col] == 0):
                    perimeter += 1
    return (perimeter)
