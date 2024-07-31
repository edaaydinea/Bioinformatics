def generate_neighborhood(pattern, d):
    # Helper function to generate all d-neighbors
    def neighbors(pattern, d):
        if d == 0:
            return {pattern}
        if len(pattern) == 0:
            return set()
        
        nucleotides = ['A', 'C', 'G', 'T']
        neighborhood = set()
        suffix_neighbors = neighbors(pattern[1:], d)
        
        for text in suffix_neighbors:
            if hamming_distance(pattern[1:], text) < d:
                for nucleotide in nucleotides:
                    neighborhood.add(nucleotide + text)
            else:
                neighborhood.add(pattern[0] + text)
        
        return neighborhood

    # Helper function to calculate the Hamming distance
    def hamming_distance(p, q):
        return sum(1 for a, b in zip(p, q) if a != b)
    
    return neighbors(pattern, d)

# Define the pattern and distance
pattern = "CCAGTCAATG"
d = 1

# Generate the 1-neighborhood
neighborhood = generate_neighborhood(pattern, d)

# Print the number of 10-mers in the 1-neighborhood
print(f"The number of 10-mers in the 1-neighborhood of {pattern} is {len(neighborhood)}")

# Optionally, print the neighborhood
for neighbor in neighborhood:
     print(neighbor)
