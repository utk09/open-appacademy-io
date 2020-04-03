# Write a program that counts the number of "E/e" in a string.


def count_e(word):
    count = 0
    i = 0
    while i < len(word):
        char = word[i]
        if char == "E" or char == "e":
            count += 1
        i += 1
    return count


print("Count for 'Excellent': ", count_e("excellent"))
print("Count for 'entrepreneurialism': ", count_e("Entrepreneurialism"))