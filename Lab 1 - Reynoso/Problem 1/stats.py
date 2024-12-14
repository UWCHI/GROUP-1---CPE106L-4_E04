# stats.py: A module for basic statistical functions

def mean(numbers):
    """Returns the mean (average) of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    """Returns the median of a list of numbers."""
    numbers.sort()  # Sort the list
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2  # Average of two middle numbers
    else:
        return numbers[mid]  # Middle number

def mode(numbers):
    """Returns the mode of a list of numbers."""
    freq = {}  # Dictionary to count occurrences
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    for num, count in freq.items():
        if count == max_count:
            return num  # Return the first mode found
