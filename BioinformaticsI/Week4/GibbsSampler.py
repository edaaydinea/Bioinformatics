import random
import numpy as np
from collections import defaultdict

def score(motifs):
    """Score a set of motifs as the number of columns that have a consensus."""
    transposed_motifs = list(zip(*motifs))
    consensus = []
    score = 0
    for column in transposed_motifs:
        most_common = max(set(column), key=column.count)
        consensus.append(most_common)
        score += len(column) - column.count(most_common)
    return score

def profile_with_pseudocounts(motifs):
    """Generate profile matrix with pseudocounts."""
    pseudocount = 1
    k = len(motifs[0])
    t = len(motifs)
    profile = defaultdict(lambda: [pseudocount] * k)
    
    for motif in motifs:
        for i in range(k):
            profile[motif[i]][i] += 1
            
    for nucleotide in profile:
        total = sum(profile[nucleotide])
        for i in range(k):
            profile[nucleotide][i] /= (t + 4 * pseudocount)
    
    return profile

def profile_most_probable_kmer(text, k, profile):
    """Find the k-mer with the highest probability according to the profile matrix."""
    max_prob = -1
    most_probable_kmer = text[:k]
    
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob = 1
        for j, nucleotide in enumerate(kmer):
            prob *= profile[nucleotide][j]
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer
    
    return most_probable_kmer

def gibbs_sampler(Dna, k, t, N):
    """Perform the Gibbs Sampler algorithm."""
    motifs = [random.choice([seq[i:i+k] for i in range(len(seq) - k + 1)]) for seq in Dna]
    best_motifs = motifs[:]
    best_score = score(motifs)
    
    for _ in range(N):
        i = random.randint(0, t - 1)
        reduced_motifs = motifs[:i] + motifs[i+1:]
        profile = profile_with_pseudocounts(reduced_motifs)
        motifs[i] = profile_most_probable_kmer(Dna[i], k, profile)
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs[:]
    
    return best_motifs

# Input reading from file
def main():
    filename = 'dataset_30309_11.txt'
    
    with open(filename, 'r') as file:
        data = file.read().split()
    
    k = int(data[0])
    t = int(data[1])
    N = int(data[2])
    Dna = data[3:]
    
    # Run Gibbs Sampler 20 times and return the best motifs
    best_motifs = None
    best_score = float('inf')
    
    for _ in range(20):
        motifs = gibbs_sampler(Dna, k, t, N)
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs
    
    print(" ".join(best_motifs))

if __name__ == "__main__":
    main()
