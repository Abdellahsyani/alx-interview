#!/usr/bin/python3
'''start finding the maximum iteration'''


def minOperations(n):
    '''return the max of operation that we do to get the n'''
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Factorize the number n
    while n > 1:
        while n % divisor == 0:
            # For each factor, add the factor value to the operations
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
