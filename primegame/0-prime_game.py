#!/usr/bin/python3
"""Prime Game: find out who wins the most rounds between Maria and Ben."""


def isWinner(x, nums):
    """Return the name of the player who won the most rounds.

    Each move removes exactly one prime number from the set, so a round
    lasts as many turns as there are primes between 1 and n.
    Maria plays first: she wins when that count is odd, Ben when it is even.

    Args:
        x (int): number of rounds.
        nums (list): value of n for each round.

    Returns:
        str: "Maria" or "Ben", or None if there is no winner.
    """
    if x is None or nums is None or x < 1 or len(nums) == 0:
        return None

    rounds = nums[:x]
    max_n = max(rounds)
    if max_n < 1:
        max_n = 1

    # Sieve of Eratosthenes, computed once up to the biggest n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = False
    is_prime[1] = False
    i = 2
    while i * i <= max_n:
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False
        i += 1

    # prime_count[k] = number of primes between 1 and k
    prime_count = [0] * (max_n + 1)
    for k in range(1, max_n + 1):
        prime_count[k] = prime_count[k - 1]
        if is_prime[k]:
            prime_count[k] += 1

    maria = 0
    ben = 0
    for n in rounds:
        if n > 0 and prime_count[n] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
