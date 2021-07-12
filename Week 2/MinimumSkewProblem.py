"""
Minimum Skew Problem: Find a position in a genome algorithm where the skew diagram attains a minimum.

- Input: A DNA string Genome.
- Output: All integer(s) i minimizing Skew_i (Genome) among all values of i (from 0 to |Genome|)

Sample Input:  TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT

Sample Output: 11 24
"""

def min_skew(genome):
    skew_i = 0
    min_skew = 1000000
    min_list = []
    for i in range(0, len(genome)):        
        nuc = genome[i]
        if nuc == "G":
            skew_i += 1
        elif nuc == "C":
            skew_i -= 1
        
        else:
            pass
        
        print (i, skew_i)
        if skew_i == min_skew:
             min_list.append(i + 1)
        elif skew_i < min_skew:
            min_list = [i + 1]
            min_skew = skew_i
    return min_list

if __name__ == '__main__':
    genome = input("What is the genome sequence?\n")
    min_list = min_skew(genome)
    print (min_list)