def HammingDistance(p, q):
	mm = [p[i] != q[i] for i in range(len(p))]
	return sum(mm)

def DistanceBetweenPatternAndStrings(Pattern, Dna_list):
	dist = 0
	k = len(Pattern)
	for dna in Dna_list:
		min_dist = len(dna)
		for i in range(len(dna) - k + 1):
			pat = dna[i:i + k]
			current_d = HammingDistance(pat, Pattern)
			if current_d < min_dist:
				min_dist = current_d
		dist += min_dist
	return dist
    
file = open('dataset_5164_1.txt')
for i, line in enumerate(file):
	if i == 0:
		Pattern = line.rstrip()
	else:
		Dna_list = line.rstrip().split(' ')

DistanceBetweenPatternAndStrings(Pattern, Dna_list)