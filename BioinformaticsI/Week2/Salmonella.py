def find_dnaA_box(genome_sequence, motif):
    motif_length = len(motif)
    matches = []

    # Scan through the genome sequence to find matches to the motif
    for i in range(len(genome_sequence) - motif_length + 1):
        if genome_sequence[i:i + motif_length] == motif:
            matches.append(i)

    return matches

# Function to read genome sequence from a text file
def read_genome_from_file(file_path):
    with open(file_path, 'r') as file:
        genome_sequence = file.read().strip().upper()  # Convert to uppercase for case insensitivity
    return genome_sequence

# Main function to find DnaA box in Salmonella enterica
def main():
    file_path = 'salmonella_enterica_genome.txt'  # Replace with your file path
    genome_sequence = read_genome_from_file(file_path)
    motif = "TTATCCACA"
    
    # Find DnaA box occurrences
    matches = find_dnaA_box(genome_sequence, motif)

    # Output results
    if matches:
        print(f"Found {len(matches)} occurrences of DnaA box motif '{motif}' in the Salmonella enterica genome:")
        for match in matches:
            print(f"Position {match}")
    else:
        print(f"No occurrences of DnaA box motif '{motif}' found in the Salmonella enterica genome.")

if __name__ == "__main__":
    main()
