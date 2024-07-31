import numpy as np

# Given motif matrix
motifs = [
    "TCGGGGGTTTTT",
    "CCGGTGACTTAC",
    "ACGGGGATTTTC",
    "TTGGGGACTTTT",
    "AAGGGGACTTCC",
    "TTGGGGACTTCC",
    "TCGGGGATTCAT",
    "TCGGGGATTCCT",
    "TAGGGGAACTAC",
    "TCGGGTATAACC"
]

# Length of motifs and number of motifs
k = len(motifs[0])
num_motifs = len(motifs)

# Initialize entropy total
total_entropy = 0

# Calculate entropy for each column
for col in range(k):
    # Frequency count of each nucleotide
    freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    for motif in motifs:
        nucleotide = motif[col]
        freq[nucleotide] += 1
    
    # Calculate probabilities
    probabilities = [freq[nuc] / num_motifs for nuc in 'ACGT']
    
    # Calculate entropy for this column
    entropy = -sum(p * np.log2(p) for p in probabilities if p > 0)
    
    # Add to total entropy
    total_entropy += entropy

# Print the total entropy accurate to within 0.002
print(f"{total_entropy:.3f}")
