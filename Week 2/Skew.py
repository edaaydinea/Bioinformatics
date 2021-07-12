def skew(genome, irange):
    skew_i = 0
    skew_list = [0]
    for i in range(0, len(genome)):        
        nuc = genome[i]
        if nuc == "G":
            skew_i += 1
        elif nuc == "C":
            skew_i -= 1
        else:
            pass
        skew_list.append(skew_i)        
    return skew_list

if __name__ == '__main__':
    genome = input("What is the genomic sequence?")
    irange = int(input("What is the range?"))

    skew_list = skew(genome, irange)
    print (skew_list)