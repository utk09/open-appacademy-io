"""
Write a method get_full_name that takes in a dictionary containing a first, last, and title. The method should return a string representing the dictionary's full name
"""


def get_full_name(hash_in):
    full_name = hash_in["first"] + " " + \
        hash_in["last"] + ", the " + hash_in["title"]
    return full_name


hash1 = {"first": "Michael", "last": "Jordan", "title": "GOAT"}
print(get_full_name(hash1))  # => "Michael Jordan, the GOAT"

hash2 = {"first": "Fido", "last": "McDog", "title": "Loyal"}
print(get_full_name(hash2))  # => "Fido McDog, the Loyal"
