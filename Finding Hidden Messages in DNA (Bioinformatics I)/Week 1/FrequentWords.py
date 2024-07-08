def FrequentWords(Text, k):
    kmer_count = {}
    max_count = 0
    
    for i in range(len(Text) - k + 1):
        kmer = Text[i:i+k]
        if kmer in kmer_count:
            kmer_count[kmer] += 1
        else:
            kmer_count[kmer] = 1
        if kmer_count[kmer] > max_count:
            max_count = kmer_count[kmer]
   
    #Find the most frequent k-mers
    most_frequent_kmers = [kmer for kmer in kmer_count if kmer_count[kmer] == max_count]
    
    return ' '.join(most_frequent_kmers)

with open('dataset_30272_13.txt', 'r') as file:
	text = file.readline().strip()
	k = int(file.readline().strip())
 
result = FrequentWords(text, k)

print(result)

