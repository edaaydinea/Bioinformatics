def ClumpFinding(Genome, k, L, t):
    clump_kmers = set()
    kmer_count = {}
    
    # Initialize the first window of length L
    first_window = Genome[:L]
    for i in range(L - k + 1):
        kmer = first_window[i:i+k]
        if kmer in kmer_count:
            kmer_count[kmer] += 1
        else:
            kmer_count[kmer] = 1
    
    # Check k-mers in the first window for t occurrences
    for kmer, count in kmer_count.items():
        if count >= t:
            clump_kmers.add(kmer)
    
    # Slide the window across the genome
    for i in range(1, len(Genome) - L + 1):
        # Remove the k-mer that is sliding out of the window
        old_kmer = Genome[i - 1:i - 1 + k]
        if kmer_count[old_kmer] == 1:
            del kmer_count[old_kmer]
        else:
            kmer_count[old_kmer] -= 1
        
        # Add the new k-mer that is sliding into the window
        new_kmer = Genome[i + L - k:i + L]
        if new_kmer in kmer_count:
            kmer_count[new_kmer] += 1
        else:
            kmer_count[new_kmer] = 1
        
        # Check the new k-mer for t occurrences
        if kmer_count[new_kmer] >= t:
            clump_kmers.add(new_kmer)
    
    return clump_kmers

# Read input from file
input_file = "dataset_30274_5.txt"
with open(input_file, 'r') as file:
    Genome = file.readline().strip()
    k, L, t = map(int, file.readline().strip().split())

# Get the result
result = ClumpFinding(Genome, k, L, t)

# Print the output in required format
print(' '.join(result))