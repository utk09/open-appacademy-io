"""
Write a method element_replace that takes in an array and a dictionary. The method should return a new array where elements of the original array are replaced with their corresponding values in the dictionary.
"""


def element_replace(arr, hash_in):
    final_arr = []
    for key in hash_in.keys():
        if key in arr:
            final_arr.append(hash_in[key])

    for each_element in arr:
        if each_element not in hash_in.keys():
            final_arr.append(each_element)

    return final_arr

arr1 = ["LeBron James", "Lionel Messi", "Serena Williams"]
hash1 = {"Serena Williams": "tennis", "LeBron James": "basketball"}
# => ["basketball", "Lionel Messi", "tennis"]
print(element_replace(arr1, hash1))


arr2 = ["dog", "cat", "mouse"]
hash2 = {"dog": "bork", "cat": "meow", "duck": "quack"}
print(element_replace(arr2, hash2))  # => ["bork", "meow", "mouse"]
