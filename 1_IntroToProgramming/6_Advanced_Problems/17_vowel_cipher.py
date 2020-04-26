"""
Write a method vowel_cipher that takes in a string and returns a new string where every vowel becomes the next vowel in the alphabet.
"""


def vowel_cipher(string):
    vowel = "aeiou"
    new_str = ""
    for each_char in string:
        if each_char in vowel:
            old_pos = vowel.index(each_char)
            new_pos = old_pos + 1
            new_str = new_str + vowel[new_pos % len(vowel)]
        else:
            new_str = new_str + each_char
    return new_str


print(vowel_cipher("bootcamp"))  # => buutcemp
print(vowel_cipher("paper cup"))  # => pepir cap
print(vowel_cipher("aeiou")) # => eioua
