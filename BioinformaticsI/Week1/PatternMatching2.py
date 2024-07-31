def PatternMatching(Pattern, Genome):
    positions = []
    pattern_length = len(Pattern)
    genome_length = len(Genome)
    
    # Iterate through the genome to find matches
    for i in range(genome_length - pattern_length + 1):
        if Genome[i:i+pattern_length] == Pattern:
            positions.append(i)
    
    return positions

# Read genome from file
genome_file = "Vibrio_cholerae.txt"
pattern = "CTTGATCAT"

with open(genome_file, 'r') as file:
    genome = file.read().replace('\n', '')

# Find positions where pattern appears in genome
positions = PatternMatching(pattern, genome)

# Print positions in required format
print(' '.join(map(str, positions)))
