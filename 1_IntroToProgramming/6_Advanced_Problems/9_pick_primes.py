"""
Write a method pick_primes that takes in an array of numbers and returns a new array containing only the prime numbers.
"""


def pick_primes(numbers):
    prime_list = []
    for each_num in numbers:
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


print(pick_primes([2, 3, 4, 5, 6]))  # => [2, 3, 5]

print(pick_primes([101, 20, 103, 2017]))  # => [101, 103, 2017]
