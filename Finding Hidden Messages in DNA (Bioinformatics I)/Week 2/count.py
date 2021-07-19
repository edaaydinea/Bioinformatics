def patternCount(Text, Pattern):
    # count the number of times a given pattern appears
    count = 0

    for i in range(0, len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count += 1
    print(count)
    return count

patternCount("AACAAGCTGATAAACATTTAAAGAG","AAAAA")