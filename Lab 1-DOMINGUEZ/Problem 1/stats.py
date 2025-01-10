"""
Module for statistical calculations.
"""
def mean(numbers):
    """Calculate the mean (average) of a list of numbers."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculate the median of a list of numbers."""
    if len(numbers) == 0:
        return 0
    numbers.sort()
    if len(numbers) % 2 == 0:
        mid1 = len(numbers) // 2
        mid2 = mid1 - 1
        return (numbers[mid1] + numbers[mid2]) / 2
    else:
        mid = len(numbers) // 2
        return numbers[mid]

def mode(numbers):
    """Calculate the mode of a list of numbers."""
    if len(numbers) == 0:
        return 0
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_count = max(freq.values())
    modes = [key for key, value in freq.items() if value == max_count]
    if len(modes) == 1:
        return modes[0]
    else:
        return modes
