"""
Write a method retrieve_values that takes in two dictionary's and a key. The method should return an array containing the values from the two hashes that correspond with the given key.
"""


def retrieve_values(hash1, hash2, key):
    final_list = []
    if key in dog1 and dog2:
        final_list.append(dog1[key])
        final_list.append(dog2[key])
    return final_list


dog1 = {"name": "Fido", "color": "brown"}
dog2 = {"name": "Spot", "color": "white"}

print(retrieve_values(dog1, dog2, "name"))  # => ["Fido", "Spot"]
print(retrieve_values(dog1, dog2, "color"))  # => ["brown", "white"]
