"""
Frequent Words with Mismatches Problem:

- Input:  A DNA string Text as well as integers k and d.
- Output: All k-mers Pattern maximizing the sum Count_d(Text, Pattern)+ Count_d(Text, Pattern_rc) over all possible k-mers.

Sample Input:  
 ACGTTGCATGTCGCATGATGCATGAGAGCT
 4 1

Sample Output:
 GATG ATGC ATGT
"""
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

def FrequentWordsWithMismatches(text, k, d):
    counts = dict()
    for i in range(len(text)-k+1):
        neighbor = Neighbors(text[i:i+k], d)
        for n in neighbor:
            counts[n] = counts.get(n, 0) + 1
    m = max(counts.values())
    return [t for t, v in counts.items() if v == m]   
              
   
if __name__ == "__main__":
    sequence = input("What is the genomic sequence?\n")
    k = int(input("What is the k?\n"))
    d = int(input("What is the d?\n"))
    
    frequent_words = FrequentWordsWithMismatches(sequence, k, d)
    print(' '.join(frequent_words))