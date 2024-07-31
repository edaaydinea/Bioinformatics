def PatternMatching(Pattern, Genome):
    positions = []
    pattern_length = len(Pattern)
    genome_length = len(Genome)
    
    # Iterate through the genome to find matches
    for i in range(genome_length - pattern_length + 1):
        if Genome[i:i+pattern_length] == Pattern:
            positions.append(i)
    
    return positions

# Read input from file
with open('dataset_30273_5.txt', 'r') as file:
    pattern = file.readline().strip()
    genome = file.readline().strip()

# Get the result
result = PatternMatching(pattern, genome)

# Print the output
print(' '.join(map(str, result)))
