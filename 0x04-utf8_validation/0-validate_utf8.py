#!/usr/bin/python3
'''the utf-8 validation check for valid data'''


def validUTF8(data):
    # Number of bytes left to process in the current UTF-8 character
    bytes_to_process = 0

    for num in data:
        # Get only the last 8 bits of the number
        byte = num & 0xFF

        if bytes_to_process == 0:
            # Determine how many bytes the character should have
            if (byte >> 5) == 0b110:  # 110xxxxx -> 2-byte character
                bytes_to_process = 1
            elif (byte >> 4) == 0b1110:  # 1110xxxx -> 3-byte character
                bytes_to_process = 2
            elif (byte >> 3) == 0b11110:  # 11110xxx -> 4-byte character
                bytes_to_process = 3
            elif (byte >> 7) == 0b0:  # 0xxxxxxx -> 1-byte character (ASCII)
                continue
            else:
                return False
        else:
            # For continuation bytes, check if they start with 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            bytes_to_process -= 1

    # If all bytes have been correctly processed, bytes_to_process should be 0
    return bytes_to_process == 0
