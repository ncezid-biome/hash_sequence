# hash_sequence

A Rosetta Stone for getting hashsums

## Contents

This is a repo to have examples on how to make hashsums for each language.

Functions:

* `hash_sequence`: convert a string into a reduced hash
* `reduceMd5`: transform an md5sum into a reduced hash

## Usage

Python

with hash_sequence.py in your working dir

```python
import hash_sequence

# convert seqeunce to PN2.0 hash
seq  = "ACTG"
hash = hash_sequence.hash_seqeunce(seq)

# convert md5 hash to PN2.0 hash
md5 = 'f1f8f4bf413b16ad135722aa4591043e'
hash = hash_seqeunce.reduceMd5(md5, 56)
```

```bash
$ python hash_sequence.py -i ACGT
46054055969511637

$ python hash_sequence.py -m f1f8f4bf413b16ad135722aa4591043e
46054055969511637
```

Perl

```perl
use hash_sequence qw/hash_sequence/;

$seq  = "ACTG";
$hash = hash_sequence($seq);
```


## FAQ

### Can I transform a hash back to the string?

No, hashing is a one-way algorithm.
There are brute-force methods such as [hash2seq](https://github.com/lskatz/hash2seq), but it is a computationally intensive method.

### Are you worried about hash collisions with different alleles?

Formally this is possible but with md5sum itself, we have not observed collisions.
See here for a small experiment: <https://github.com/lskatz/mlst-hash-template/issues/16>.
