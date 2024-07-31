def minimum_skew(genome):
    n = len(genome)
    min_skew = float('inf')
    min_indices = []

    current_skew = 0
    for i in range(n + 1):
        if current_skew < min_skew:
            min_skew = current_skew
            min_indices = [i]
        elif current_skew == min_skew:
            min_indices.append(i)

        if i < n:
            if genome[i] == 'G':
                current_skew += 1
            elif genome[i] == 'C':
                current_skew -= 1
    
    return min_indices

# Function to read genome from a text file
def read_genome_from_file(file_path):
    with open(file_path, 'r') as file:
        genome = file.read().strip()
    return genome

# Example usage:
file_path = 'dataset_30277_10.txt'  # Replace with your file path
genome = read_genome_from_file(file_path)
min_skew_positions = minimum_skew(genome)

# Print the positions where minimum skew occurs
print(" ".join(map(str, min_skew_positions)))
