"""
Write a method get_double_age that takes in a dictionaary and returns twice the "age" value of the dictionary.
"""


def get_double_age(hash_in):
    x = hash_in["age"]
    return x*2


print(get_double_age({"name": "App Academy", "age": 5}))  # => 10
print(get_double_age({"name": "Ruby", "age": 23}))       # => 46
