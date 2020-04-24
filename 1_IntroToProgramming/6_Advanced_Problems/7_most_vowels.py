"""
Write a method most_vowels that takes in a sentence string and returns the word of the sentence that contains the most vowels.
"""


def most_vowels(sentence):
    vowels = "aeiou"
    word_dict = {}
    count = 0
    split_sentence = sentence.split(" ")
    for each_word in split_sentence:
        for each_letter in each_word:
            if each_letter in vowels:
                count += 1
        word_dict[each_word] = count
        count = 0

    value_list = []
    for key, value in word_dict.items():
        value_list.append(value)
        max_value = max(value_list)

    for key, value in word_dict.items():
        if value == max_value:
            return key


print(most_vowels("what a wonderful life"))  # => "wonderful"
