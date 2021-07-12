sequence = input("What is the genomic sequence?\n ")
pattern = input("What is the pattern?\n")

DNA = str(sequence.upper())
kmer = str(pattern.upper())
k = len(kmer)
output = list()

for i in range(0, len(DNA) - k + 1):
	substring = DNA[i:i + k]
	if substring == kmer:
		output.append(str(i))

answer = ' '.join(output)
print(answer)