def ReverseComplement(Pattern):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = ''
    
    # Iterate through Pattern in reverse order, compute complement, and build reverse complement string
    for nucleotide in reversed(Pattern):
        reverse_complement += complement[nucleotide]
    
    return reverse_complement

# Read input from file
with open('dataset_30273_2.txt', 'r') as file:
    pattern = file.readline().strip()

# Get the result
result = ReverseComplement(pattern)

# Print the output
print(result)
