"""
Write a method element_times_index(nums) that takes in an array of numbers and returns a new array containing every number of the original array multiplied with its index.
"""


def element_times_index(numbers):
    new_numbers = []
    for i in range(len(numbers)):
        old_elem = numbers[i]
        new_elem = old_elem * i
        new_numbers.append(new_elem)
    return new_numbers


print(element_times_index([4, 7, 6, 5]))      # => [0, 7, 12, 15]
print(element_times_index([1, 1, 1, 1, 1, 1]))  # => [0, 1, 2, 3, 4, 5]
