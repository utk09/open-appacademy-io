"""
Write a method frequent_letters that takes in a string and returns an array containing the characters that appeared more than twice in the string.
"""


def frequent_letters(string):
    repeated_words_array = []
    repeated_dict = {each_letter: string.count(
        each_letter) for each_letter in string}
    for key, values in repeated_dict.items():
        if values > 2:
            repeated_words_array.append(key)
    return repeated_words_array


print(frequent_letters('mississippi'))  # => ["i", "s"]

print(frequent_letters('bootcamp'))  # => []

