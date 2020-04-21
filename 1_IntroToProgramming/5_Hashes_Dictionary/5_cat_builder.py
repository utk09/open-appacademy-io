"""
Write a method cat_builder that takes in a name, color, and age. The method should return a dictionary representing a cat with those values.
"""


def cat_builder(name_str, color_str, age_num):
    final_dict = {}
    final_dict["name"] = name_str
    final_dict["color"] = color_str
    final_dict["age"] = age_num
    return final_dict


# => {"name": "Whiskers", "color": "orange", "age": 3}
print(cat_builder("Whiskers", "orange", 3))

# => {"name": "Salem", "color": "black", "age": 100}
print(cat_builder("Salem", "black", 100))
