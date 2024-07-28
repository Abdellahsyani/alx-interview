#!/usr/bin/python3
'''draw the pascal triangle'''


def pascal_triangle(n):
    '''function to create the triangle'''
    the_list = []
    if type(n) is not int or n <= 0:
        return the_list
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(the_list[i-1][j-1] + the_list[i-1][j])
            row.append(1)
        the_list.append(row)
    return the_list
