#!/usr/bin/python3
'''the utf-8 validation check for valid data'''


def validUTF8(data):
    """
    Validate if a list of integers represents a valid UTF-8 encoding.
    """
    n = len(data)
    i = 0

    while i < n:
        byte = data[i]
        if byte < 0 or byte > 255:
            return False

        if byte & 0b10000000 == 0:
            i += 1
        elif byte & 0b11100000 == 0b11000000:
            if i + 1 >= n or data[i + 1] & 0b11000000 != 0b10000000:
                return False
            i += 2
        elif byte & 0b11110000 == 0b11100000:
            if i + 2 >= n or not (data[i + 1]
               & 0b11000000 == 0b10000000 and data[i + 2]
               & 0b11000000 == 0b10000000):
                return False
            i += 3
        elif byte & 0b11111000 == 0b11110000:
            if i + 3 >= n or not (data[i + 1] & 0b11000000 == 0b10000000
               and data[i + 2] & 0b11000000 == 0b10000000 and data[i + 3]
               & 0b11000000 == 0b10000000):
                return False
            i += 4
        else:
            return False

    return True
