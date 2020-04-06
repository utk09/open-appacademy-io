"""
Write a method select_odds(numbers) that takes in an array of numbers and returns a new array containing the odd numbers of the original array.
"""


def select_odds(numbers):
    new_numbers = []
    i = 0
    while i < len(numbers):
        if (numbers[i]) % 2 == 1:
            new_numbers.append(numbers[i])
        i += 1
    return new_numbers


print(select_odds([13, 4, 3, 7, 6, 11]))   # => [13, 3, 7, 11]
print(select_odds([2, 4, 6]))              # => []
print(select_odds([10, 23, 6, 7, 14, 5]))  # => [23, 7, 5]
