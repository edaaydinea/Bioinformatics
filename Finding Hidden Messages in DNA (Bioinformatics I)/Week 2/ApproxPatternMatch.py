"""
Approximate Pattern Matching Problem: Find all approximate occurences of pattern in a string.

- Input: Strings Pattern and Text along with an integer d.
- Output: All starting positions where Pattern appears as as substring of Text with at most d mismatches.

Sample Input:
ATTCTGGA
CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
3

Sample Output:
6 7 26 27
"""

def HammingDistance(seq1, seq2):
    return len([i for i in range(len(seq1)) if seq1[i] != seq2[i]])
    
def ApproxPatternMatching(pattern, text, d):
    pos = []
    l = len(pattern)
    for i in range(len(text)-l+1):
        if HammingDistance(pattern, text[i:i+l]) <= d:
            pos.append(i)
    return pos
 
   
if __name__ == "__main__":
    pattern = input("What is the pattern?\n")
    sequence = input("What is the genomic sequence?\n")
    d = int(input("What is the integer?\n"))
    pos = ApproxPatternMatching(pattern, sequence,d)
    print(*pos, sep = " ")