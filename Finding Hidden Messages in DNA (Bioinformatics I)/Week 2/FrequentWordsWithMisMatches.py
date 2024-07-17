from collections import defaultdict

def hamming_distance(s1, s2):
    # Calculate Hamming distance between two strings of equal length
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance

def generate_kmer_neighbors(kmer, d):
    # Generate all neighbors of a k-mer with up to d mismatches
    if d == 0:
        return {kmer}
    if len(kmer) == 1:
        return {'A', 'C', 'G', 'T'}
    
    neighborhood = set()
    suffix_neighbors = generate_kmer_neighbors(kmer[1:], d)
    for neighbor in suffix_neighbors:
        if hamming_distance(kmer[1:], neighbor) < d:
            for nucleotide in ['A', 'C', 'G', 'T']:
                neighborhood.add(nucleotide + neighbor)
        else:
            neighborhood.add(kmer[0] + neighbor)
    
    return neighborhood

def frequent_words_with_mismatches(text, k, d):
    frequent_patterns = []
    frequency_array = defaultdict(int)
    n = len(text)

    # Count frequencies of all k-mers and their neighbors with up to d mismatches
    for i in range(n - k + 1):
        kmer = text[i:i + k]
        neighbors = generate_kmer_neighbors(kmer, d)
        for neighbor in neighbors:
            frequency_array[neighbor] += 1
    
    max_count = max(frequency_array.values())

    # Collect all k-mers with maximum frequency
    frequent_patterns = [kmer for kmer, count in frequency_array.items() if count == max_count]

    return frequent_patterns

# Function to read inputs from a text file
def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    text = lines[0].strip()
    k, d = map(int, lines[1].strip().split())
    return text, k, d

# Example usage:
file_path = 'dataset_30278_9.txt'  # Replace with your file path
text, k, d = read_input_from_file(file_path)
result = frequent_words_with_mismatches(text, k, d)
print(result)
