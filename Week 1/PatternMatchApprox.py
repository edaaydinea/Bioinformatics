def approx(kmer, substring, k, n):
	count = 0
	for i in range(k):
		if substring[i] != kmer[i]:
			count += 1
		if count > n:
			return False
	return True

sequence = input("What is the genetic sequence? ")
pattern = input("What is the pattern? ")
n = int(input("What is the maximum number of mismatches? "))

DNA = str(sequence.upper())
kmer = str(pattern.upper())
k = len(kmer)
output = list()


for i in range(0, len(DNA) - k + 1):
	substring = DNA[i:i + k]
	if approx(kmer, substring, k, n) is True:
		output.append(str(i))

answer = ' '.join(output)
print(answer)