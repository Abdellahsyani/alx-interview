#!/usr/bin/python3


def island_perimeter(grid):
    """count the space of the island
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (grid[row][col] == 1):
                # check the left side of land
                if (col == 0 or grid[row][col - 1] == 0):
                    perimeter += 1
                # check the top side of the land
                if (row == 0 or grid[row - 1][col] == 0):
                    perimeter += 1
                # check the right side of the land
                if (col == len(grid[0]) - 1 or grid[row][col + 1] == 0):
                    perimeter += 1
                # check the buttom side of the land
                if (row == len(grid[0]) - 1 or grid[row + 1][col] == 0):
                    perimeter += 1
    return (perimeter)
