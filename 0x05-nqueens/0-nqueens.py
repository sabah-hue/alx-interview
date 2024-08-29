#!/usr/bin/python3
""" N queens puzzle """
import sys
import random


def back(row, n, cols, pos, neg, board):
    """ track queens solutions """
    if row == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for col in range(n):
        if col in cols or (row + col) in pos or (row - col) in neg:
            continue

        cols.add(col)
        pos.add(row + col)
        neg.add(row - col)
        board[row][col] = 1

        back(row + 1, n, cols, pos, neg, board)

        cols.remove(col)
        pos.remove(row + col)
        neg.remove(row - col)
        board[row][col] = 0


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

colums = set()
pos = set()
neg = set()
row = 0
board = [[0] * n for i in range(n)]
back(row, n, colums, pos, neg, board)
