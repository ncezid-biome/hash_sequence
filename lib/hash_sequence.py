import hashlib
import argparse

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
    
    parser = argparse.ArgumentParser(prog='hash_sequence',description='hashes a DNA sequence based on the 56-bit hash used in PN2.0 or formats an md5 hash as an n-bit hash in PN2.0 format')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--input', help='input DNA sequence with no extra chars before or after sequence, ex: ATGCATTG')
    group.add_argument('-l', '--list', help='txt file of input sequences, separated by newline')
    group.add_argument('-m', '--md5', help='an md5 hash, ex: 098f6bcd4621d373cade4e832627b4f6')
    parser.add_argument('-b', '--bits', default=56, type=int, help='number of bits for final hash sequence, can only be used with -m, default: 56')
    parser.add_argument('-o','--output',help='output file, default: STDOUT')


    args = parser.parse_args()

    if args.list:
        out_str = ''
        with open(args.list) as in_file:
            for line in in_file:
                out_str += hash_sequence(line.strip('\n')) + '\n'
    if args.input:
    	out_str = hash_sequence(args.input) + '\n'
    if args.md5 and args.bits:
        out_str = reduceMd5(args.md5, args.bits) + '\n'

    if args.output:
        with open(args.output,'w') as out_file:
            out_file.write(out_str)
    else:
        print(out_str, end='')
