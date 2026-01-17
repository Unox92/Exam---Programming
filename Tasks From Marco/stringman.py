class sentence:
    def __init__(self, text, delimiter):
        self.text = text
        self.delimiter = delimiter
    
    def strLength(self):
        length = len(self.text)
        print(f"The length of the string is {length}")
        return length
    
    def cutString(self):
        return self.text.split(self.delimiter)
    
    def showWordAt(self, word_list, index):
        if 0 <= index < len(word_list):
            print(f"The word at index {index} is {word_list[index]}")
        else:
            print("Index out of range")
    
    def showIndexAt(self, word_list, word):
        if word in word_list:
            index = word_list.index(word)
            print(f"The index for the word {word} is {index}")
        else:
            print(f"Word '{word}' not found")