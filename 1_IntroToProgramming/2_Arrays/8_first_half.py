"""
Write a method first_half(array) that takes in an array and returns a new array containing the first half of the elements in the array. If there is an odd number of elements, return the first half including the middle element.
"""

# import math as m


def first_half(an_array):
    new_array = []
    k = (len(an_array))/2.0
    # x = int(m.ceil(k))
    i = 0
    while i < k:
        new_elem = an_array[i]
        new_array.append(new_elem)
        i += 1
    # for i in range(x):
    #     new_elem = an_array[i]
    #     new_array.append(new_elem)
    return new_array


print(first_half(["Brian", "Abby", "David", "Ommi"]))  # => ["Brian", "Abby"]
print(first_half(["a", "b", "c", "d", "e"]))          # => ["a", "b", "c"]
