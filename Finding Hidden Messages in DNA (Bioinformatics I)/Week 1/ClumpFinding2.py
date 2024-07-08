def ClumpFindingCount(Genome, k, L, t):
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
    
    return len(clump_kmers)

# Read E. coli genome from file
genome_file = "E_coli.txt"
with open(genome_file, 'r') as file:
    Genome = file.read().replace('\n', '')

# Define parameters for Clump Finding
k = 9
L = 500
t = 3

# Get the count of unique 9-mers forming (500, 3)-clumps
count = ClumpFindingCount(Genome, k, L, t)

# Print the count
print(count)
