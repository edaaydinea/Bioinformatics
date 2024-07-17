def hamming_distance(s1, s2):
    # Calculate Hamming distance between two strings of equal length
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance

def count_with_mismatches(text, pattern, d):
    k = len(pattern)
    n = len(text)
    count = 0

    for i in range(n - k + 1):
        substring = text[i:i + k]
        if hamming_distance(pattern, substring) <= d:
            count += 1

    return count

# Example usage:
text = "TACGCATTACAAAGCACA"
pattern = "TGT"
d = 2
count = count_with_mismatches(text, pattern, d)

# Print the result
print(count)
