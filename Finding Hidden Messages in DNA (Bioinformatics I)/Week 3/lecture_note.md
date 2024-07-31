# From Implanted Patterns to Regulatory Motifs (Part 1)

1. **Game Introduction**
    - Generate ten random sequences
    - Insert a 15-nucleotide-long pattern at random positions in these sequences.
    - Hide the patterns and find where they are inserted.
2. **Algorithm for Pattern Detection**:
    - Modify the frequent words problem to find the inserted pattern.
    - Concatenate all sequences and find the most frequent word.
    - The inserted pattern will appear ten times in the concatenated sequence.
3. **Experiment Modification**:
    - Insert the 15-nucleotide-long pattern with four random mutations.
    - This creates a (k,d) motif: a k-mer appearing in each sequence with at most d mutations.
4. **Biological Relevance**:
    - The problem relates to finding regulatory elements in DNA.
    - Focus on circadian clock genes.
5. **Biological Context**:
    - The circadian clock influences protein expression based on the time of day.
    - Plants depend heavily on circadian rhythms for photosynthesis, flowering, and frost resistance.
    - Three genes (CCA1, LCY, TOC1) manage the circadian behavior in plants.
        - CCA1, LCY, and TOC1 are regulatory proteins (a.k.a. transcription factors) control other genes by binding to short DNA fragments (transcription factor binding sites) in the upstream regions of these genes.
    - These genes bind to specific regions upstream of other genes to regulate them.
6. **Regulatory Protein Binding**:
    - Proteins like CCA1 bind to upstream regions of genes to control expression.
    - The goal is to find hidden messages indicating where these proteins bind.
7. **Formulating the Problem**:
    - Implanted Motif Problem: Given DNA sequences and integers k and d, find all (k,d) motifs.
        - Input: A set of strings Dna, and integers k (motif length) and d (maximal number of mismatches in a motif)
        - Output: All (k,d) - motifs in Dna.
        - 
        
        ```python
        MotifEnumeration(Dna, k,d)
        for each k-mer a in Dna
        	for each k-mer a' differenting from a by at most d mutations
        		if a' is a (k,d)-mer
        			output a'
        ```
        
        - Why this simple (albeit slow) algorithm work for finding real biological motifs?
            - MotifEnumeration assumes that EACH sequence has a k-mer similar to an (unknown) implanted pattern. This condition does no hold for noisy biological datasets.
8. **Solving the Problem**:
    - Explore all possible 4^k k-mers and check which represent (k,d)-motifs.
    - Compare sequences pairwise to find similarities due to implanted motifs.
    - Pairwise comparison may fail due to mutations; consider motif enumeration instead.
9. **Motif Enumeration Algorithm**:
    - Generate all possible mutations for each k-mer from sequences.
    - Check if mutated k-mers appear as (k,d)-mers in the sequences.
10. **Real Biological Problem**:
    - The model of implanting patterns does not fully reflect biological reality.
    - Some genes may not have the pattern implanted.
    - Develop scoring for motifs, even if some sequences lack the motif.

---

**Türkçe Çeviri: DNA'daki Düzenleyici Motifleri Bulmak İçin Algoritmalar**

1. **Oyun Tanıtımı**:
    - On rastgele dizi oluşturun.
    - Bu dizilere rastgele konumlarda 15 nükleotit uzunluğunda bir desen ekleyin.
    - Desenleri gizleyin ve nerede yerleştirildiklerini bulun.
2. **Desen Tespiti İçin Algoritma**:
    - Eklenen deseni bulmak için sık kullanılan kelimeler problemini değiştirin.
    - Tüm dizileri birleştirin ve en sık kullanılan kelimeyi bulun.
    - Eklenen desen, birleştirilmiş dizide on kez görünecektir.
3. **Deney Değişikliği**:
    - 15 nükleotit uzunluğundaki deseni dört rastgele mutasyon ile ekleyin.
    - Bu, her dizide en fazla d mutasyon ile görünen bir k-mer olan (k,d) motifini oluşturur.
4. **Biyolojik Alaka**:
    - Sorun, DNA'daki düzenleyici elementleri bulmakla ilgilidir.
    - Sirkadiyen saat genlerine odaklanın.
5. **Biyolojik Bağlam**:
    - Sirkadiyen saat, günün saatine bağlı olarak protein ifadesini etkiler.
    - Bitkiler, fotosentez, çiçeklenme ve dona dayanıklılık için sirkadiyen ritimlere büyük ölçüde bağımlıdır.
    - Üç gen (CCA1, LCY, TOC1) bitkilerde sirkadiyen davranışı yönetir.
    - Bu genler, diğer genleri düzenlemek için belirli bölgelerine bağlanır.
