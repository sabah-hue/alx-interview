#!/usr/bin/python3
"""a method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """lockboxes method"""
    n = len(boxes)
    if n == 0:
        return False
    unlocked = {0}
    queue = [boxes[0]]  # init queue
    while queue:
        box = queue.pop(0)
        for key in box:
            if key not in unlocked and key < n:
                # box unlocked
                unlocked.add(key)
                queue.append(boxes[key])
    return len(unlocked) == n
