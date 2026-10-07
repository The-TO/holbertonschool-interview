#!/usr/bin/python3
"""Module pour verifier l'necodage utf-8"""


def count_ones_left(n):
    """permet de compter les 1"""
    count = 0
    for i in range(7, -1, -1):
        if n & (1 << i):
            count += 1
        else:
            break
    return count


def validUTF8(data):
    """fonction mermettant la verif"""
    remaining = 0

    for d in data:
        if not remaining:
            remaining = count_ones_left(d)
            if remaining == 0:
                continue
            elif remaining ==1 or remaining > 4:
                return False
        else:
            if count_ones_left(d) != 1:
                return False
        remaining -= 1
    return remaining == 0