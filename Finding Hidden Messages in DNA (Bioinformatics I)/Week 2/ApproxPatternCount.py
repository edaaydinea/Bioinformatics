def hamming_distance(s1, s2):
    # Calculate Hamming distance between two strings of equal length
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance

def approximate_pattern_count(text, pattern, d):
    k = len(pattern)
    n = len(text)
    count = 0

    for i in range(n - k + 1):
        substring = text[i:i + k]
        if hamming_distance(pattern, substring) <= d:
            count += 1

    return count

# Function to read inputs from a text file
def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    pattern = lines[0].strip()
    text = lines[1].strip()
    d = int(lines[2].strip())
    return pattern, text, d

# Example usage:
file_path = 'dataset_30278_6.txt'  # Replace with your file path
pattern, text, d = read_input_from_file(file_path)
count = approximate_pattern_count(text, pattern, d)

# Print the result
print(count)
