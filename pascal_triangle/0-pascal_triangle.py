#!/usr/bin/python3

def pascal_triangle(n):
    row = [i]
    new_row = []
    for i in range(len(new_row)):
        if i == 0:
            new_row[i] = 1
        elif i == len(new_row)-1:
            new_row[i] =1
        else:
            new_row[i] = row[i] + row[i-1]