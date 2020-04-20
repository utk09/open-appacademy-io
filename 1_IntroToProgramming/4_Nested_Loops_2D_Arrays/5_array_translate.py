"""
Write a method array_translate that takes in an array whose elements alternate between words and numbers. The method should return a string where each word is repeated the number of times that immediately follows in the array.
"""


def array_translate(array):
    pairs = ""
    for i in range(len(array)):
        if i % 2 == 0:
            x = array[i] * array[i + 1]
            pairs = pairs + x
    return pairs


# => "CatCatDogDogDogMouse"
print(array_translate(["Cat", 2, "Dog", 3, "Mouse", 1]))

print(array_translate(["red", 3, "blue", 1]))  # => "redredredblue"
