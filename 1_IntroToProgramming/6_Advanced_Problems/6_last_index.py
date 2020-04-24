"""
Write a method last_index that takes in a string and a character. The method should return the last index where the character can be found in the string.
"""


def last_index(string, character):
    char_list = []
    for each_word in string:
        char_list.append(each_word)

    index_list = []
    for letter_index in range(len(char_list)):
        if char_list[letter_index] == character:
            index_list.append(letter_index)
    return index_list[-1]


print(last_index("abca", "a"))  # => 3
print(last_index("mississipi", "i"))  # => 9
print(last_index("octagon", "o"))  # => 5
print(last_index("programming", "m"))  # => 7
