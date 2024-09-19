#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins, total):
    """
    determine the fewest number of coins
    needed to meet a given i total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    equal = 0
    num = 0

    for i in coins:
        while equal < total:
            equal += i
            num += 1
        if equal == total:
            return num
        equal = equal - i
        num = num - 1
    return -1
