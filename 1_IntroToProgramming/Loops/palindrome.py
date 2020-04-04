'''
Write a method is_palindrome(word) that takes in a string word and returns the true if the word is a palindrome, false otherwise. A palindrome is a word that is spelled the same forwards and backwards.
'''


def is_palindrome(word):
    str_value = ''
    new_word = ''
    for i in range(len(word)):
        str_value = word[i]
        new_word = str_value + new_word
    if new_word == word:
        return True
    else:
        return False


print(is_palindrome("racecar"))  # prints true
print(is_palindrome("kayak"))  # prints true
print(is_palindrome("bootcamp"))  # prints false
