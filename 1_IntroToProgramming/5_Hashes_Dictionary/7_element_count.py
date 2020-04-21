"""
Write a method element_count that takes in an array and returns a dictionary representing the count of each element in the array.
"""


def element_count(arr):
    final_dict = {}
    final_dict = {each_element: arr.count(
        each_element) for each_element in arr}
    return final_dict


print(element_count(["a", "b", "a", "a", "b"]))  # => {"a":3, "b":2}

# => {"red": 2, "blue": 1, "green": 1}
print(element_count(["red", "red", "blue", "green"]))
