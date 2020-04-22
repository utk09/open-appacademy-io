"""
Write a method hash_to_pairs that takes in a dictionary and returns a 2D array representing each key-value pair of the dictionary.
"""


def hash_to_pairs(hash_in):
    data_pairs = [[key, value] for key, value in hash_in.items()]
    return data_pairs

# => [["name", "skateboard"], ["wheels", 4], ["weight", "7.5 lbs"]]
print(hash_to_pairs({"name": "skateboard", "wheels": 4, "weight": "7.5 lbs"}))


# => [["kingdom", "animalia"], ["genus", "canis"], ["breed", "German Shepherd"]]
print(hash_to_pairs({"kingdom": "animalia",
                     "genus": "canis", "breed": "German Shepherd"}))
