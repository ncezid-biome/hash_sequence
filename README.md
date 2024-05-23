# hash_sequence

A Rosetta Stone for getting hashsums

## Contents

This is a repo to have examples on how to make hashsums for each language.

Functions:

* `hash_sequence`: convert a string into a reduced hash
* `reduceMd5`: transform an md5sum into a reduced hash

## Usage

Python

```python
import hash_sequence

seq  = "ACTG"
hash = hash_sequence(seq)
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
