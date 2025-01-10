#stats.py
def median(numbers):
    #Calculate the median
    numbers = sorted(numbers)
    n = len(numbers)
    mid = n // 2
    return (numbers[mid] if n % 2 != 0 else (numbers[mid - 1] + numbers[mid]) / 2)

def mode(numbers):
    #Find the mode
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    return modes[0] if len(modes) == 1 else None

def mean(numbers):
    #Calculate the average
    return sum(numbers) / len(numbers) if numbers else 0
