"""
Write a method whisper_words that takes in an array of words and returns a new array containing a whispered version of each word. See the examples. Solve this using map :-).
"""


def whisper_words(words):
    new_sent = map(map_words, words)
    new_sent_2 = list(new_sent)

    return new_sent_2


def map_words(words):
    each_word = words.lower() + "..."
    return each_word


# => ["keep...", "the...", "noise...", "down..."]
print(whisper_words(["KEEP", "The", "NOISE", "down"]))
