"""
Write a method triple_sequence that takes in two numbers, start and length. The method should return an array representing a sequence that begins with start and is length elements long. In the sequence, every element should be 3 times the previous element. Assume that the length is at least 1.
"""


def triple_sequence(start, length):
    final_list = [start]
    val = start
    i = 0
    while i < length-1:
        x = mul_previous(val)
        final_list.append(x)
        val = x
        i += 1
    return final_list


def mul_previous(num):
    return num * 3


print(triple_sequence(2, 4))  # => [2, 6, 18, 54]

print(triple_sequence(4, 5))  # => [4, 12, 36, 108, 324]
