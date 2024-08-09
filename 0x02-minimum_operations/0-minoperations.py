#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method
that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""
import math  # Import the math module


def minOperations(n):
    """ calc fewest number of operations needed to result n H characters"""
    operations = 0
    div = 2
    if n < div:
        return operations
    while n >= div:
        if n % div == 0:
            operations += div
            n = n / div
            div = div - 1
        div = div + 1
    return operations
