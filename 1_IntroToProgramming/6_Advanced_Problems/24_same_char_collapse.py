"""
Write a method same_char_collapse that takes in a string and returns a collapsed version of the string. To collapse the string, we repeatedly delete 2 adjacent characters that are the same until there are no such adjacent characters. If there are multiple pairs that can be collapsed, delete the leftmost pair. For example, we take the following steps to collapse "zzzxaaxy": zzzxaaxy -> zxaaxy -> zxxy -> zy
"""


def same_char_collapse(string):
    collapsable = True
    while collapsable:
        collapsable = False
        split = list(string)
        for i in range(0, len(split) - 1):
            if split[i] == split[i+1]:
                split[i] = ""
                split[i+1] = ""
                collapsable = True
                break
        string = "".join(split)
    return string


print(same_char_collapse("zzzxaaxy"))  # => "zy"
# because zzzxaaxy -> zxaaxy -> zxxy -> zy

print(same_char_collapse("uqrssrqvtt"))  # => "uv"
# because uqrssrqvtt -> uqrrqvtt -> uqqvtt -> uvtt -> uv
