"""
Implement Neighbors to find the d-neighborhood of a string.

- Input: A string Pattern and an integer d.
- Output: The collection of strings Neighbors(Pattern, d). (You may return the strings in any order, but each line should contain only one string.)

Sample Input: 
    ACG
    1

Sample Output:
    CCG TCG GCG AAG ATG AGG ACA ACC ACT ACG

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

if __name__ == '__main__':
    pattern = input("What is the pattern?\n")
    d = int(input("What is the d?\n"))
    ImmediateNeighbors(pattern)
    n = Neighbors(pattern,d)
    print(' '.join(n))
