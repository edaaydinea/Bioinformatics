def hamming_distance(s1, s2):
    """Calculate the Hamming distance between two strings of equal length."""
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def distance_between_pattern_and_strings(pattern, dna):
    """Compute the distance between a pattern and a collection of strings in DNA."""
    k = len(pattern)
    total_distance = 0
    
    for text in dna:
        min_distance = float('inf')
        # Check all k-mers in the text
        for i in range(len(text) - k + 1):
            kmer = text[i:i+k]
            dist = hamming_distance(pattern, kmer)
            if dist < min_distance:
                min_distance = dist
        total_distance += min_distance
    
    return total_distance

def read_input(file_path):
    """Read input data from a file and parse it."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        pattern = lines[0].strip()
        dna = lines[1].strip().split()
    return pattern, dna

# File path
file_path = 'dataset_30312_1.txt'

# Read the input
pattern, dna = read_input(file_path)

# Function Call
result = distance_between_pattern_and_strings(pattern, dna)
print(result)
