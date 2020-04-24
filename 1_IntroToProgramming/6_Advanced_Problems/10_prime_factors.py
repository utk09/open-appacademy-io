"""
Write a method prime_factors that takes in a number and returns an array containing all of the prime factors of the given number.
"""


def prime_factors(number):
    final_list = []
    prime_list_2 = pick_primes(number)
    for each_value in prime_list_2:
        if number % each_value == 0:
            final_list.append(each_value)

    return final_list


def pick_primes(numbers):
    prime_list = []
    for each_num in range(numbers):
        x = prime_or_not(each_num)
        if x != None:
            prime_list.append(x)
    return prime_list


def prime_or_not(new_num):
    prime_list = []
    last_num = new_num + 1

    if new_num == 2:
        return new_num

    elif new_num > 2:
        for each_num in range(2, last_num):
            if new_num % each_num == 0:
                prime_list.append(each_num)
        if len(prime_list) == 1:
            for each_element in prime_list:
                return each_element
        else:
            return None

    else:
        return None


print(prime_factors(24))  # => [2, 3]

print(prime_factors(60))  # => [2, 3, 5]
