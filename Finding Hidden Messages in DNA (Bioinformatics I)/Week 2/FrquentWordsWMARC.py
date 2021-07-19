"""
Frequent Words with Mismatches and Reverse Complements Problem: Find the most frequent k-mers (with mismatches and reverse complements) in a string.

- Input:  A DNA string Text as well as integers k and d.
- Output: All k-mers Pattern maximizing the sum Count_d(Text, Pattern)+ Count_d(Text, Pattern_rc) over all possible k-mers.

Sample Input:  
 ACGTTGCATGTCGCATGATGCATGAGAGCT
 4 1

Sample Output:
 ATGT ACAT
"""

def ReverseComplement(seq):
    for base in seq:
        if base not in 'ATCGatcg':
            print("Error: NOT a DNA sequence")
            return None
    seq1 = 'ATCGTAGCatcgtagc'
    seq_dict = { seq1[i]:seq1[i+4] for i in range(16) if i < 4 or 8<=i<12 }
    return "".join([seq_dict[base] for base in reversed(seq)])


def ImmediateNeighbors(pattern):
    neighbor = set()
    nset = {'A', 'C', 'G', 'T'}
    for i in range(len(pattern)):
        for n in nset:
            neighbor.add(pattern[:i]+n+pattern[i+1:])
    return neighbor

def Neighbors(pattern, d):
    if d == 0:
        return {pattern}
    ineighbor = ImmediateNeighbors(pattern)
    neighbor = ineighbor
    for j in range(d-1):
        for p in ineighbor:
            neighbor = neighbor.union(ImmediateNeighbors(p))
        ineighbor = neighbor
    return neighbor

def FrequentWordsWMARC(text, k, d):
    #Frequent Words with Mismatches and Reverse Complements
    counts = dict()
    for i in range(len(text)-k+1):
        neighbor = Neighbors(text[i:i+k], d)
        for n in neighbor:
            nrc = ReverseComplement(n)
            counts[n] = counts.get(n, 0) + 1
            counts[nrc] = counts.get(nrc, 0) + 1
    m = max(counts.values())
    return [t for t, v in counts.items() if v == m]                
   
if __name__ == "__main__":
    sequence = input("What is the genomic sequence?\n")
    k = int(input("What is the k?\n"))
    d = int(input("What is the d?\n"))
    
    frequent_words = FrequentWordsWMARC(sequence, k, d)
    print(' '.join(frequent_words))