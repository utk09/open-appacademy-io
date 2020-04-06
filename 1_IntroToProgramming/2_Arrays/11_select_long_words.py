"""
Write a method select_long_words(words) that takes in an array of words and returns a new array containing all of the words of the original array that are longer than 4 characters.
"""


def select_long_words(words):
    new_longest_word = []
    i = 0
    while i < len(words):
        k = len(words[i])
        if k > 4:
            new_longest_word.append(words[i])
        i += 1
    return new_longest_word


# ["eating", "dinner"]
print(select_long_words(["what", "are", "we", "eating", "for", "dinner"]))
print(select_long_words(["keep", "coding"]))  # => ["coding"]
