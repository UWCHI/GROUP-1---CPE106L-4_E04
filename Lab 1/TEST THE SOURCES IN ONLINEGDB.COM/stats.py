# Note: Run this file "stats.py" when testing in onlinegdb.com

def mean(numbers):
    """Compute the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    """Compute the median of a list of numbers."""
    if not numbers:
        return 0
    numbers.sort()
    mid = len(numbers) // 2
    return (numbers[mid - 1] + numbers[mid]) / 2 if len(numbers) % 2 == 0 else numbers[mid]

def mode(numbers):
    """Compute the mode of a list of numbers."""
    if not numbers:
        return 0
    freq = {num: numbers.count(num) for num in set(numbers)}
    max_count = max(freq.values())
    return [num for num, count in freq.items() if count == max_count][0]
