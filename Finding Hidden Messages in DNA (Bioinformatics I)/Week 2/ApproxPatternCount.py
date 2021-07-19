"""
Approximate Pattern Count

- Input: String Pattern and Text as well as an integer d
- Output: Count_d(Text,Pattern)

Sample Input:
GAGG
TTTAGAGCCTTCAGAGG
2

Sample Output:
4
"""

def HammingDistance(seq1, seq2):
    return len([i for i in range(len(seq1)) if seq1[i] != seq2[i]])

def ApproxPatternCount(pattern, text, d):
    c = 0
    l = len(pattern)  
    for i in range(len(text)-l+1):
        if HammingDistance(pattern, text[i:i+l]) <= d:
            c += 1
    return c  

if __name__ == "__main__":
    pattern = input("What is the pattern?\n")
    sequence = input("What is the genomic sequence?\n")
    d = int(input("What is the integer?\n"))
    pos = ApproxPatternCount(pattern, sequence,d)
    print(pos)