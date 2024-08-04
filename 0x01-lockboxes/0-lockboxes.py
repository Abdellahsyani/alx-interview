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
    queue = [0]  # Initialize a queue with the initial unlocked box

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
