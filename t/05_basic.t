#!/usr/bin/env perl
use strict;
use warnings;
use Test::More tests => 3;
use FindBin qw/$RealBin/;
use lib "$RealBin/../lib";

use Digest::MD5 qw(md5_hex);

use_ok("hash_sequence");
use hash_sequence qw/hash_sequence reduceMd5/;

my $seq     = "ACGT";
my $longseq = $seq x 100;

subtest 'hash short sequence' => sub {
    is( hash_sequence($seq),     46054055969511637,     "hash_sequence" );
    
    my $hex = md5_hex($seq);
    is( reduceMd5($hex, 56), 46054055969511637, "reduceMd5" );
};

subtest 'hash long sequence' => sub {
    is( hash_sequence($longseq),     53658030375034075,     "hash_sequence" );
    
    my $hex = md5_hex($longseq);
    is( reduceMd5($hex, 56), 53658030375034075, "reduceMd5" );
};
