"""
Hamming Distance Problem: Compute the Hamming distance between two strings.

- Input: Two strings of equal length.
- Output:The Hamming distance between these strings.

Sample Input: 
    GGGCCGTTGGT
    GGACCGTTGAC

Sample Output:
    3
"""


def HammingDistance(p, q):
    # your code here
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist +=1
    print(dist)
    return dist


if __name__ == '__main__':
    sequence1 = input("What is the first genomic sequence?\n")
    sequence2 = input("What is the second genomic sequence?\n ")
    HammingDistance(sequence1,sequence2)