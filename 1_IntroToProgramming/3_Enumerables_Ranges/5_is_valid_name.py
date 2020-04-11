"""
Write a method is_valid_name that takes in a string and returns a boolean indicating whether or not it is a valid name.
"""

# A name is valid is if satisfies all of the following:
# - contains at least a first name and last name, separated by spaces
# - first part of the name should be capitalized
#


def is_valid_name(string):
    old_name = string.split(" ")
    if len(old_name) < 2:
        return False
    else:
        for word in old_name:
            if not is_capitalized(word):
                return False
    return True


def is_capitalized(word):
    if word == word.capitalize():
        return True
    else:
        return False


print(is_valid_name("Kush Patel"))       # => true
print(is_valid_name("Daniel"))           # => false
print(is_valid_name("Robert Downey Jr"))  # => true
print(is_valid_name("ROBERT DOWNEY JR"))  # => false
