# Write a program that counts the number of "A/a" in a string.


def count_a(word):
    count = 0
    i = 0
    while i < len(word):
        char = word[i]
        if char == "a" or char == "A":
            count += 1
        i += 1
    print(count)
    return count


count_a("application")  # => 2
count_a("bike")         # => 0
count_a("Arthur")       # => 1
count_a("Aardvark")     # => 3
