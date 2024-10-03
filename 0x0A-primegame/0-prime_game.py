#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    """
    if x <= 0:
        return None

    if nums is None:
        return None

    if x != len(nums):
        return None

    ben, maria = 0, 0

    z = [1 for x in range(sorted(nums)[-1] + 1)]
    z[0], z[1] = 0, 0
    for j in range(2, len(z)):
        multy(z, j)

    for i in nums:
        if sum(z[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def multy(arr, x):
    """ Removes multiples of a prime number from arr """
    for i in range(2, len(arr)):
        try:
            arr[i * x] = 0
        except (ValueError, IndexError):
            break
