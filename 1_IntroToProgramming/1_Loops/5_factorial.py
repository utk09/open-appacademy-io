# Write a method factorial(num) that takes in a number num and returns the product of all numbers from 1 up to and including num.


def factorial(num):
    total = 1
    for i in range(1, num+1):
        total = total * i
    return total


print(factorial(3))  # prints 6
print(factorial(5))  # prints 120
