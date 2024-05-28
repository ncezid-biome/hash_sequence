import importlib.util
import sys
spec = importlib.util.spec_from_file_location("hash_sequence", "/home/runner/work/hash_sequence/hash_sequence/lib/hash_sequence.py")
hash_sequence = importlib.util.module_from_spec(spec)
sys.modules["hash_sequence"] = hash_sequence
spec.loader.exec_module(hash_sequence)

import hashlib

seq = 'ACGT'

def test_answer():
    # hash ACGT
    assert hash_sequence.hash_sequence(seq) == '46054055969511637'
    # format md5 hash of ACGT
    md5_seq = hashlib.md5(seq.encode("utf-8")).hexdigest()
    assert hash_sequence.reduceMd5(md5_seq, 56) == 46054055969511637
    # hash ACGT*100
    long_seq = 'ACGT' * 100
    assert hash_sequence.hash_sequence(long_seq) == '53658030375034075'
    # format md5 hash of ACGT*100
    md5_long_seq = hashlib.md5(long_seq.encode("utf-8")).hexdigest()
    assert hash_sequence.reduceMd5(md5_long_seq, 56) == 53658030375034075
