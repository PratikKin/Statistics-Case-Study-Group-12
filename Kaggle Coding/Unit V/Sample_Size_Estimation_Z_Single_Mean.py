import numpy as np
import scipy.stats as stats

def calculate_sample_size(population_std, margin_of_error, alpha):
    # Z-score corresponding to the desired confidence level
    z_tab = stats.norm.ppf(1 - alpha)

    # Calculate sample size using the formula
    required_sample_size = ((z_tab * population_std) / margin_of_error)**2

    return int(np.ceil(required_sample_size))  # Round up to ensure a sufficient sample size

# Example usage:
population_std = 40.70793   # Replace with the known population standard deviation
margin_of_error = 2   # Replace with the desired margin of error
confidence_level = 0.95  # Replace with the desired confidence level (e.g., 0.95 for 95%)

sample_size = calculate_sample_size(population_std, margin_of_error, confidence_level)
print(f"Estimated sample size: {sample_size}")
