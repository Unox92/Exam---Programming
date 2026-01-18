
"""
main.py

This file demonstrates how to use the StringMan class from stringman.py.
"""

from stringman import StringMan

# Create an object with a string and a delimiter
text = "this is a simple string example"
delimiter = " "

string_object = StringMan(text, delimiter)

# Print the length of the string
string_object.length_of_str()

# Split the string and store the result
words = string_object.str_split()

# Print the word at a specific index
string_object.show_word(words, 2)

# Print the index of a specific word
string_object.show_index("simple")
