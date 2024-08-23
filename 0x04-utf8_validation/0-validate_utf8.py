#!/usr/bin/python3
'''the utf-8 validation check for valid data'''


def validUTF8(data):
    # Number of bytes to process for the current character
    bytes_to_process = 0

    # Masks to check the first byte
    mask1 = 1 << 7   # 10000000
    mask2 = 1 << 6   # 01000000

    for num in data:
        # Mask out the first 8 bits
        byte = num & 0xFF

        if bytes_to_process == 0:
            # Determine how many bytes this character should have
            if byte & mask1 == 0:
                # 1-byte character (starts with 0xxxxxxx)
                continue
            elif byte & mask1 and byte & mask2 == 0:
                # Invalid pattern (starts with 10xxxxxx)
                return False
            elif byte & (mask1 >> 1) == mask1:
                bytes_to_process = 3
            elif byte & (mask1 >> 2) == mask1 >> 1:
                bytes_to_process = 2
            elif byte & (mask1 >> 3) == mask1 >> 2:
                bytes_to_process = 1
            else:
                return False
        else:
            # Check that the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False
            bytes_to_process -= 1

    # If we have processed all bytes correctly, bytes_to_process should be 0
    return bytes_to_process == 0
