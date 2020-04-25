"""
Write a method perfect_square_or_not that takes in a number and returns a boolean indicating whether it is a perfect square. A perfect square is a number that results from multiplying a number by itself. For example, 9 is a perfect square because 3*3 = 9, 25 is a perfect square because 5*5 = 25.
"""


def perfect_square_or_not(number):
    if number == 0 or number == 1:
        return True

    else:
        new_list = factor_of_num(number)

        final_list = []
        for each_val in new_list:
            if each_val * each_val == number:
                final_list.append(each_val)

        if len(final_list) == 1:
            return True
        else:
            return False


def factor_of_num(num):
    val_list = []
    for a_val in range(2, num):
        if num % a_val == 0:
            val_list.append(a_val)
    return val_list


print(perfect_square_or_not(5))  # => false
print(perfect_square_or_not(12))  # => false
print(perfect_square_or_not(30))  # => false
print(perfect_square_or_not(9))  # => true
print(perfect_square_or_not(25))  # => true
