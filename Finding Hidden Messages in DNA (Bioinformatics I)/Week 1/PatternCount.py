Pattern = input("What is the pattern? ")
Text = input("What is the genomic sequence? ")

def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

PatternCount(Pattern, Text)