6. **Düzenleyici Protein Bağlanması**:
    - CCA1 gibi proteinler, genlerin yukarı akış bölgelerine bağlanarak ifadesini kontrol eder.
    - Amaç, bu proteinlerin bağlanmasını belirten gizli mesajları bulmaktır.
7. **Sorunun Formüle Edilmesi**:
    - Eklenmiş Motif Problemi: DNA dizileri ve k ve d tamsayıları verildiğinde, tüm (k,d) motiflerini bulun.
8. **Sorunun Çözülmesi**:
    - Tüm olası 4^k k-merleri keşfedin ve hangilerinin (k,d)-motiflerini temsil ettiğini kontrol edin.
    - Ekim motiflerine bağlı benzerlikleri bulmak için dizileri çiftler halinde karşılaştırın.
    - Çiftler halinde karşılaştırma, mutasyonlar nedeniyle başarısız olabilir; bunun yerine motif sayımını dikkate alın.
9. **Motif Sayım Algoritması**:
    - Dizilerden her k-mer için tüm olası mutasyonları üretin.
    - Mutasyona uğramış k-merlerin dizilerde (k,d)-mer olarak görünüp görünmediğini kontrol edin.
10. **Gerçek Biyolojik Sorun**:
    - Desenlerin eklenmesi modeli biyolojik gerçekliği tam olarak yansıtmaz.
    - Bazı genler desenin eklenmemiş olabilir.
    - Motifleri puanlamak için, bazı diziler motif içermese bile bir yöntem geliştirin.

# From Implanted Patterns to Regulatory Motifs (Part 2)

1. **Flaw in the Motif Enumeration Algorithm**:
    - Assumed the motif occurs in every string in the collection.
    - This assumption is not always true in biological applications.
2. **Alternative Approach**:
    - Assign a score to a given collection of k-mers chosen from the strings.
    - Represent the selected k-mers as a Motif matrix.
    - Indicate the most frequent nucleotide in each column with a capital letter, breaking ties arbitrarily.
    - Positions two and three in the Motif matrix are highly conserved, while position ten is the least conserved.
3. **Visualizing the Motif Matrix**:
    - Use a motif logo where nucleotide size correlates with frequency in the Motif matrix.
    - Construct a consensus string from the capital letters in each column of the Motif matrix to provide a candidate Motif.
4. **Objective**:
    - Choose k-mers from the strings to produce the most conserved Motif matrix.
    - Take the Consensus String as the desired Motif.
    - Define the score of the Motif matrix as the number of lowercase letters in the matrix.
    - Minimize this score to find the optimal k-mers.
    
    ```python
    Motif Finding Problem: Given a collection of strings, 
    find a set of k-mers, one from each string, that minimizes the score of the resulting motif.
    
    - Input: A collection of strings Dna and an integer k.
    - Output: A collection Motifs of k-mers, one from each string in Dna, minimizing Score(Motifs) among all possible choices of k-mers
    ```
    
5. **Brute Force Algorithm**:
    - Compute score of every possible choice of k-mers in Dna.
    - Consider every possible choice of k-mers to find a Motif matrix.
    - Take the collection of k-mers with the lowest score.
    - For t strings of length n, there are (n - k + 1)^t possibilities.
    - Scoring the matrix requires k * t steps.
    - Overall running time: O(n^t * k * t), impractical for real values of n and t. (TOO SLOW!!)
6. **Improving the Algorithm**:
    - Rethink the motif finding problem by choosing the consensus string first.
    - Then, find the Motif matrix that scores best against this consensus.
    - Compute the number of lowercase symbols in the motif matrix row by row.
    - The number of lowercase symbols in a row equals the number of symbols that don't match the consensus, known as the Hamming distance.
    - Score of the Motif matrix is the sum of Hamming distances between each string in the matrix and the consensus string.
7. **Equivalent Motif Finding Problem**:
    - Look for a pattern serving as the consensus string that minimizes the distance to motifs over all choices of motifs in the strings.
    - Focus on finding an optimal consensus string without searching through every possible choice of motifs.
    - 
    
    ```python
    Equivalent Motif Finding Problem: 
    Given a collection of strings, find a pattern and a collection of k-mers 
    (one from each string) that minimizes the distance between all possible patterns
    and all possible collections of k-mers.
    
    - Input: A collection of strings Dna and an integer k.
    - Output: A k-mer Pattern and a collection of k-mers Motifs, one from each string in Dna, 
    minimizing d(Pattern, Motifs) among all possible choices of Pattern and Motifs.
    ```
    

---

