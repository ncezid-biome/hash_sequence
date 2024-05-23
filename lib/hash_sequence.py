import hashlib

def hash_sequence(sequence: str) -> str:

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
    p = (1 << max_bits_in_result) - 1
    rest = int(md5, 16)
    result = 0
    while rest != 0:
        result = result ^ (rest & p)
        rest = rest >> max_bits_in_result
    return result