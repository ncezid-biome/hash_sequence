import hashlib

def hash_sequence(sequence: str) -> str:
    """
    Hashes a given sequence using the MD5 algorithm.

    Args:
        sequence (str): The sequence to be hashed.

    Returns:
        str: The hashed result as a string.
    """
    md5 = hashlib.md5(sequence.encode("utf-8"))
    max_bits_in_result = 56
    p = (1 << max_bits_in_result) - 1
    rest = int(md5.hexdigest(), 16)
    result = 0
    while rest != 0:
        result = result ^ (rest & p)
        rest = rest >> max_bits_in_result
    return str(result)

def reduceMd5(md5: str, max_bits_in_result: int) -> int:
    """
    Reduces a given MD5 hash to a specified number of bits.

    Args:
        md5 (str): The MD5 hash to be reduced.
        max_bits_in_result (int): The maximum number of bits in the resulting hash.

    Returns:
        int: The reduced hash as an integer.
    """
    p = (1 << max_bits_in_result) - 1
    rest = int(md5, 16)
    result = 0
    while rest != 0:
        result = result ^ (rest & p)
        rest = rest >> max_bits_in_result
    return result

# Add in some basic test here for main() but it can be elsewhere long term
if __name__ == "__main__":
    print(hash_sequence("ACGT"))
    print(reduceMd5("098f6bcd4621d373cade4e832627b4f6", 56))