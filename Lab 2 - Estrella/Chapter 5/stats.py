"""
  PROBLEM 1
  
"""
from collections import Counter


def mean(numbers):
       if not numbers:
        raise ValueError("The list of numbers is empty.")
    return sum(numbers) / len(numbers)


def median(numbers):
        if not numbers:
        raise ValueError("The list of numbers is empty.")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    midpoint = n // 2

    if n % 2 == 1:  # Odd number of elements
        return sorted_numbers[midpoint]
    else:  # Even number of elements
        return (sorted_numbers[midpoint - 1] + sorted_numbers[midpoint]) / 2


def mode(numbers):
        if not numbers:
        raise ValueError("The list of numbers is empty.")

    count = Counter(numbers)
    max_frequency = max(count.values())
    modes = [key for key, val in count.items() if val == max_frequency]

    # If multiple modes exist, return the first one
    return modes[0]


# Example usage for testing
if __name__ == "__main__":
    sample_numbers = [1, 2, 2, 3, 4]
    print("Mean:", mean(sample_numbers))
    print("Median:", median(sample_numbers))
    print("Mode:", mode(sample_numbers))
