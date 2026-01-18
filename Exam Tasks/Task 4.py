
"""
Task 4

This script builds the word "world" from a list, then swaps it with "hello",
capitalises both words, converts them to uppercase, and prints them with a divider.
"""

world = ["d", "l", "r", "o", "w"]
hello = "hello"

"""
This function reverses the list from world with a loop and returns the word"
"""
def reverse_word(letter_list):
    rslt = ""
    for lttr in letter_list:
        rslt = lttr + rslt
    return rslt

world_word = reverse_word(world)

# This capitalises both words
two_words = (hello + " " + world_word).title()

# This swaps the two words and then converts them to uppercase
w1, w2 = two_words.split()
print("Hello World")
print("-" * 60)
print((w2 + " | " + w1).upper())