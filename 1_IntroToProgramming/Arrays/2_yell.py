# Write a method yell(words) that takes in an array of words and returns a new array where every word from the original array has an exclamation point after it.


def yell(words):
    add_exclam = []
    for i in range(len(words)):
        old_word = words[i]
        new_word = old_word + "!"
        add_exclam.append(new_word)
    return add_exclam


print(yell(["hello", "world"]))  # => ["hello!", "world!"]
print(yell(["code", "is", "cool"]))  # => ["code!", "is!", "cool!"]
