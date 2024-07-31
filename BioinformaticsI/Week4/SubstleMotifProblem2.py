from scipy.special import comb

def probability_of_capturing_at_least_two(n, m, k):
    num_positions = n - m + 1
    
    # Probability of capturing a specific implanted 15-mer with one 15-mer
    p_capture = 1 / num_positions
    
    # Probability of not capturing the implanted 15-mer with one 15-mer
    p_not_capture = 1 - p_capture
    
    # Probability of capturing exactly 0 or 1 implanted 15-mers out of k
    p_0 = p_not_capture ** k
    p_1 = k * (p_not_capture ** (k - 1)) * p_capture
    
    # Probability of capturing at least 2 implanted 15-mers
    p_at_least_two = 1 - p_0 - p_1
    
    return p_at_least_two

# Example usage
n = 600  # Length of each DNA string
m = 15   # Length of the 15-mer
k = 10   # Number of randomly selected 15-mers

# Calculate the probability
probability = probability_of_capturing_at_least_two(n, m, k)
print(f"Probability of capturing at least two implanted {m}-mers: {probability:.6f}")
