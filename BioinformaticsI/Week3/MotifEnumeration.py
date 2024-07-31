"""
Implanted Motif Problem: Find all (k, d)-motifs in a collection of strings.
- Input: A collection of strings Dna, and integers k and d.
- Output: All (k, d)-motifs in Dna.

MotifEnumeration(Dna, k, d)
    Patterns ← an empty set
    for each k-mer Pattern in the first string in Dna
        for each k-mer Pattern’ differing from Pattern by at most d mismatches
            if Pattern' appears in each string from Dna with at most d mismatches
                add Pattern' to Patterns
    remove duplicates from Patterns
    return Patterns
    
Sample Input:
    3 1
    ATTTGGC TGCCTTA CGGTATC GAAAATT
    
Sample Output:
    ATA ATT GTT TTT
"""

from itertools import product

def hamming_distance(p, q):
    """Calculate the Hamming distance between two strings p and q."""
    return sum(pi != qi for pi, qi in zip(p, q))

def neighbors(pattern, d):
    """Generate all neighbors of a pattern with at most d mismatches."""
    nucleotides = 'ACGT'
    if d == 0:
        yield pattern
    else:
        for i in range(len(pattern)):
            for x in nucleotides:
                if x != pattern[i]:
                    for suffix in neighbors(pattern[i+1:], d-1):
                        yield pattern[:i] + x + suffix

def is_motif(pattern, dna_strings, d):
    """Check if a pattern is a motif in all strings with at most d mismatches."""
    k = len(pattern)
    for dna in dna_strings:
        found = False
        for i in range(len(dna) - k + 1):
            if hamming_distance(pattern, dna[i:i+k]) <= d:
                found = True
                break
        if not found:
            return False
    return True

def MotifEnumeration(dna_strings, k, d):
    patterns = set()
    for dna in dna_strings:
        for i in range(len(dna) - k + 1):
            kmer = dna[i:i+k]
            for neighbor in neighbors(kmer, d):
                if is_motif(neighbor, dna_strings, d):
                    patterns.add(neighbor)
    
    return sorted(patterns)

def read_input(file_path):
    """Read input data from a file and parse it."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        k, d = map(int, lines[0].strip().split())
        dna_strings = lines[1].strip().split()
    return k, d, dna_strings

# File path
file_path = 'dataset_30302_8.txt'

# Read the input
k, d, dna_strings = read_input(file_path)

# Function Call
result = MotifEnumeration(dna_strings, k, d)
print(" ".join(result))

