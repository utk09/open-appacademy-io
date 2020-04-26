"""
Write a method vowel_cipher that takes in a string and returns a new string where every vowel becomes the next vowel in the alphabet.
"""


def vowel_cipher(string):
    vowel = "aeiou"
    new_str = ""
    for each_char in string:
        if each_char in vowel:
            



print(vowel_cipher("bootcamp"))  # => buutcemp
print(vowel_cipher("paper cup"))  # => pepir cap
