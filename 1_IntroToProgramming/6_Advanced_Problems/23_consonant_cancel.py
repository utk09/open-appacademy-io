"""
Write a method consonant_cancel that takes in a sentence and returns a new sentence where every word begins with it's first vowel.
"""


def consonant_cancel(sentence):
    sentence = sentence.split(" ")
    sent_arr = []
    final_sent = " "
    for each_word in sentence:
        sent_arr.append(minus_conso(each_word))

    final_sent = " ".join(map(str, sent_arr))
    return final_sent


def minus_conso(word):
    vowels = "aeiou"
    for each_index, each_char in enumerate(word):
        if each_char in vowels:
            after_vowel = word[each_index:]
            new_word = after_vowel
            return new_word


print(consonant_cancel("down the rabbit hole"))  # => "own e abbit ole"

# => "iting ode is allenging"
print(consonant_cancel("writing code is challenging"))
