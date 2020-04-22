"""
Write a method whisper_words that takes in an array of words and returns a new array containing a whispered version of each word. See the examples. Solve this using map :-).
"""


def whisper_words(words):
    new_sent_2 = []

    for each_word in words:
        each_word = each_word.lower() + "..."
        new_sent_2.append(each_word)

    return new_sent_2


# => ["keep...", "the...", "noise...", "down..."]
print(whisper_words(["KEEP", "The", "NOISE", "down"]))
