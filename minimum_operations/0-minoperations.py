#!/usr/bin/python3
"""Module qui affiche un minimum d'opération pour réaliser une tache"""

def minOperations(n):
    if n <= 1:
        return 0

    total_operations = 0

    divisor = 2

    while n > 1:
        if n % divisor == 0:
            total_operations += divisor
            n //= divisor
        else:
            divisor += 1

    return total_operations
