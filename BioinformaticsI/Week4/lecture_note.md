# How Rolling Dice Helps Us Find Regulatory Motifs (Part1)

1. **Randomized Motif Search Algorithm Overview:**
    - The algorithm involves iterating between finding a Profile given Motifs and finding Motifs given a Profile.
    - Iteration continues until the score of the motifs improves no further.
    - Initial motifs are randomly chosen, which might seem ineffective, but the iterative process can reveal meaningful patterns.
    
    ```jsx
    RandomizedMotifSearch(Dna, k, t)
    	randomly select k-mers Motifs = (Motif1, ... Motif1) in each string from DNA
    	bestMotifs <- Motifs
    	while forever
    		Profile <- Profile(Motifs)
    		Motifs <- Motifs(Profile, Dna)
    		if Score(Motifs) < Score(bestMotrifs)
    			bestMotifs <- Motifs
    		else
    			return(bestMotifs)
    ```
    
2. **Algorithm Mechanics:**
    - Construct a Profile from the randomly selected Motifs.
    - Determine the most probable k-mers in each DNA sequence based on the Profile.
    - Iteratively update motifs using the Profile and repeat the process.
3. **Effectiveness of Randomized Search:**
    - Randomly selected motifs might not initially reveal correct motifs due to their randomness.
    - However, biased profiles from implanted motifs can lead to correct motifs through iteration.
    - Even random starts can lead to correct motifs if the process is repeated enough times.
4. **Example Illustration:**
    - In a DNA sequence example with implanted motifs, the algorithm initially misses most motifs but can find correct ones through iterative refinement.
    - The profile matrix becomes biased towards the implanted motifs due to the presence of accurate k-mers.
5. **Biological Application:**
    - Applied to understanding tuberculosis (TB) by identifying regulatory motifs involved in gene expression changes under hypoxic conditions.
    - DNA array experiments identified genes activated in hypoxia, aiming to discover the regulatory motif controlling these genes.
6. **Algorithm Comparisons:**
    - Randomized Motif Search vs. Median String Problem:
        - Median String Problem is limited by computational complexity for longer motifs.
        - Randomized Motif Search can handle longer motifs and can provide similar results.
7. **Motif Entropy:**
    - Entropy measures the variability of motifs.
    - Construct Profile Matrix for motifs, where entropy is calculated based on nucleotide distributions in columns.
    - Lower entropy indicates a more conserved motif.
8. **Motif Logo:**
    - Represents the height of each nucleotide in a motif column based on its frequency.
    - Used to visualize the conservation and variability of motifs.
9. **Evaluation of Results:**
    - The randomized motif search captured parts of the desired motifs but missed some details.
    - Further improvement in algorithms is needed to refine regulatory motif finding.

# How Rolling Dice Helps Us Find Regulatory Motifs (Part2)

### Gibbs Sampling for Motif Finding

1. **Overview of Gibbs Sampling:**
    - Gibbs Sampling is a more cautious approach compared to Randomized Motif Search.
    - Unlike Randomized Motif Search, which can change all motifs in each iteration, Gibbs Sampling updates only one motif at a time.
2. **Algorithm Process:**
    - Start by randomly selecting motifs from DNA sequences.
    - Remove one motif and the corresponding sequence from consideration.
    - Construct a Count Matrix from the remaining motifs, then build a Profile Matrix from this Count Matrix.
    - Calculate the probability of all k-mers in the removed sequence based on the Profile Matrix.
    - Use these probabilities to roll a die with sides proportional to the computed probabilities, determining the new position of the motif in the removed sequence.
3. **Iteration:**
    - Repeat the process of removing one motif, updating the Profile Matrix, and rolling the die to place the motif in the removed sequence.
    - Continue iterating until motifs improve or a set number of iterations (e.g., 100,000) are reached.
4. **Detailed Steps:**
    - **Initialization:** Randomly select k-mers from each sequence.
    - **Motif Removal:** Choose one k-mer from a sequence (Sequence*) and remove it.
    - **Profile Construction:** Create a Profile Matrix from the remaining k-mers.
    - **Probability Calculation:** Compute the probability of each k-mer position in the removed sequence.
    - **Die Rolling:** Use a die weighted by these probabilities to select a new position for the removed k-mer.
    - **Iteration:** Update the sequence with the new position and repeat the process.
5. **Example and Considerations:**
    - If most probabilities are zero, practical considerations suggest giving small probabilities to unlikely events to avoid issues similar to rolling a one-sided die.
    - Historical reference to Oliver Cromwell’s warning highlights the need to avoid absolute probabilities (0 and 1) in statistical models.
6. **Final Notes:**
    - Gibbs Sampling is designed to explore the solution space more carefully than Randomized Motif Search, potentially leading to better convergence on the correct motifs.

# How Rolling Dice Helps Us Find Regulatory Motifs (Part3)

### Addressing Zeroes in Randomized Algorithms

1. **Issue with Zeroes:**
    - Randomized algorithms struggle with zeroes in probability matrices.
    - Zeroes can occur when an event is not observed in a sample, leading to an empirical probability of zero, which does not reflect the true probability.
2. **Laplace's Solution:**
    - Laplace’s rule of succession helps address this issue.
    - By assuming the existence of additional, unobserved events, Laplace suggested adding pseudocounts to avoid zero probabilities.
    - For instance, adding 1 to each entry in the profile matrix to account for unobserved events.
3. **Applying Laplace's Rule:**
    - **Profile Matrix Update:** Add 1 to every entry in the count matrix, updating the profile matrix and probabilities.
    - **Example:** Instead of rolling a one-sided die, a seven-sided die is used after applying Laplace’s rule.
4. **Gibbs Sampling with Pseudocounts:**
    - **Process:**
        - Randomly select motifs and remove one sequence.
        - Construct the Count Matrix and apply pseudocounts (adding 1s).
        - Update the Profile Matrix and compute probabilities.
        - Roll a seven-sided die to select a new motif position.
    - **Iterations:** Repeat the process, iterating until motifs improve or a set number of iterations is reached.
5. **Success of Gibbs Sampling:**
    - With pseudocounts, Gibbs Sampling can successfully find motifs, even capturing implanted motifs in a few iterations.
    - Example: After three iterations, Gibbs Sampling almost captures the correct motifs, demonstrating its effectiveness in identifying the correct motif despite initial randomness.
6. **Challenges with Complex Motifs:**
    - For motifs with many mutations or complex patterns, finding the exact motif can be nearly impossible.
    - Random motifs may compete with real motifs, making detection difficult in long DNA strings.
7. **Alternative Approach - ChIP-sequencing:**
    - **ChIP-sequencing Technique:** Reduces the length of DNA strings to focus on smaller areas, improving the chances of finding elusive motifs.
    - By narrowing the search area, ChIP-sequencing enhances statistical power and facilitates the identification of regulatory motifs.
8. **Conclusion:**
    - Randomized algorithms, including Gibbs Sampling, can effectively find motifs when zero probabilities are addressed using techniques like pseudocounts.
    - For complex motifs, techniques like ChIP-sequencing are used to improve detection by reducing the search space.