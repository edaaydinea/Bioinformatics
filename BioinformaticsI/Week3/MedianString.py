def hamming_distance(p, q):
    """Calculate the Hamming distance between two strings p and q."""
    return sum(pi != qi for pi, qi in zip(p, q))

def d(pattern, dna_strings):
    """Calculate the distance of a pattern to a set of DNA strings."""
    k = len(pattern)
    total_distance = 0
    for dna in dna_strings:
        min_distance = float('inf')
        for i in range(len(dna) - k + 1):
            substring = dna[i:i+k]
            min_distance = min(min_distance, hamming_distance(pattern, substring))
        total_distance += min_distance
    return total_distance

def generate_kmers(k):
    """Generate all possible k-mers of length k."""
    from itertools import product
    nucleotides = 'ACGT'
    return [''.join(kmer) for kmer in product(nucleotides, repeat=k)]

def MedianString(k, dna_strings):
    """Find the k-mer that minimizes d(Pattern, Dna)."""
    kmers = generate_kmers(k)
    best_kmer = None
    min_distance = float('inf')
    for kmer in kmers:
        current_distance = d(kmer, dna_strings)
        if current_distance < min_distance:
            min_distance = current_distance
            best_kmer = kmer
    return best_kmer

def read_input(file_path):
    """Read input data from a file and parse it."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        k = int(lines[0].strip())
        dna_strings = lines[1].strip().split()
    return k, dna_strings

# File path
file_path = 'dataset_30304_9.txt'

# Read the input
k, dna_strings = read_input(file_path)

# Function Call
result = MedianString(k, dna_strings)
print(result)
