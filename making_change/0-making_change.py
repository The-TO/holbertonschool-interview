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

    dp = [total + 1] *(total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i-coin] + 1)

    if dp[total] == total +1:
        return -1
    
    return dp[total]
