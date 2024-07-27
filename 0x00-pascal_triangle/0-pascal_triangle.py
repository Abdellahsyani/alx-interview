#!/usr/bin/python3
"""draw the pascal triangle"""

def pascal_triangle(n):
    the_list = []
    if n <= 0:
        return the_list
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(the_list[i-1][j-1] + the_list[i-1][j])
            row.append(1)
        the_list.append(row)
    for row in the_list:
        print(row)
