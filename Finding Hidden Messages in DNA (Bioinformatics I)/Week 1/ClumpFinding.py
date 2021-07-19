sequence = input("What is the genomic sequence? ")
k = int(input("What is the length k of each kmer? "))
L = int(input("What is the length of clump L? "))
t = int(input("What is the minimum times t? "))

DNA = str(sequence.upper())

# Count the number of each kmer
# Produce dictionary with (kmer, number of times) pairs in counts

counts = {}

for i in range(0, len(DNA) - k + 1):
	kmer = DNA[i:i + k]
	if kmer in counts:
		counts[kmer] += 1
	else:
		counts[kmer] = 1

# print(counts)
# print(counts.values())

# Eliminate all pairs that appear less than t times; new dict called frequent

frequent = {}

for k in counts:
	if counts[k] >= t:
		frequent[k] = counts[k]

answer = frequent.keys()
output = ' '.join(answer)
print(output)