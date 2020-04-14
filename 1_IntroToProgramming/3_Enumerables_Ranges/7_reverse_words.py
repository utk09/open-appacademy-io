"""
Write a method reverse_words that takes in a sentence string and returns the sentence with the order of the characters in each word reversed. Note that we need to reverse the order of characters in the words, do not reverse the order of words in the sentence.
"""


def reverse_words(sent):
    new_word_list = []
    new_word_string = ""
    parts = sent.split(" ")
    for each_word in parts:
        reverse_word = reverse2(each_word)
        new_word_list.append(reverse_word)
    new_word_string = " ".join(new_word_list)
    return new_word_string


def reverse2(each_word):
    str_value = ''
    new_word = ''
    for i in range(len(each_word)):
        str_value = each_word[i]
        new_word = str_value + new_word
    return(new_word)


print(reverse_words('keep coding'))  # => 'peek gnidoc'
# => 'yticilpmis si etisiuqererp rof ytilibailer'
print(reverse_words('simplicity is prerequisite for reliability'))
