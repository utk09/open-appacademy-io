"""
The fibonacci sequence is a sequence of numbers whose first and second elements are 1. To generate further elements of the sequence we take the sum of the previous two elements. For example the first 6 fibonacci numbers are 1, 1, 2, 3, 5, 8. Write a method fibonacci that takes in a number length and returns the fibonacci sequence up to the given length.
"""


def fibonacci(length):
    final_list = []
    x = 1
    if length == 0:
        return final_list

    elif length == 1:
        final_list.append(1)
        return final_list

    else:
        final_list.append(1)
        final_list.append(1)
        for val in range(1, length - 1):
            x = x + final_list[val]
            final_list.append(x)
            x = final_list[val]
        return final_list


print(fibonacci(0))  # => []

print(fibonacci(1))  # => [1]

print(fibonacci(6))  # => [1, 1, 2, 3, 5, 8]

print(fibonacci(8))  # => [1, 1, 2, 3, 5, 8, 13, 21]

print(fibonacci(12))
