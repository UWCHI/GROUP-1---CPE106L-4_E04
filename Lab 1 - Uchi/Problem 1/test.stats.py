# test_stats.py
# Test script for stats.py

from stats import mean, median, mode

# Test data
numbers = [1, 2, 2, 3, 4]

# Testing each function
print("Testing stats.py...")
print("Numbers:", numbers)
print("Mean:", mean(numbers))  # Should return 2.4
print("Median:", median(numbers))  # Should return 2
print("Mode:", mode(numbers))  # Should return 2
