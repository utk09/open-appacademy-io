"""
Write a method even_nums(max) that takes in a number max and returns an array containing all even numbers from 0 to max
"""


def even_nums(maximum):
    new_nums = []
    old_elem = []
    for i in range(maximum+1):
        old_elem.append(i)
    for j in range(len(old_elem)):
        if j % 2 == 0:
            new_nums.append(j)
    return new_nums


print(even_nums(10))  # => [0, 2, 4, 6, 8, 10]
print(even_nums(5))  # => [0, 2, 4]
