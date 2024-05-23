#!/usr/bin/env perl
package hash_sequence;

use strict;
use warnings;
use Digest::MD5 qw(md5_hex);
use Exporter;
our @ISA = qw(Exporter);
our @EXPORT_OK = qw(hash_sequence reduceMd5);

=pod

=head1 NAME hash_sequence

=head1 SYNOPSIS

    use hash_sequence qw(hash_sequence reduceMd5);
    my $reduced = hash_sequence($sequence);
    my $reduced = reduceMd5($md5, $max_bits_in_result);

=head1 DESCRIPTION

This module provides a function to hash a sequence and a function to reduce a md5 hash to a number.

=head1 FUNCTIONS

=over 4

=item hash_sequence($sequence)

Hashes the given sequence using md5 and reduces the result to a 56 bit hash.

=item reduceMd5($md5, $max_bits_in_result)

Reduces the given md5 hash to a 56 bit hash.

=back

=cut

sub hash_sequence {
    my ($sequence) = @_;

    my $md5 = md5_hex($sequence);
    my $max_bits_in_result = 56;
    my $p = (1 << $max_bits_in_result) - 1;
    my $rest = hex($md5);
    my $result = 0;
    while ($rest != 0) {
        $result = $result ^ ($rest & $p);
        $rest = $rest >> $max_bits_in_result;
    }
    return "$result";
}

sub reduceMd5 {
    my ($md5, $max_bits_in_result) = @_;
    my $p = (1 << $max_bits_in_result) - 1;
    my $rest = hex($md5);
    my $result = 0;
    while ($rest != 0) {
        $result = $result ^ ($rest & $p);
        $rest = $rest >> $max_bits_in_result;
    }
    return $result;
}
