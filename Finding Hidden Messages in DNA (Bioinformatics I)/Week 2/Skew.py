def skew_diagram(genome):
    n = len(genome)
    skew_values = [0] * (n + 1)
    
    for i in range(1, n + 1):
        skew_values[i] = skew_values[i - 1]
        if genome[i - 1] == 'G':
            skew_values[i] += 1
        elif genome[i - 1] == 'C':
            skew_values[i] -= 1
    
    return skew_values

# Example usage:
genome = "GAGCCACCGCGATA"
skew_values = skew_diagram(genome)

# Print the skew values from 0 to 14
print(" ".join(map(str, skew_values[:15])))

