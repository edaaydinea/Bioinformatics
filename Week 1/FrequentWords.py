# Frequent Words Problem: Find the most frequent k-mers in a string.
#      Input: A string Text and an integer k.
#      Output: All most frequent k-mers in Text.

# Sample Input:
#      ACGTTGCATGTCGCATGATGCATGAGAGCT
#      4

# Sample Output:
#      CATG GCAT

sequence = input("What is the genomic sequence? ")
k = int(input("What is the length of k-mer? "))

DNA = str(sequence.upper())

counts = {}

for i in range(0, len(DNA) - k + 1):
	kmer = DNA[i:i + k]
	if kmer in counts:
		counts[kmer] += 1
	else:
		counts[kmer] = 1

frequent = max(counts.values())

ans = []
for k in counts:
	if counts[k] == frequent:
		print(k)
		ans.append(k)
		
print(ans)
