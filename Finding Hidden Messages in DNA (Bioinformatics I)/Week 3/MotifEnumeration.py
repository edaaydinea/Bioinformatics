def HammingDistance(p,q):
	distance = 0
	for i in range(len(p)):
		if (p[i] != q[i]):
			distance += 1
	return distance

def ImmediateNeighbors(pattern):
	alphabet = ['A','T','C','G']
	Neighborhood = set()
	for i in range(len(pattern)):
		symbol = pattern[i]
		for nt in alphabet:
			if (nt != symbol[i]):
				Neighbor = pattern[:i] + nt + pattern[i+1:]
				Neighborhood.add(Neighbor)
	return Neighborhood

def Neighbors(pattern,d):
	alphabet = ['A','T','C','G']
	if (d == 0):
		return set([pattern])
	if (len(pattern) == 1):
		return set(alphabet)
	Neighborhood = set()
	SuffixNeighbors = Neighbors(pattern[1:],d)
	for each in SuffixNeighbors:
		if (HammingDistance(pattern[1:], each) < d):
			for nt in alphabet:
				Neighborhood.add(nt + each)
		else:
			Neighborhood.add(pattern[0] + each)
	return Neighborhood

def MotifEnumeration(Dna, k, d):
	kmers = []
	for i in range(len(Dna)):
		ls = set()
		for j in range(len(Dna[i])-k+1):
			string = Dna[i][j:j+k]
			ls.update(Neighbors(string,d))
			ls.add(string)
		kmers.append(ls)
	Patterns = kmers[0]
	for s in kmers[1:]:
		Patterns.intersection_update(s)
	return Patterns

seqs = ['CTGGCAGTATTTGGCGCAGCACCAC','TTACGATGGCCTAATCGGACTCTAC','CGCCCTTGGGCGCTCGACTACAGAC','TTATCGTCCCAATGAGCACCTTGGC','GAAAGCGTACATTGCTTGGGCTAGC','ACAGCATGGAATTCCTTCAGCGACC']
ans = MotifEnumeration(seqs,5,2)

output = open('motifenumeration.txt','w')
output.write(' '.join(map(str,ans)))
output.close()