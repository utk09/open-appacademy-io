"""
Write a method abbreviate_sentence that takes in a sentence string and returns a new sentence where every word longer than 4 characters has all of it's vowels removed.
"""


def abbreviate_sentence(sent):
    words = sent.split(" ")
    new_words = []
    for word in words:
        if len(word) > 4:
            new_word = abbreviate_word(word)
            new_words.append(new_word)
        else:
            new_words.append(word)

        new_sent = " ".join(map(str, new_words))
    return new_sent



print(abbreviate_sentence("follow the yellow brick road")) # => "fllw the yllw brck road"

print(abbreviate_sentence("what a wonderful life"))  # => "what a wndrfl life"
