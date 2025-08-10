# compressor.py
# Handles compression and decompression for alphabets and numbers

ALPHA_MAP = {chr(ord('a') + i): i for i in range(26)}
#NUM_MAP = {str(i): i for i in range(10)}

ALPHA_FLAG = chr(102)  # 'f' in ASCII
NUM_FLAG = chr(101)    # 'e' in ASCII


def chars_to_dec(data, character_map):
    """Convert string to a decimal integer using given mapping."""
    data += 'b'  # sentinel
    number = 0
    base = len(character_map)
    for character in data[::-1]:
        number = number * base + character_map[character]
    return number


def comp(number):
    """Compress an integer into a string with base-100 encoding."""
    number = int(number)
    compressed_data = ''
    while number:
        compressed_data += chr(number % 100)  # only first 99 chars
        number //= 100
    return compressed_data


def decomp(compressed_data):
    """Decompress base-100 encoded string back to integer."""
    number = 0
    for character in compressed_data[::-1]:
        number = number * 100 + ord(character)
    return number


def dec_to_chars(number, character_map):
    """Convert integer back to string using given mapping."""
    reversed_character_map = {v: k for k, v in character_map.items()}
    data = ''
    base = len(character_map)
    while number:
        data += reversed_character_map[number % base]
        number //= base
    return data[::-1][1:][::-1]  # remove sentinel


def compress_data(data, mode="alpha"):
    """
    Compress data and add mode flag.
    mode = "alpha" or "num"
    """
    if mode == "alpha":
        if not data.isalpha():
            raise ValueError("Alphabet mode only accepts letters a-z.")
        flag = ALPHA_FLAG
        mapping = ALPHA_MAP
        compressed = comp(chars_to_dec(data, mapping))
    elif mode == "num":
        if not data.isdigit():
            raise ValueError("Number mode only accepts digits 0-9.")
        flag = NUM_FLAG
        compressed = comp(data)
    else:
        raise ValueError("Invalid mode. Use 'alpha' or 'num'.")

    return flag + compressed


def decompress_data(data):
    """Decompress data based on its mode flag."""
    flag = data[0]
    payload = data[1:]

    if flag == ALPHA_FLAG:
        mapping = ALPHA_MAP
        number = decomp(payload)
        return dec_to_chars(number, mapping)
    elif flag == NUM_FLAG:
        number = decomp(payload)
        print(len(str(number)))
        return number
    else:
        raise ValueError("Unknown compression flag in data.")
