#!/usr/bin/python3
"""module to etablish perimeter of island"""


def island_perimeter(grid):
    """fonction to do it"""

    perimeter = 0
    rows = len(grid)
    if rows > 0:
        col = len(grid[0])
    else:
        col = 0

    for i in range(rows):
        for j in range(col):
            if grid[i][j] == 1:
                perimeter += 4
            if i > 0 and grid[i - 1][j] == 1:
                perimeter -= 2
            if j > 0 and grid[i][j - 1] == 1:
                perimeter -= 2

    return (perimeter)
