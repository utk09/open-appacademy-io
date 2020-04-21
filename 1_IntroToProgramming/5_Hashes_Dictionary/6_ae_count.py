"""
Write a method ae_count that takes in a string and returns a dictionary containing the number of a's and e's in the string. Assume the string contains only lowercase characters.
"""


def ae_count(string):
    count_a = 0
    count_e = 0
    final_dict = {}
    for each_letter in string:
        if each_letter == "a":
            count_a += 1
        elif each_letter == "e":
            count_e += 1
    final_dict["a"] = count_a
    final_dict["e"] = count_e
    return final_dict


print(ae_count("everyone can program"))  # => {"a": 2, "e": 3}
print(ae_count("keyboard"))  # => {"a": 1, "e": 1}
