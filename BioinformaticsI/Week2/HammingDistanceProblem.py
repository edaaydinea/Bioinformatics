def hamming_distance(s1, s2):
    # Ensure strings are of equal length
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")

    # Calculate Hamming distance
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance

# Function to read strings from a text file
def read_strings_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    s1 = lines[0].strip()
    s2 = lines[1].strip()
    return s1, s2

# Example usage:
file_path = 'dataset_30278_3.txt'  # Replace with your file path
s1, s2 = read_strings_from_file(file_path)
distance = hamming_distance(s1, s2)

# Print the Hamming distance
print(distance)
