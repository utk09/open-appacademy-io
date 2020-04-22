"""
Write a method map_by_key that takes in an array of dictionary and a key string. The method should returns a new array containing the values from each dictionary for the given key.
"""


def map_by_key(arr, key):
    map_list = []
    for each_dict in range(len(arr)):
        map_dict = arr[each_dict]

        for key_in, value_in in map_dict.items():
            if key_in == key:
                map_list.append(map_dict[key_in])

    return map_list


locations = [
    {"city": "New York City", "state": "New York", "coast": "East"},
    {"city": "San Francisco", "state": "California", "coast": "West"},
    {"city": "Portland", "state": "Oregon", "coast": "West"},
]

# => ["New York", "California", "Oregon"]
print(map_by_key(locations, "state"))

# => ["New York City", "San Francisco", "Portland"]
print(map_by_key(locations, "city"))
