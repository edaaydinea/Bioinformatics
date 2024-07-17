def hamming_distance(s1, s2):
    # Calculate Hamming distance between two strings of equal length
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance

def approximate_pattern_matching(pattern, text, d):
    k = len(pattern)
    n = len(text)
    positions = []

    for i in range(n - k + 1):
        substring = text[i:i + k]
        if hamming_distance(pattern, substring) <= d:
            positions.append(i)

    return positions

# Function to read inputs from a text file
def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    pattern = lines[0].strip()
    text = lines[1].strip()
    d = int(lines[2].strip())
    return pattern, text, d

# Example usage:
file_path = 'dataset_30278_4.txt'  # Replace with your file path
pattern, text, d = read_input_from_file(file_path)
matches = approximate_pattern_matching(pattern, text, d)

# Print the starting positions of approximate matches
print(" ".join(map(str, matches)))
