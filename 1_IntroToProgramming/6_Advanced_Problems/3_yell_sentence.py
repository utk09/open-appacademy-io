"""
Write a method yell_sentence that takes in a sentence string and returns a new sentence where every word is yelled. See the examples. Use map to solve this.
"""


def yell_sentence(sent):
    new_sent = sent.split(" ")
    new_sent_2 = []
    final_out = " "
    
    for each_word in new_sent:
        each_word = each_word.upper() + "!"
        new_sent_2.append(each_word)

    final_out = " ".join(map(str, new_sent_2))
    return final_out


# => "I! HAVE! A! BAD! FEELING! ABOUT! THIS!"
print(yell_sentence("I have a bad feeling about this"))
