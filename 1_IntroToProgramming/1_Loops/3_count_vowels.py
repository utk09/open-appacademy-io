# Write a program that counts the number of "vowels(a,e,i,o,u)" in a string.


def count_vowels(word):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    count = 0
    i = 0
    while i < len(word):
        char = word[i]
        # print(char)
        if char in vowels:
            count += 1
        i += 1
    print(count)
    return count


count_vowels("bootcamp")  # => 3
count_vowels("apple")     # => 2
count_vowels("pizza")     # => 2
