"""

Implement GreedyMotifSearch

- Input: Integers k and t, followed by a collection of strings Dna.
- Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.

Sample Input:
3 5
GGCGTTCAGGCA AAGAATCAGTCA CAAGGAGTTCGC CACGTCAATCAC CAATAATATTCG

Sample Output:
CAG CAG CAA CAA CAA
"""

def profile_most_probable_kmer(text, k, profile):
    """Return the Profile-most probable k-mer in a string."""
    max_prob = -1
    most_probable_kmer = text[:k]
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = 1
        for j in range(k):
            if kmer[j] == 'A':
                prob *= profile[0][j]
            elif kmer[j] == 'C':
                prob *= profile[1][j]
            elif kmer[j] == 'G':
                prob *= profile[2][j]
            elif kmer[j] == 'T':
                prob *= profile[3][j]
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer
    return most_probable_kmer

def profile_matrix(motifs, k):
    """Return the profile matrix of motifs."""
    profile = [[0]*k for _ in range(4)]
    for i in range(k):
        column = ''.join([motif[i] for motif in motifs])
        for j in range(4):
            profile[j][i] = column.count('ACGT'[j]) / len(column)
    return profile

def score(motifs):
    """Return the score of motifs."""
    k = len(motifs[0])
    profile = profile_matrix(motifs, k)
    consensus = ''
    for j in range(k):
        max_freq = 0
        frequent_symbol = ''
        for i in range(4):
            if profile[i][j] > max_freq:
                max_freq = profile[i][j]
                frequent_symbol = 'ACGT'[i]
        consensus += frequent_symbol
    score = 0
    for motif in motifs:
        score += sum([1 for i in range(k) if motif[i] != consensus[i]])
    return score

def greedy_motif_search(dna, k, t):
    """Return the best motifs in dna."""
    best_motifs = [string[:k] for string in dna]
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i+k]]
        for j in range(1, t):
            profile = profile_matrix(motifs, k)
            motifs.append(profile_most_probable_kmer(dna[j], k, profile))
        if score(motifs) < score(best_motifs):
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
file_path = 'dataset_30305_5.txt'

# Read the input
k, t, dna = read_input(file_path)

# Function Call
result = greedy_motif_search(dna, k, t)
print(' '.join(result))
