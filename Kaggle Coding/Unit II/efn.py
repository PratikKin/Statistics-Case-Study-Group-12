import numpy as np
from scipy.stats import norm

def z_test_for_proportion(p, p_0, n, alternative="two-sided"):
  z = (p - p_0) / np.sqrt(p_0 * (1 - p_0) / n)

  if alternative == "two-sided":
    p_value = 1 - norm.cdf(z) * 2
  elif alternative == "less":
    p_value = norm.cdf(-z)
  elif alternative == "greater":
    p_value = norm.cdf(z)
  else:
    raise ValueError("Invalid alternative hypothesis.")

  return z, p_value

# Example usage:

p = 0.72
p_0 = 0.60
n = 100
alternative = "two-sided"

z, p_value = z_test_for_proportion(p, p_0, n, alternative)

print("Test statistic:", z)
print("P-value:", p_value)

