"""
Write a method map_by_name that takes in an array of dictionary and returns a new array containing the names of each dictionary key.
"""


def map_by_name(arr):
    map_list = []
    for each_dict in range(len(arr)):
        map_dict = arr[each_dict]
        
        for key, value in map_dict.items():
            if key == "name":
                map_list.append(map_dict["name"])

    return map_list


pets = [
    {"type": "dog", "name": "Rolo"},
    {"type": "cat", "name": "Sunny"},
    {"type": "rat", "name": "Saki"},
    {"type": "dog", "name": "Finn"},
    {"type": "cat", "name": "Buffy"}
]
print(map_by_name(pets))  # => ["Rolo", "Sunny", "Saki", "Finn", "Buffy"]

countries = [
    {"name": "Japan", "continent": "Asia"},
    {"name": "Hungary", "continent": "Europe"},
    {"name": "Kenya", "continent": "Africa"},
]
print(map_by_name(countries))  # => ["Japan", "Hungary", "Kenya"]
