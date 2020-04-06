"""
Write a method reverse_range(min, max) that takes in two numbers min and max. The function should return an array containing all numbers from min to max in reverse order. The min and max should be excluded from the array
"""


def reverse_range(minimum, maximum):
    new_range = []
    new_nums = []
    for i in range(minimum+1, maximum):
        new_nums.append(i)
    new_range = new_nums[::-1]
    return new_range


print(reverse_range(10, 17))  # => [16, 15, 14, 13, 12, 11]
print(reverse_range(1, 7))   # => [6, 5, 4, 3, 2]
