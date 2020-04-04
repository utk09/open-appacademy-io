# Write a method reverse(word) that takes in a string word and returns the word with its letters in reverse order.


def reverse(word):
    str_value = ''
    new_word = ''
    for i in range(1, len(word)+1):
        str_value = word[-i]
        new_word = new_word + str_value
    return(new_word)


print(reverse("cat"))  # prints "tac"
print(reverse("programming"))  # prints ""
print(reverse("bootcamp"))   # prints "pmactoob"
print(reverse("noon"))  # print "noon"


# Solution 2

print("---------------------------------------------")


def reverse2(word):
    str_value = ''
    new_word = ''
    for i in range(len(word)):
        str_value = word[i]
        new_word = str_value + new_word
    return(new_word)


print(reverse2("cat"))  # prints "tac"
print(reverse2("programming"))  # prints ""
print(reverse2("bootcamp"))   # prints "pmactoob"
print(reverse2("noon"))  # print "noon"
