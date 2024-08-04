#!/usr/bin/python3
'''check locked and opened boxes'''


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes: A list of lists, which list contains keys to other boxes.
    Returns;
        True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # First box is unlocked

    def dfs(box_index):
        for key in boxes[box_index]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                dfs(key)
    dfs(0)
    return all(visited)
