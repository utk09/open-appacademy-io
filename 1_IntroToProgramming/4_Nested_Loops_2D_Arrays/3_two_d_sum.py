"""
Write a method two_d_Sum that takes in a two dimensional array and returns the sum of all elements in the array.
"""


def two_d_sum(arr):
    sum_all = 0
    try:
        for i in arr:
            for j in i:
                sum_all = sum_all + j
        return sum_all
    except:
        return "Please Enter a 2D Array"


array_1 = [
    [4, 5],
    [1, 3, 7, 1]
]
print(two_d_sum(array_1))   # => 21

array_2 = [
    [3, 3],
    [2],
    [2, 5]
]
print(two_d_sum(array_2))  # => 15
