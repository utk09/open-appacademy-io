"""
Write a method is_valid_name that takes in a string and returns a boolean indicating whether or not it is a valid name.
"""

# A name is valid is if satisfies all of the following:
# - contains at least a first name and last name, separated by spaces
# - each part of the name should be capitalized
#
# Hint: use str.upcase or str.downcase
# "a".upcase # => "A"


def is_valid_name(string):
    old_name = string.split(" ")
    name = 0
    x = []
    if len(old_name) < 2:
        return False
    else:
        while name < len(old_name):
            new_name = old_name[name]
            if new_name == new_name.capitalize():
                x.append(True)
            else:
                x.append(False)
            name += 1
        for i in x:
            if x[i] == True:
                return True
            else:
                return False


print(is_valid_name("Kush Patel"))       # => true
print(is_valid_name("Daniel"))           # => false
print(is_valid_name("Robert Downey Jr"))  # => true
print(is_valid_name("ROBERT DOWNEY JR"))  # => false
