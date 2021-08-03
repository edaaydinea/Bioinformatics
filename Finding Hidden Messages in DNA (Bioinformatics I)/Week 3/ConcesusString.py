def Count(Motifs):
    # initializing the count dictionary
    count = {}
    # all motifs will have the same string length
    k = len(Motifs[0])
    # for each letter
    for symbol in "ACGT":
        # each key in the dictionary ("A", "C", "G", "T") will store a list
        count[symbol] = []
        # loop through each letter within the motif string
        for j in range(k):
            # create a placeholder for count
            count[symbol].append(0)
    # number of motifs in input matrix
    t = len(Motifs)
    # for each motif
    for i in range(t):
        # for each letter in motif
        for j in range(k):
            # save the current letter into a variable
            symbol = Motifs[i][j]
            # add to total in count dictionary[current letter][char in motif]
            count[symbol][j] += 1
    return count

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count = Count(Motifs)
    for key, motif_lists in sorted(count.items()):
        profile[key] = motif_lists
        for motif_list, number in enumerate(motif_lists):
            motif_lists[motif_list] = number/t
    return profile

def Consensus(Motifs):
    k = len(Motifs[0])
    profile = Profile(Motifs)
    consensus = ""
    for j in range(k):
        maximum = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if profile[symbol][j] > maximum:
                maximum = profile[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

profile = {'A': [0.4,  0.3,  0.0,  0.1,  0.0,  0.9],
           'T': [0.3,  0.1,  0.0,  0.4,  0.5,  0.0],
           'G': [0.1,  0.3,  1.0,  0.1,  0.5,  0.0],
           'C': [0.2,  0.3,  0.0,  0.4,  0.0,  0.1]}

motif1 = "AACGTA"
motif2 = "CCCGTT"
motif3 = "CACCTT"
motif4 = "GGATTA"
motif5 = "TTCCGG"
motifs = [motif1, motif2, motif3, motif4, motif5]

print(Consensus(motifs))