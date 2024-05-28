import sys
sys.path.append('/home/runner/work/hash_sequence/hash_sequence/lib/')

import hashlib
import hash_seqeunce

seq = 'ACGT'

def test_answer():
    # hash ACGT
    assert hash_sequence.hash_seqeunce(seq) == '46054055969511637'
    # format md5 hash of ACGT
    md5_seq = hashlib.md5(seq.encode("utf-8")).hexdigest()
    assert hash_sequence.reduceMd5(md5_seq, 56) == 46054055969511637
    # hash ACGT*100
    long_seq = 'ACGT' * 100
    assert hash_sequence.hash_seqeunce(long_seq) == '53658030375034075'
    # format md5 hash of ACGT*100
    md5_long_seq = hashlib.md5(long_seq.encode("utf-8")).hexdigest()
    assert hash_sequence.reduceMd5(md5_long_seq, 56) == 53658030375034075
