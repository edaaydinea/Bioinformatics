# Welcome!

## Video

- This course will focus on how to find these messages hidden within DNA.

## Reading: Course Details

- an Honors Track is designed for learners who wish to  implement the algorithms encountered in the interactive text by solving  a series of Code Challenges.

[BioinformaticsAlgorithms](http://bioinformaticsalgorithms.com/)

# Week 1

## Where in the genome does DNA replication begin?

### A Journey of a Thousand Miles

**Genome replication** is one of the most important tasks carried out in the cell. Before a cell can divide, it must first replicate its genome so that each of the two daughter cells inherits its own copy. In 1953, James Watson and Francis Crick completed their [landmark paper](https://www.nature.com/articles/171737a0) on the DNA double helix with a now-famous phrase:

> It has not escaped our notice that the specific pairing we have postulated immediately suggests a possible copying mechanism for the genetic material.
> 

They conjectured that the two strands of the parent DNA molecule unwind during replication, and then each parent strand acts as a template for the synthesis of a new strand. As a result, the replication process begins with a pair of complementary strands of DNA and ends with two pairs of complementary strands, as shown in the figure below.

Although this figure successfully models DNA replication on a simple level, the details of replication turned out to be much more intricate than Watson and Crick imagined; as we will see, an astounding amount of molecular logistics is required to ensure DNA replication.

![semiconservative_replication.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/2e48dbc0-c8ca-47ed-846d-3a1864ba185d/c0071a38-7c52-441a-91a6-01c98c033dff/semiconservative_replication.png)

!http://bioinformaticsalgorithms.com/images/Replication/semiconservative_replication.png

**Figure:** A naive view of replication. Nucleotides adenine (A) and thymine (T) are complements of each other, as are cytosine (C) and guanine (G). Complementary nucleotides bind to each other in DNA.

At first glance, a computer scientist might not imagine that these details have any computational relevance. To mimic the process in the above figure algorithmically, we only need to take a string representing the genome and return a copy of it! Yet if we take the time to review the underlying biological process, we will be rewarded with new algorithmic insights into analyzing replication. Replication begins in a genomic region called the **replication origin** (denoted *ori*) and is carried out by molecular copy machines called **DNA polymerases**.

Locating *ori* presents an important task not only for understanding how cells replicate but also for various biomedical problems. For example, some **gene therapy** methods use genetically engineered mini-genomes, which are called **viral vectors** because they are able to penetrate cell walls (just like real viruses). Viral vectors carrying artificial genes have been used in agriculture, such as to engineer frost-resistant tomatoes and pesticide-resistant corn. In 1990, gene therapy was first successfully performed on humans when it saved the life of a four-year-old girl suffering from Severe Combined Immunodeficiency Disorder; the girl had been so vulnerable to infections that she was forced to live in a sterile environment.

The idea of gene therapy is to intentionally infect a patient who lacks a crucial gene with a viral vector containing an artificial gene that encodes a therapeutic protein. Once inside the cell, the vector replicates and eventually produces many copies of the therapeutic protein, which in turn treats the patient’s disease. To ensure that the vector actually replicates inside the cell, biologists must know where *ori* is in the vector’s genome and ensure that the genetic manipulations that they perform do not affect it.

In the following problem, we assume that a genome has a single *ori* and is represented as a **DNA string**, or a string of nucleotides from the four-letter alphabet {A, C, G, T}.

**Finding Origin of Replication Problem:**

- **Input**: A DNA string *Genome*.
- **Output**: The location of *ori* in *Genome*.

**STOP and Think:** Does the Finding Origin of Replication Problem represent a clearly stated computational problem? (On "STOP and Think" questions, we encourage you to interact with other learners in the discussion forum below.)

Although the Finding *ori* Problem asks a legitimate biological question, it does not present a well-defined computational problem. Indeed, biologists would immediately plan an experiment to locate *ori*: for example, they might delete various short segments from the genome in an effort to find a segment whose deletion stops replication. Computer scientists, on the other hand, would shake their heads and demand more information before they can even start thinking about the problem.

Why should biologists care what computer scientists think? Computational methods are now the only realistic way to answer many questions in modern biology. First, these methods are much faster than experimental approaches; second, the results of many experiments cannot be interpreted without computational analysis. In particular, existing experimental approaches to *ori* prediction are rather time consuming. As a result, *ori* has only been experimentally located in a handful of species. Thus, we would like to design a computational approach to find *ori* so that biologists are free to spend their time and money on other tasks.

### Hidden Messaged in the Replication Origin

In the rest of this chapter, we will focus on the relatively easy case of finding *ori* in bacterial genomes, most of which consist of a single circular chromosome. Research has shown that the region of the bacterial genome encoding *ori* is typically a few hundred nucleotides long. Our plan is to begin with a bacterium in which *ori* is known, and then determine what makes this genomic region special in order to design a computational approach for finding *ori* in other bacteria. Our example is *Vibrio cholerae*, the pathogenic bacterium that causes cholera; here is the nucleotide sequence appearing in the *ori* of *Vibrio cholerae*:

atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaac
ctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca
cggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgactt
gtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggatt
acgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttagga
tagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaat
tgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaag
atcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtt
tccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc

How does the bacterial cell know to begin replication exactly in this short region within the much larger *Vibrio cholerae* chromosome, which consists of 1,108,250 nucleotides? There must be some “hidden message” in the *ori* region ordering the cell to begin replication here. Indeed, we know that the initiation of replication is mediated by ***DnaA***, a protein that binds to a short segment within the *ori* known as a ***DnaA* box**. You can think of the *DnaA* box as a message within the DNA sequence telling the *DnaA* protein: “bind here!” The question is how to find this hidden message without knowing what it looks like in advance—can you find it? In other words, can you find something that stands out in *ori*? This discussion motivates the following problem.

**Hidden Message Problem:** *Find a “hidden message” in the replication origin.*

- **Input**: A string *Text* (representing the replication origin of a genome).
- **Output**: A hidden message in *Text*.

**STOP and Think**: Does the Hidden Message Problem represent a clearly stated computational problem?

## **Hidden messages in "The Gold-Bug"**

Although the Hidden Message Problem poses a legitimate intuitive question, it again makes absolutely no sense to a computer scientist because the notion of a “hidden message” is not precisely defined. The *ori* region of *Vibrio cholerae* is currently just as puzzling as the parchment discovered by William Legrand in Edgar Allan Poe's story "The Gold-Bug". Written on the parchment was

53‡‡†305))6·;4826)4‡.)4‡);806·;48†8^60))85;161;:‡·8†83(88)5·†;46(;88·96·?;8)·‡(;485);5·†2:·‡(;4956·2(5·—4)8^8·;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806·81(‡9;48;(88;4(‡?34;48)4‡;1‡(;:188;‡?;

Upon seeing the parchment, the narrator remarks, "Were all the jewels of Golconda awaiting me upon my solution of this enigma, I am quite sure that I should be unable to earn them." Legrand retorts, "It may well be doubted whether human ingenuity can construct an enigma of the kind which human ingenuity may not, by proper application, resolve." He reasons that the three consecutive symbols **;48** appear with surprising frequency on the parchment.

```
53‡‡†305))6·;4826)4‡.)4‡);806·;48†8^60))85;161;:‡·8
†83(88)5·†;46(;88·96·?;8)·‡(;485);5·†2:·‡(;4956·2(5
·—4)8^8·;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4
)485†528806·81(‡9;48;(88;4(‡?34;48)4‡;1‡(;:188;‡?;
```

Legrand had already deduced that the pirates spoke English; he therefore assumed that the high frequency of **;48** implied that it encodes the most frequent English word, **THE**. Substituting **;** for **T**, **4** for **H**, and **8** for **E**, Legrand had a slightly easier text to decipher (shown below), which would eventually lead him to the buried treasure. Can you decode this message too?

```
53‡‡†305))6·THE26)H‡.)H‡)TE06·THE†E^60))E5T161T:‡·E
†E3(EE)5·†TH6(TEE·96·?TE)·‡(THE5)T5·†2:·‡(TH956·2(5
·—H)E^E·TH0692E5)T)6†E)H‡‡T1(‡9THE0E1TE:E‡1THE†E5TH
)HE5†52EE06·E1(‡9THET(EETH(‡?3HTHE)H‡T1‡(T:1EET‡?T
```

## **Counting Words**

Operating under the assumption that DNA is a language of its own, let's borrow Legrand's method and see if we can find any surprisingly frequent "words" within the *ori* of *Vibrio cholerae*. We have added reason to look for frequent words in the *ori* because for various biological processes, certain nucleotide strings often appear surprisingly often in small regions of the genome. This is often because certain proteins can only bind to DNA if a specific string of nucleotides is present, and if there are more occurrences of the string, then it is more likely that binding will successfully occur. (It is also less likely that a mutation will disrupt the binding process.)

For example, **ACTAT** is a surprisingly frequent substring of ACA**ACTAT**GCAT**ACTAT**CGGGA**ACTAT**CCT.

We will use the term ***k*-mer** to refer to a string of length *k* and define *Count*(*Text*, *Pattern*) as the number of times that a *k*-mer *Pattern* appears as a substring of *Text*. Following the above example,

*Count*(ACA**ACTAT**GCAT**ACTAT**CGGGA**ACTAT**CCT, ACTAT) = 3.

We note that *Count*(CG**ATATA**TCC**ATA**G, **ATA**) is equal to 3 (not 2) since we should account for overlapping occurrences of *Pattern* in *Text*.

To compute *Count*(*Text*, *Pattern*), our plan is to “slide a window” down *Text*, checking whether each *k*-mer substring of *Text* matches *Pattern*. We will therefore refer to the *k*-mer starting at position *i* of *Text* as *Text*(*i*, *k*). Throughout this book, we will often use **0-based indexing**, meaning that we count starting at 0 instead of 1. In this case, *Text* begins at position 0 and ends at position |*Text*| − 1 (|*Text*| denotes the number of symbols in *Text*). For example, if *Text* = GACCATACTG, then *Text*(4, 3) = ATA. Note that the last *k*-mer of *Text* begins at position |*Text*| − *k*, e.g., the last 3-mer of GACCATACTG starts at position 10 − 3 = 7. This discussion results in the following pseudocode for computing *Count*(*Text*, *Pattern*).

**Important Note:** We do not assume that you know how to program; we only expect you to program if you are following the Honors Track. However, we do need to communicate the computational methods used in modern biology. To do so, we will use the language of **pseudocode**, which is more precise than human language. Please click [here](http://bioinformaticsalgorithms.com/excerpt/Pseudocode.pdf) for an overview of pseudocode.

```
PatternCount(Text,Pattern)
        count ← 0
        for i ← 0 to |Text| − |Pattern|
            ifText(i, |Pattern|) = Pattern
            count ←count + 1
        returncount
```

If you are following the Honors Track, then you should complete the "Code Challenge" assessments you encounter. If not, there is no need to learn to program or complete Code Challenges. If you haven't programmed before and are interested in learning how, we suggest our ["Biology Meets Programming"](http://coursera.org/learn/bioinformatics) course.

**Code Challenge:** Implement **PatternCount** (reproduced below).

**Input:** Strings *Text* and *Pattern*.

**Output:** *Count*(*Text*, *Pattern*).

```
PatternCount(Text,Pattern)
 count ← 0
 for i ← 0 to |Text| − |Pattern|
 ifText(i, |Pattern|) = Pattern
    count ←count + 1
  returncount
```

Some notes on how code challenges work:

1. You should write your code implementing **PatternCount** first; you can choose any programming language you like.
2. When you click "Download Dataset", you will receive a randomized dataset. In this problem, the dataset will contain two lines: the first line contains *Text*, and the second line contains *Pattern*. In general, the "Sample Input" section shows how
3. Run your program (in the programming language of your choice) on the dataset, and then return the **output** of your program in the text field below. (Please do not enter your code in the browser.)
4. There is a time limit on each problem to ensure that your code is sufficiently efficient to return the correct output quickly.
5. You can see how you should format your answer by looking at the sample output.
6. You have unlimited attempts to answer the question, but each time you click "Try Again", you will need to download a *new* dataset.
7. We also provide additional *small* datasets (see link below) to help you debug your code.

**Note:** We also provide additional *small* datasets (click below) to help you debug your code.

[Debug Datasets](https://bioinformaticsalgorithms.com/data/debugdatasets/replication/PatternCount.zip)

**Sample Input:**

```
GCGCG
GCG
```

**Sample Output:**

```
2
```

You have an unlimited number of attempts.

**Time limit:**

5 mins

```python
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
```

## **The Frequent Words Problem**

We say that *Pattern* is a **most frequent *k*-mer** in *Text* if it maximizes *Count*(*Text*, *Pattern*) among all *k*-mers. You can see that **ACTAT** is a most frequent 5-mer of ACA**ACTAT**GCAT**ACTAT**CGGGA**ACTAT**CCT, and **ATA** is a most frequent 3-mer of CG**ATATA**TCC**ATA**G.

**STOP and Think**: Can a string have multiple most frequent *k*-mers?

We now have a rigorously defined computational problem.

**Frequent Words Problem:** *Find the most frequent k-mers in a string.*

- **Input**: A string *Text* and an integer *k*.
- **Output:** All most frequent *k*mers in *Text*.

A straightforward algorithm for finding the most frequent *k*-mers in a string *Text* checks all *k*-mers appearing in this string (there are |*Text*| − *k* + 1 such *k*-mers) and then computes how many times each *k*-mer appears in *Text*. To implement this algorithm, called **FrequentWords**, we will need to generate an array *Count*, where *Count*(*i*) stores *Count*(*Text*, *Pattern*) for *Pattern* = *Text*(*i*, *k*) (see figure below).

https://ucarecdn.com/8367f24c-c989-4ad1-b5a4-9ab2dafa3a10/

**Figure:** The array *Count* for *Text* = ACTGACTCCCACCCC and *k* = 3. For example, *Count*(0) = *Count*(4) = 2 because ACT (shown in boldface) appears twice in *Text*.

The pseudocode for **FrequentWords** is shown below.

```sql
FrequentWords(Text,k)
FrequentPatterns← an empty set
fori ← 0 to |Text| −k
Pattern ← thek-merText(i,k)
Count(i) ←PatternCount(Text,Pattern)
maxCount ← maximum value in arrayCount
fori ← 0 to |Text| −k
ifCount(i) =maxCount
            addText(i, k) toFrequentPatterns
    remove duplicates fromFrequentPatterns
returnFrequentPatterns
```

Although **FrequentWords** finds most frequent *k*-mers, it is not very efficient. Each call to **PatternCount**(*Text*, *Pattern*) checks whether the *k*-mer *Pattern* appears in position 0 of *Text*, position 1 of *Text*, and so on. Since each *k*-mer requires |*Text*| − k + 1 such checks, each one requiring as many as *k* comparisons, the overall number of steps of **PatternCount**(*Text*, *Pattern*) is (|*Text*| − *k* + 1) · *k*. Furthermore, **FrequentWords** must call **PatternCount** |*Text*| − *k* + 1 times (once for each *k*-mer of *Text*), so that its overall number of steps is (|*Text*| − *k* + 1) · (|*Text*| − *k* + 1) · *k*. To simplify the matter, computer scientists often say that the runtime of ﻿**FrequentWords** has an upper bound of |*Text*|2 · *k* steps and refer to the **complexity** of this algorithm as O(|*Text*|2 · *k*). For more details, see "DETOUR: Big-O Notation" in the [print companion](http://bioinformaticsalgorithms.com/).

If |*Text*| and *k* are small, as is the case when looking for *DnaA* boxes in the typical bacterial *ori*, then an algorithm with running time of O(|*Text*|2 · *k*) is perfectly acceptable. But once we find some new biological application requiring us to solve the Frequent Words Problem for a very long *Text*, we will quickly run into trouble. What can we do instead?
