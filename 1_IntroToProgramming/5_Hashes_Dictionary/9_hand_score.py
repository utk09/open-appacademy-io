"""
Write a method hand_score that takes in a string representing a hand of cards and returns it's total score. You can assume the letters in the string are only A, K, Q, J. A is worth 4 points, K is 3 points, Q is 2 points, and J is 1 point. The letters of the input string not necessarily uppercase.
"""


def hand_score(hand):
    hand_uppercase = hand.upper()
    card_score_dict = {"A": 4, "K": 3, "Q": 2, "J": 1}
    card_total = 0
    for each_card in hand_uppercase:
        if each_card in card_score_dict.keys():
            card_total = card_total + card_score_dict[each_card]
    return card_total


print(hand_score("AQAJ"))  # => 11
print(hand_score("jJka"))  # => 9
