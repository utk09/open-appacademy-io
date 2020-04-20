"""
Write a method opposite_count that takes in an array of unique numbers. The method should return the number of pairs of elements that sum to 0.
"""


def opposite_count(nums):
    count = 0
    n = len(nums)
    for i in range(0, n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == 0:
                count += 1
    return count


print(opposite_count([2, 5, 11, -5, -2, 7]))  # => 2
print(opposite_count([21, -23, 24 - 12, 23]))  # => 1
