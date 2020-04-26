"""
Write a method that takes in a string and returns the number of times that the same letter repeats twice in a row.
"""


def double_letter_count(string):
    new_str = string.split(" ")
    count = 0
    for each_word in new_str:
        for i in range(len(each_word) - 1):
            if each_word[i] == each_word[i + 1]:
                count += 1
    return count


print(double_letter_count("the jeep rolled down the hill"))  # => 3
print(double_letter_count("bootcamp"))  # => 1
