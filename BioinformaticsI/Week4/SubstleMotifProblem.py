def probability_of_capturing_at_least_one(n, m, k, implanted_length):
    # Number of possible positions for a m-mer in a string of length n
    num_positions = n - m + 1
    
    # Probability of not capturing the implanted 15-mer in a single m-mer
    p_not_capture = 1 - 1 / num_positions
    
    # Probability that none of the k selected m-mers capture the implanted 15-mer
    p_none = p_not_capture ** k
    
    # Probability of capturing at least one m-mer
    p_at_least_one = 1 - p_none
    
    return p_at_least_one

# Example usage
n = 600  # Length of each DNA string
m = 15   # Length of the 15-mer
k = 10   # Number of randomly selected 15-mers
implanted_length = 15  # Length of the implanted sequence

# Calculate the probability
probability = probability_of_capturing_at_least_one(n, m, k, implanted_length)
print(f"Probability of capturing at least one implanted {implanted_length}-mer: {probability:.6f}")
