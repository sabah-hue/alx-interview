#!/usr/bin/python3
""" N queens puzzle """
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
for i in range(n - 2):
    x = []
    for j in range(n):
        if j == 0:
            z = i + 1
        elif j == n - 1:
            z = n - 2 - i
        elif j > i:
            z = j - i
        else:
            z = i - j
        x.append([j, z])
    print(f"{x}")
