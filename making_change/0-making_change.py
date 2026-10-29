#!/usr/bin/python3
"""
Module 0-making_change.

Détermine le nombre minimum de pièces nécessaires
pour atteindre un montant total donné.
"""


def makeChange(coins, total):
    """
    Calcule le nombre minimum de pièces pour atteindre `total`.

    Args:
        coins (list of int): valeurs des pièces disponibles
            (quantité illimitée de chaque pièce).
        total (int): montant à atteindre.

    Returns:
        int: le nombre minimum de pièces,
             0 si total <= 0,
             -1 si le total ne peut pas être atteint.
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0

    for coin in coins:
        coin_count += total // coin
        total = total % coin
        if total <= 0:
            return coin_count

    return -1
