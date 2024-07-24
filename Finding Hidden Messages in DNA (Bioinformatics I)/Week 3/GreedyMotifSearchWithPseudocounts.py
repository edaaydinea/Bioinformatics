"""
Implement GreedyMotifSearch with Pseudocounts

- Input: Integers k and t, followed by a collection of strings Dna.
- Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.

Sample Input:
3 5
GGCGTTCAGGCA AAGAATCAGTCA CAAGGAGTTCGC CACGTCAATCAC CAATAATATTCG


Sample Output:
TTC ATC TTC ATC TTC
"""

def calculate_profile(motifs):
    """Calculate the profile matrix from a list of motifs with pseudocounts."""
    k = len(motifs[0])
    t = len(motifs)
    profile = [[0] * k for _ in range(4)]  # Profile matrix for A, C, G, T
    
    # Count occurrences of each nucleotide in each column
    for i in range(k):
        col = [motif[i] for motif in motifs]
        profile[0][i] = (col.count('A') + 1) / (t + 4)  # Add 1 for pseudocount
        profile[1][i] = (col.count('C') + 1) / (t + 4)
        profile[2][i] = (col.count('G') + 1) / (t + 4)
        profile[3][i] = (col.count('T') + 1) / (t + 4)
    
    return profile

def score(motifs):
    """Calculate the score of a set of motifs."""
    profile = calculate_profile(motifs)
    k = len(motifs[0])
    score = 0
    
    for i in range(k):
        column = [motif[i] for motif in motifs]
        max_freq = max([column.count(nuc) / len(motifs) for nuc in 'ACGT'])
        score += len(motifs) - max_freq * len(motifs)
    
    return score

def profile_most_probable_kmer(text, k, profile):
    """Find the Profile-most probable k-mer in the given text."""
    max_prob = -1
    most_probable_kmer = None
    nucleotides = 'ACGT'
    
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = 1.0
        for j, nucleotide in enumerate(kmer):
            if nucleotide == 'A':
                prob *= profile[0][j]
            elif nucleotide == 'C':
                prob *= profile[1][j]
            elif nucleotide == 'G':
                prob *= profile[2][j]
            elif nucleotide == 'T':
                prob *= profile[3][j]
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer
    
    return most_probable_kmer

def greedy_motif_search(dna, k, t):
    """Perform the Greedy Motif Search algorithm with pseudocounts."""
    best_motifs = [text[:k] for text in dna]  # Initial motifs (first k-mer of each string)
    best_score = score(best_motifs)
    
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i+k]]
        for j in range(1, t):
            profile = calculate_profile(motifs)
            most_probable_kmer = profile_most_probable_kmer(dna[j], k, profile)
            motifs.append(most_probable_kmer)
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs
    
    return best_motifs

def read_input(file_path):
    """Read input data from a file and parse it."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        k, t = map(int, lines[0].strip().split())
        dna = lines[1].strip().split()
    return k, t, dna

# File path
file_path = 'dataset_30306_9.txt'

# Read the input
k, t, dna = read_input(file_path)

# Function Call
result = greedy_motif_search(dna, k, t)
print(' '.join(result))
