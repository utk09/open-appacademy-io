"""
Write a method caesar_cipher that takes in a string and a number. The method should return a new string where every character of the original is shifted num characters in the alphabet.
"""

# Feel free to use this variable:
# alphabet = "abcdefghijklmnopqrstuvwxyz"


# chr(97) = a
# ord('a') = 97

def caesar_cipher(string, num):
    string = string.lower()
    new_str = ""
    for character in range(len(string)):
        char_new = string[character]
        new_str = new_str + chr((ord(char_new) + num - 97) % 26 + 97)
    return new_str


print(caesar_cipher("apple", 1))  # => "bqqmf"
print(caesar_cipher("bootcamp", 2))  # => "dqqvecor"
print(caesar_cipher("zebra", 4))  # => "difve"
