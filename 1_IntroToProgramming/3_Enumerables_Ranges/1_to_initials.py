"""
Write a method to_initials that takes in a person's name string and returns a string representing their initials.
"""


def to_initials(name):
    x_split = name.split(" ")
    new_name = " "
    new_name_array = []
    i = 0
    while i < len(x_split):
        m = (x_split[i])[0]
        new_name_array.append(m)
        i += 1
    new_name = "".join(new_name_array)
    return new_name


print(to_initials("Kelvin Bridges"))      # => "KB"
print(to_initials("Michaela Yamamoto"))   # => "MY"
print(to_initials("Mary La Grange"))      # => "MLG"
