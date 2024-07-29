#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    pascal = []
    if n <= 0:
        return []

    for i in range(n):
        inner = []
        if i == 0:
            inner.append(1)
        else:
            for j in range(i + 1):
                if j == 0 or j == i:
                    inner.append(1)
                else:
                    element = pascal[i - 1][j] + pascal[i - 1][j - 1]
                    inner.append(element)
        pascal.append(inner)
    return pascal
