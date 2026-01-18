
"""
For this task I need to create two files, one called stringman.py and one called main.py
"""

"""
_init_ function handles the string operations, and stores the string

"""
class StringMan:
    """
    _init_ function handles the string operations, and stores the string
    """

    def __init__(self, text, delimiter):
        self.text = text
        self.delimiter = delimiter

    """
    length_of_str prints the length of the string
    """
    def length_of_str(self):
        print("The length of the string is", len(self.text))

    """
    str_split splits the string and returns a list
    """
    def str_split(self):
        return self.text.split(self.delimiter)

    """
    show_word prints the word at the index
    """
    def show_word(self, word_list, index):
        print("The word at index", index, "is", word_list[index])

    """
    show_index prints the index of the word given by the user
    """
    def show_index(self, word):
        words = self.str_split()
        print("The index of the word", word, "is", words.index(word))