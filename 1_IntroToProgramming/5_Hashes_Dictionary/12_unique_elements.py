"""
Write a method unique_elements that takes in an array and returns a new array where all duplicate elements are removed. Solve this using a dictionary.
"""

# Hint: all keys of a dictionary are automatically unique


def unique_elements(arr):
    final_list = []
    new_dict = {each_element: arr.count(
        each_element) for each_element in arr}
    for each_key in new_dict.keys():
        final_list.append(each_key)
    return final_list


print(unique_elements(['a', 'b', 'a', 'a', 'b', 'c']))  # => ["a", "b", "c"]
