"""
Write a method is_valid_email that takes in a string and returns a boolean indicating whether or not it is a valid email address.
"""

# For simplicity, we'll consider an email valid when it satisfies all of the following:
# - contains exactly one @ symbol
# - contains only lowercase alphabetic letters before the @
# - contains exactly one . after the @


def is_valid_email(string):
    parts = string.split("@")
    if len(parts) != 2:
        return False
    first = parts[0]
    second = parts[1]
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for each_char in first:
        if each_char not in alpha:
            return False

    if len(second.split(".")) == 2:
        return True

    else:
        return False


print(is_valid_email("abc@xy.z"))         # => true
print(is_valid_email("jdoe@gmail.com"))   # => true
print(is_valid_email("jdoe@g@mail.com"))  # => false
print(is_valid_email("jdoe42@gmail.com"))  # => false
print(is_valid_email("jdoegmail.com"))    # => false
print(is_valid_email("az@email"))         # => false
print(is_valid_email("AASDSGGDGGD@dffdfh.dfbhdfh"))  # => false
