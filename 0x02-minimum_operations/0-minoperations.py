#!/usr/bin/python3
'''start finding the maximum iteration'''


def minOperations(n):
    '''return the number of iteration to get the n'''
    if n <= 1:
        return 0

    operations = 0
    current_length = 1  # Start with one 'H'
    clipboard = 0       # Start with an empty clipboard

    while current_length < n:
        # Find the largest factor of the remaining length needed
        for i in range(n // 2, 0, -1):
            if (n - current_length) % i == 0:
                # Copy the current length if it's a factor
                clipboard = current_length
                operations += 1  # Copy All operation
                break

        # Calculate how many times we need to paste to reach the next multiple
        paste_count = (n - current_length) // clipboard
        current_length += clipboard * paste_count
        operations += paste_count  # Paste operations

    return operations
