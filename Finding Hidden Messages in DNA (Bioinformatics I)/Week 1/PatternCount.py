def PatternCount(Text, Pattern):
    count = 0
    pattern_length = len(Pattern)
    text_length = len(Text)
    
    for i in range(text_length - pattern_length + 1):
        if Text[i:i+pattern_length] == Pattern:
            count += 1
    
    return count

# Read input from file
with open('dataset_30272_6.txt', 'r') as file:
    text = file.readline().strip()
    pattern = file.readline().strip()

# Get the result
result = PatternCount(text, pattern)

# Print the output
print(result)