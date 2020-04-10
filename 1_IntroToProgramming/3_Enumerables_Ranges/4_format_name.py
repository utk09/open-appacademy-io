"""
Write a method format_name that takes in a name string and returns the name properly capitalized.
"""

# Hint: use str.upcase and str.downcase
# "abc".upcase # => "ABC"


def format_name(string):
    words = string.split(" ")
    new_words = []
    for word in words:
        new_word = capitalized_name(word)
        new_words.append(new_word)
        new_sent = " ".join(map(str, new_words))
    return new_sent


def capitalized_name(word):
    capitalized_word = word.capitalize()
    return capitalized_word


print(format_name("chase WILSON"))  # => "Chase Wilson"
print(format_name("brian CrAwFoRd scoTT"))  # => "Brian Crawford Scott"
