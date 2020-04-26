"""
Write a method pyramid_sum that takes in an array of numbers representing the base of a pyramid. The function should return a 2D array representing a complete pyramid with the given base. To construct a level of the pyramid, we take the sum of adjacent elements of the level below.
"""

# For example, the base [1, 4, 6] gives us the following pyramid
#     15
#   5   10
# 1   4    6


def pyramid_sum(base):
    final_arr = []
    final_arr.append(base)
    i = 0
    while i < len(base) - 1:
        x = adjacent_sum(base)
        final_arr.append(x)
        base = x
    final_arr = final_arr[::-1]

    return final_arr


def adjacent_sum(arr):
    new_arr = []
    for each_term in range(len(arr) - 1):
        new_arr.append(arr[each_term] + arr[each_term + 1])
    return new_arr


print(pyramid_sum([1, 4, 6]))  # => [[15], [5, 10], [1, 4, 6]]


# => [[41], [19, 22], [10, 9, 13], [3, 7, 2, 11]]
print(pyramid_sum([3, 7, 2, 11]))