1. **Motif Sayım Algoritmasındaki Hata**:
    - Motifin her dizide bulunduğunu varsayıyordu.
    - Bu varsayım biyolojik uygulamalarda her zaman doğru değildir.
2. **Alternatif Yaklaşım**:
    - Dizilerden seçilen k-mer koleksiyonuna puan atayın.
    - Seçilen k-mer'leri bir Motif matrisi olarak temsil edin.
    - Her sütundaki en sık görülen nükleotidi büyük harfle belirtin, eşitlik durumunda rastgele kırın.
    - Motif matrisindeki iki ve üç numaralı pozisyonlar oldukça korunmuşken, on numaralı pozisyon en az korunmuş pozisyondur.
3. **Motif Matrisinin Görselleştirilmesi**:
    - Motif matrisinde nükleotid büyüklüğünün frekansla orantılı olduğu bir motif logosu kullanın.
    - Motif matrisi sütunlarındaki büyük harflerden bir konsensus dizisi oluşturun.
4. **Amaç**:
    - Dizilerden en korunmuş Motif matrisini oluşturacak k-mer'leri seçin.
    - Konsensus Dizisini istenen Motif olarak alın.
    - Motif matrisinin puanını matristeki küçük harflerin sayısı olarak tanımlayın.
    - Bu puanı en aza indirerek en uygun k-mer'leri bulun.
5. **Kaba Kuvvet Algoritması**:
    - Bir Motif matrisi bulmak için her olası k-mer seçeneğini göz önünde bulundurun.
    - En düşük puana sahip k-mer koleksiyonunu alın.
    - Uzunluğu n olan t dizi için (n - k + 1)^t olasılık vardır.
    - Matrisin puanlanması k * t adım gerektirir.
    - Toplam çalışma süresi: O(n^t * k * t), n ve t'nin gerçek değerleri için pratik değildir.
6. **Algoritmayı Geliştirme**:
    - Motif bulma sorununu konsensus dizisini önce seçerek yeniden düşünün.
    - Ardından, bu konsensusa karşı en iyi puanı alan Motif matrisini bulun.
    - Motif matrisindeki küçük harflerin sayısını satır satır hesaplayın.
    - Bir satırdaki küçük harflerin sayısı, konsensusa uymayan sembollerin sayısına eşittir ve Hamming mesafesi olarak bilinir.
    - Motif matrisinin puanı, matristeki her dizinin konsensus dizisiyle olan Hamming mesafelerinin toplamıdır.
7. **Eşdeğer Motif Bulma Sorunu**:
    - Tüm dizilerdeki motiflere olan mesafeyi en aza indiren konsensus dizisi olarak hizmet edecek bir deseni arayın.
    - Her olası motif seçeneğini aramadan optimal konsensus dizisini bulmaya odaklanın.

# From Implanted Patterns to Regulatory Motifs (Part 3)

**Median String Problem: A New Approach to Motif Finding**

1. **Defining Distance Between k-mers and Longer Strings**:
    - Compare the k-mer to the first k-mer in the longer string.
    - Calculate the distance and move through the string to find the minimal distance.
    - The minimal distance between the k-mer and the longer string is the distance between a pattern and the string.
2. **Distance Between a k-mer and a Set of Strings**:
    - Sum the distances between the pattern and each string in the set.
    - For example, for a pattern "AAA" and a set of strings, compute the distance with every string and sum up the distances. The result might be 5.
    - The median string for the set of strings is the k-mer pattern that minimizes the distance between the pattern and the DNA over all possible k-mers.
3. **Median String Problem**:
    - Another equivalent motif finding problem.
    - Search for a k-mer pattern minimizing the distance between this pattern and the set of strings DNA among all possible k-mers.
    - Simple algorithm: Try all possible k-mers and find the one with minimal distance to DNA.
    - Running time: $4^k \times n \times t \times k$, where t is the number of sequences and n is their length.
    - This algorithm is still exponential but practical for small k (usually less than 15).
4. **Dramatic Improvement**:
    - Started with a slow brute force algorithm for the motif finding problem.
    - Switched to the median string problem with a much faster algorithm.
    - This change of perspective greatly improved the solution.
5. **Greedy Motif Search**:
    - Despite improvements, the median string problem can still be slow for long motifs.
    - Introduce a greedy algorithm to solve the motif finding problem.
    - Construct the consensus string and count matrix, transform it into a profile matrix with nucleotide frequencies in each column.
    - View these frequencies as probabilities, akin to a four-sided biased die.
6. **Probability of Generating DNA Strings**:
    - Calculate the probability of generating a given DNA string from the profile matrix by multiplying corresponding elements.
    - The closer a string is to the consensus string, the higher the probability of generating it.
