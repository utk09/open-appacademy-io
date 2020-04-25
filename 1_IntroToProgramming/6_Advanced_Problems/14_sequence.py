"""
A number's summation is the sum of all positive numbers less than or equal to the number. For example: the summation of 3 is 6 because 1 + 2 + 3 = 6, the summation of 6 is 21 because 1 + 2 + 3 + 4 + 5 + 6 = 21. Write a method summation_sequence that takes in a two numbers: start and length. The method should return an array containing length total elements. The first number of the sequence should be the start number. At any point, to generate the next element of the sequence we take the summation of the previous element. You can assume that length is not zero.
"""


def summation_sequence(start, length):
    final_list = [start]
    val = start
    i = 0
    while i < length - 1:
        x = total_sum(val)
        final_list.append(x)
        val = x
        i += 1
    return final_list


def total_sum(num):
    for i in range(1, num):
        num = num + i
    return num


print(summation_sequence(3, 4))  # => [3, 6, 21, 231]
# => 3, 1+2+3=6, 1+2+3+4+5+6=21, 1+2+3+4+5+6+7+8+9+10+....+19+20+21 = 231

print(summation_sequence(5, 3))  # => [5, 15, 120]
# => 5, 1+2+3+4+5=15, 1+2+3+4+5+....13+14+15=120
