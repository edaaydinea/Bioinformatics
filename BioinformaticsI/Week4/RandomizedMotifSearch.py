import random

def ProfileWithPseudocounts(motifs):
    k = len(motifs[0])
    profile = {
        'A': [1] * k,
        'C': [1] * k,
        'G': [1] * k,
        'T': [1] * k
    }
    
    for motif in motifs:
        for i, nucleotide in enumerate(motif):
            profile[nucleotide][i] += 1
            
    total_counts = len(motifs) + 4
    
    for nucleotide in profile:
        for i in range(k):
            profile[nucleotide][i] /= total_counts
    
    return profile

def Pr(kmer, profile):
    prob = 1.0
    for i, nucleotide in enumerate(kmer):
        prob *= profile[nucleotide][i]
    return prob

def ProfileMostProbableKmer(text, k, profile):
    max_prob = -1
    most_probable_kmer = text[:k]
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob = Pr(kmer, profile)
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer
    return most_probable_kmer

def Score(motifs):
    consensus = ''
    k = len(motifs[0])
    for i in range(k):
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            count[motif[i]] += 1
        consensus += max(count, key=count.get)
    return sum(hamming_distance(consensus, motif) for motif in motifs)

def hamming_distance(p, q):
    return sum(pc != qc for pc, qc in zip(p, q))

def RandomMotifs(Dna, k, t):
    random_motifs = []
    for i in range(t):
        start = random.randint(0, len(Dna[i]) - k)
        random_motifs.append(Dna[i][start:start + k])
    return random_motifs

def RandomizedMotifSearch(Dna, k, t):
    motifs = RandomMotifs(Dna, k, t)
    best_motifs = motifs[:]
    while True:
        profile = ProfileWithPseudocounts(motifs)
        motifs = [ProfileMostProbableKmer(dna, k, profile) for dna in Dna]
        if Score(motifs) < Score(best_motifs):
            best_motifs = motifs[:]
        else:
            return best_motifs

def main():
    # Read input from file
    with open('dataset_30307_5.txt', 'r') as file:
        lines = file.readlines()
    
    k, t = map(int, lines[0].strip().split())
    Dna = lines[1].strip().split()
    
    best_motifs = RandomizedMotifSearch(Dna, k, t)
    best_score = Score(best_motifs)
    
    for _ in range(1000):
        motifs = RandomizedMotifSearch(Dna, k, t)
        current_score = Score(motifs)
        if current_score < best_score:
            best_motifs = motifs
            best_score = current_score
    
    print(" ".join(best_motifs))

if __name__ == "__main__":
    main()