7. **Profile-most Probable k-mer**:
    - The k-mer with the highest probability among all k-mers in the sequence.
    - Start from the first k-mer in the string, compute probability, and record it.
    - Continue until the matrix is filled and select the highest probability.
8. **Greedy Motif Search Algorithm**:
    - Start with i-1 motifs from the first i-1 sequences.
    - Form a profile of motifs from these sequences.
    - Select the profile-most probable k-mer in the i-th sequence.
    - Iterate this process to extend the set of motifs.

---

**Türkçe Çeviri: Medyan Dizi Problemi: Motif Bulmada Yeni Bir Yaklaşım**

1. **k-mer'ler ile Uzun Diziler Arasındaki Mesafeyi Tanımlama**:
    - k-mer'i daha uzun dizideki ilk k-mer ile karşılaştırın.
    - Mesafeyi hesaplayın ve en küçük mesafeyi bulmak için dizi boyunca ilerleyin.
    - k-mer ile uzun dizi arasındaki en küçük mesafe, bir desen ile dizi arasındaki mesafedir.
2. **k-mer ile Dizi Kümesi Arasındaki Mesafe**:
    - Desen ile her dizi arasındaki mesafeleri toplayın.
    - Örneğin, "AAA" deseni ve bir dizi kümesi için, her dizi ile mesafeyi hesaplayın ve mesafeleri toplayın. Sonuç 5 olabilir.
    - Dizi kümesi için medyan dizi, tüm olası k-mer'ler arasında desen ile DNA arasındaki mesafeyi en aza indiren k-mer desenidir.
3. **Medyan Dizi Problemi**:
    - Bir başka eşdeğer motif bulma sorunu.
    - Bu desen ile dizi kümesi DNA arasındaki mesafeyi en aza indiren bir k-mer desenini arayın.
    - Basit algoritma: Tüm olası k-mer'leri deneyin ve DNA'ya olan mesafenin minimum olduğu k-mer'i bulun.
    - Çalışma süresi: $4^k \times n \times t \times k$, burada t dizi sayısı ve n uzunluklarıdır.
    - Bu algoritma hala üstel ancak küçük k (genellikle 15'ten az) için pratiktir.
4. **Çarpıcı İyileştirme**:
    - Yavaş bir kaba kuvvet algoritması ile motif bulma problemine başladık.
    - Çok daha hızlı bir algoritma ile medyan dizi problemine geçtik.
    - Bu bakış açısı değişikliği çözümü büyük ölçüde iyileştirdi.
5. **Açgözlü Motif Arama**:
    - İyileştirmelere rağmen, medyan dizi problemi uzun motifler için hala yavaş olabilir.
    - Motif bulma sorununu çözmek için açgözlü bir algoritma tanıtın.
    - Konsensus dizisini ve sayım matrisini oluşturun, bunu her sütunda nükleotid frekanslarına sahip profil matrisine dönüştürün.
    - Bu frekansları dört taraflı yanlı bir zar gibi olasılıklar olarak görün.
6. **DNA Dizileri Üretme Olasılığı**:
    - Profil matrisindeki karşılık gelen elemanları çarparak verilen bir DNA dizisini üretme olasılığını hesaplayın.
    - Bir dizi konsensus dizisine ne kadar yakınsa, onu üretme olasılığı o kadar yüksektir.
7. **Profil-En Olası k-mer**:
    - Dizideki tüm k-mer'ler arasında en yüksek olasılığa sahip k-mer.
    - Dizideki ilk k-mer'den başlayın, olasılığı hesaplayın ve kaydedin.
    - Matris dolana kadar devam edin ve en yüksek olasılığı seçin.
8. **Açgözlü Motif Arama Algoritması**:
    - İlk i-1 diziden i-1 motif ile başlayın.
    - Bu dizilerden motiflerin profilini oluşturun.
    - i. dizide profil-en olasılı k-mer'i seçin.
    - Motif kümesini genişletmek için bu işlemi yineleyin.

---

---

<aside>
❓ **Exercise Break:** What is the expected number of occurrences of a 9-mer in 500 random DNA strings, each of length 1000? Assume that the sequences are formed by selecting each nucleotide (A, C, G, T) with the same probability (0.25).

**Note:** Express your answer as a decimal; allowable error = 0.0001

</aside>

- Number of possible 9-mers in one DNA string:
    - Each DNA string is 1000 bases long. A 9-mer can start as positions 1 through 992 (since 1000 - 9 +1 = 992)
- Total number of possible 9-mers in 500 DNA string:
    - 500 * 992 = 49600
- Probability of specific 9-mer appearing in a given position:
    - = 49600 * (0,25)^9
    - = 49600 * 0,000003814697265625
    - = 0,189208984375

---
