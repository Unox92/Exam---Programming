
"""
main.py

main.py demonstrates how to use the StringMan class from StringMan.py.
"""

from stringman import StringMan

# This creates an object with a string
text = input("Enter a sentence: ")
delimiter = " "
string_object = StringMan(text, delimiter)


# This prints the length of the string
string_object.length_of_str()


# This splits the string and stores the results
words = string_object.str_split()


# This prints the word at the index
string_object.show_word(words, 2)


# This prints the index of that word
string_object.show_index(words[2])