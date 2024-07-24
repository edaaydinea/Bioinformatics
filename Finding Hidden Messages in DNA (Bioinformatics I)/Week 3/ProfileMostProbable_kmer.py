def calculate_probability(kmer, profile):
    """Calculate the probability of a k-mer given a profile matrix."""
    nucleotides = 'ACGT'
    probability = 1.0
    for i, nucleotide in enumerate(kmer):
        if nucleotide == 'A':
            probability *= profile[0][i]
        elif nucleotide == 'C':
            probability *= profile[1][i]
        elif nucleotide == 'G':
            probability *= profile[2][i]
        elif nucleotide == 'T':
            probability *= profile[3][i]
    return probability

def profile_most_probable_kmer(text, k, profile):
    """Find the Profile-most probable k-mer in the given text."""
    max_probability = -1
    most_probable_kmer = None
    
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = calculate_probability(kmer, profile)
        if prob > max_probability:
            max_probability = prob
            most_probable_kmer = kmer
    
    return most_probable_kmer

def read_input(file_path):
    """Read input data from a file and parse it."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        text = lines[0].strip()
        k = int(lines[1].strip())
        profile = [list(map(float, line.strip().split())) for line in lines[2:]]
    return text, k, profile

# File path
file_path = 'dataset_30305_3.txt'

# Read the input
text, k, profile = read_input(file_path)

# Function Call
result = profile_most_probable_kmer(text, k, profile)
print(result)
