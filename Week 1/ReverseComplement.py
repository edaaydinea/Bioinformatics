dataset = input("What is the DNA string pattern? ")

forwardString = list(str(dataset.upper()))

def complement(DNAstring):
	for n, i in enumerate(DNAstring):
		if i == "A":
			DNAstring[n] = "T"
		elif i == "T":
			DNAstring[n] = "A"
		elif i == "C":
			DNAstring[n] = "G"
		elif i == "G":
			DNAstring[n] = "C"

	DNAstring.reverse()
	answer = ''.join(DNAstring)
	print(" ")
	print(answer)
	return None

complement(forwardString)