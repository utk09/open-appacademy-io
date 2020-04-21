"""
Write a method frequent_letters that takes in a string and returns an array containing the characters that appeared more than twice in the string.
"""


def frequent_letters(string):
    repeated_dict = {each_letter: string.count(
        each_letter) for each_letter in string}


print(frequent_letters('mississippi'))  # => ["i", "s"]

print(frequent_letters('bootcamp'))  # => []
