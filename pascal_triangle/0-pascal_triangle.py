#!/usr/bin/python3
"""Module qui affiche un triangle de Pascal"""


def pascal_triangle(n):
    """Algo pour le triangle de Pascale"""
    row = []
    if n <= 0:
        return row
    elif n <= 2:
        row.append([1])
        row.append([1, 1])
    else:
        row.append([1])
        row.append([1, 1])
        prevlist = 1
        while n-2 != 0:
            index = 0 
            new_row = []
            new_row.append(1)
            for _ in row[prevlist]:
                try:
                    new_row.append(row[prevlist][index]+ row[prevlist][index+1])
                except IndexError:
                    pass
                index += 1
            new_row.append(1)
            row.append(new_row)
            prevlist += 1
            n -= 1
        return row