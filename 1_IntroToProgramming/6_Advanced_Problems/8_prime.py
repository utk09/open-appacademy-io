"""
Write a method prime_or_not that takes in a number and returns a boolean, indicating whether the number is prime. A prime number is only divisible by 1 and itself.
"""


def prime_or_not(num):
    prime_list = []
    last_num = num + 1

    if num == 2:
        return True

    elif num > 2:
        for each_num in range(2, last_num):
            if num % each_num == 0:
                prime_list.append(each_num)
        if len(prime_list) == 1:
            return True
        else:
            return False

    else:
        return False


print(prime_or_not(2))  # => true
print(prime_or_not(5))  # => true
print(prime_or_not(11))  # => true
print(prime_or_not(4))  # => false
print(prime_or_not(9))  # => false
print(prime_or_not(-5))  # => false
