def hamming_distance(s1, s2):
    # Calculate Hamming distance between two strings of equal length
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance

def generate_neighbors(pattern, d):
    # Generate all neighbors of a pattern with up to d mismatches
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    
    neighborhood = set()
    suffix_neighbors = generate_neighbors(pattern[1:], d)
    for neighbor in suffix_neighbors:
        if hamming_distance(pattern[1:], neighbor) < d:
            for nucleotide in ['A', 'C', 'G', 'T']:
                neighborhood.add(nucleotide + neighbor)
        else:
            neighborhood.add(pattern[0] + neighbor)
    
    return neighborhood

# Function to read inputs from a text file and return Pattern and d
def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    Pattern = lines[0].strip()
    d = int(lines[1].strip())
    return Pattern, d

# Function to output the collection of strings Neighbors(Pattern, d)
def neighbors(Pattern, d):
    neighbor_set = generate_neighbors(Pattern, d)
    return sorted(neighbor_set)

# Main function to execute the task
def main():
    file_path = 'dataset_30282_4.txt'  # Replace with your file path
    Pattern, d = read_input_from_file(file_path)
    result = neighbors(Pattern, d)
    # Remove , ' and [] from the list
    result = str(result).replace(",", "").replace("'", "").replace("[", "").replace("]", "")
    print(result)

if __name__ == "__main__":
    main()
