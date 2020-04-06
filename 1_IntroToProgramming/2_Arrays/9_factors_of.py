"""
Write a method factors_of(num) that takes in a num and returns an array of all positive numbers less than or equal to num that can divide num.
"""


def factors_of(nums):
    new_nums = []
    i = 1
    while i < nums+1:
        if nums % i == 0:
            new_nums.append(i)
        i += 1
    return new_nums


print(factors_of(3))   # => [1, 3]
print(factors_of(4))   # => [1, 2, 4]
print(factors_of(8))   # => [1, 2, 4, 8]
print(factors_of(9))   # => [1, 3, 9]
print(factors_of(16))  # => [1, 2, 4, 8, 16]
