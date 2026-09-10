#!/usr/bin/python3
"""Module qui affiche un triangle de Pascal"""


def pascal_triangle(n):
    """Algo pour le triangle de Pascale"""
    row = []
    if n <= 0:
        return row
    elif n == 1:
        row.append([1])
        return row
    elif n == 2:
        row.append([1])
        row.append([1, 1])
        return row

    else:
        row.append([1])
        row.append([1, 1])
        pvlt = 1
        while n-2 != 0:
            index = 0
            new_row = []
            new_row.append(1)
            for _ in row[pvlt]:
                try:
                    new_row.append(row[pvlt][index] + row[pvlt][index + 1])
                except IndexError:
                    pass
                index += 1
            new_row.append(1)
            row.append(new_row)
            pvlt += 1
            n -= 1
        return row
