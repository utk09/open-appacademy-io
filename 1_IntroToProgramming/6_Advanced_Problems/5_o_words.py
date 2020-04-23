"""
Write a method o_words that takes in a sentence string and returns an array of the words that contain an "o". Use select in your solution!
"""

"""

Built-in Functions( https://docs.python.org/3.6/library/functions.html )

abs() | dict() | help() | min() | setattr() | all() | dir() | hex() | next()

slice() | any() | divmod() | id() | object() | sorted() | ascii() | enumerate()

input() | oct() | staticmethod() | bin() | eval() | int() | open() | str()

bool() | exec() | isinstance() | ord() | sum() | bytearray() | filter()

issubclass() | pow() | super() | bytes() | float() | iter() | print() | tuple()

callable() | format() | len() | property() | type() | chr() | frozenset()

list() | range() | vars() | classmethod() | getattr() | locals() | repr() | zip()

compile() | globals() | map() | reversed() | __import__() | complex() | hasattr()

max() | round() | delattr() | hash() | memoryview() | set()

"""


# select() not available in python. So using traditional method instead

def o_words(sentence):
    final_list = []
    split_sent = sentence.split(" ")
    for each_word in split_sent:
        if each_word.__contains__("o"):
            final_list.append(each_word)
    return final_list


print(o_words("How did you do that?"))  # => ["How", "you", "do"]
