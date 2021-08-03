def GreedyMotifSearchWithPseudocounts(DNA_list, k, t, pseudocount = 1):
	BestMotifs = [dna[0:k] for dna in DNA_list]
	LowestScore = CalculateScore(BestMotifs)
	DNA = DNA_list[0]
	for i in range(len(DNA) - k + 1):
		Motifs = [DNA[i:i + k]]
		for j in range(1, t):
			profile = FormProfileWithPseudoCounts(Motifs, pseudocount)
			Motifs.append(ProfileMostProbableKmer(DNA_list[j], k, profile))
		CurrentScore = CalculateScore(Motifs)
		if CurrentScore < LowestScore:
			BestMotifs = Motifs
			LowestScore = CurrentScore
	return BestMotifs

def FormProfileWithPseudoCounts(TextList, pseudocount = 1):
	if type(TextList) != list:
		TextList = [TextList]
	t = len(TextList)
	k = len(TextList[0])
	profile = {'A': [pseudocount]*k, 'C': [pseudocount]*k, 'G': [pseudocount]*k, 'T': [pseudocount]*k}
	for i in range(k):
		for j in range(t):
			profile[TextList[j][i]][i] += 1
	return profile

def ProfileMostProbableKmer(text, k, profile):
	max_prob = -1
	for i in range(len(text) - k + 1):
		Pattern = text[i:i + k]
		prob = profile[Pattern[0]][0]
		for j in range(1, len(Pattern)):
			prob *= profile[Pattern[j]][j]
		if prob > max_prob:
			most_probable = Pattern
			max_prob = prob
	return most_probable

def HammingDistance(p, q):
	mm = [p[i] != q[i] for i in range(len(p))]
	return sum(mm)

def CalculateScore(Motifs):
	k = len(Motifs[0])
	profile = FormProfileWithPseudoCounts(Motifs)
	consensus = ''
	for i in range(k):
		most_freq = 0
		for nuc in ['A', 'C', 'G', 'T']:
			if profile[nuc][i] > most_freq:
				most_freq = profile[nuc][i]
				to_add = nuc
		consensus += to_add
	score = 0
	for motif in Motifs:
		score += HammingDistance(consensus, motif)
	return score

DNA_list = []
file = open('dataset_160_9.txt')
for i, line in enumerate(file):
	if i == 0:
		k, t = map(int, line.rstrip().split(' '))
	else:
		DNA_list.append(line.rstrip())
print('\n'.join(DNA_list))