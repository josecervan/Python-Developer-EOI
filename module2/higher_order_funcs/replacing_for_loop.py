from functools import reduce


numbers = list(range(1, 7))

# # Filter for odd numbers
odds = list(filter(lambda x: x % 2 == 1, numbers))

# Square all odd numbers
squared_odds = list(map(lambda x: x ** 2, numbers))

# Calculate total
total = reduce(lambda x, y: x + y, numbers)

# Results
print(f'Numbers: {numbers}')
print(f'Odds: {odds}')
print(f'Squared odds: {squared_odds}')
print(f'Total sum: {total}')
