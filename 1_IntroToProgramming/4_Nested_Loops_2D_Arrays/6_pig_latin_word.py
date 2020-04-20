"""
Write a method pig_latin_word that takes in a word string and translates the word into pig latin.
"""

# Pig latin translation uses the following rules:
# - for words that start with a vowel, add 'yay' to the end
# - for words that start with a nonvowel, move all letters before the first vowel to the end of the word and add 'ay'


def pig_latin_word(word):
    new_word = ""
    vowels = "aeiou"
    if word[0] in vowels:
        new_word = word + "yay"
        return new_word
    else:
        pass


print(pig_latin_word("apple"))   # => "appleyay"
print(pig_latin_word("eat"))     # => "eatyay"
print(pig_latin_word("banana"))  # => "ananabay"
print(pig_latin_word("trash"))   # => "ashtray"
