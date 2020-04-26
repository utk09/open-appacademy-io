"""
Write a method anagrams_or_not that takes in two words and returns a boolean indicating whether or not the words are anagrams. Anagrams are words that contain the same characters but not necessarily in the same order. Solve this without using .sort
"""


def anagrams_or_not(word1, word2):
    arr1 = []
    arr2 = []
    for ele1 in word1:
        arr1.append(ele1)

    x = arr1

    for ele2 in word2:
        arr2.append(ele2)

    y = arr2

    x.sort()
    y.sort()

    if x == y:
        return True
    else:
        return False


print(anagrams_or_not("cat", "act"))  # => true
print(anagrams_or_not("restful", "fluster"))  # => true
print(anagrams_or_not("cat", "dog"))  # => false
print(anagrams_or_not("boot", "bootcamp"))  # => false
