"""
Write a method combinations that takes in an array of unique elements, the method should return a 2D array representing all possible combinations of 2 elements of the array.
"""

from itertools import combinations


def combinations_ans(arr):
    pairs = []
    comb = list(combinations(arr, 2))
    for i in range(len(comb)):
        pairs.append(list(comb[i]))
    return pairs


# => [ [ "a", "b" ], [ "a", "c" ], [ "b", "c" ] ]
print(combinations_ans(["a", "b", "c"]))

# => [ [ 0, 1 ], [ 0, 2 ], [ 0, 3 ], [ 1, 2 ], [ 1, 3 ], [ 2, 3 ] ]
print(combinations_ans([0, 1, 2, 3]))
