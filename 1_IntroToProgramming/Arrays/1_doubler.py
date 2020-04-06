# Write a method doubler(numbers) that takes an array of numbers and returns a new array where every element of the original array is multiplied by 2.


def doubler(numbers):
    new_numbers = []
    for i in range(len(numbers)):
        old_elem = numbers[i]
        new_elem = old_elem * 2
        new_numbers.append(new_elem)
    return(new_numbers)


print(doubler([1, 2, 3, 4]))  # prints [2,4,6,8]
print(doubler([2, 4, 6]))  # prints [4, 8, 12]
