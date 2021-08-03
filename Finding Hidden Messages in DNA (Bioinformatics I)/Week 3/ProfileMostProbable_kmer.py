with open('dataset_159_3.txt', 'r') as file:
	text = file.readline().strip()
	k = int(file.readline())
	profile = [x.strip().split() for x in file.readlines()]
	profile = [list(map(float, x)) for x in profile]

base_dict = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3}
kmer_dict = {}
for index in range(len(text) - k + 1):
	kmer = text[index : index + k]
	prob = 1
	for base_index in range(len(kmer)):
		base = kmer[base_index]
		base_prob = profile[base_dict[base]][base_index]
		prob *= base_prob
	kmer_dict[kmer] = prob

print(max(kmer_dict, key = kmer_dict.get))