import string
import wget

class TextContainer():

    def _init_(self, text):
        self.text = text

    def count_words(self):
        return len(self.text.split(" "))
        
    def count_chars(self, text):
        return len(self.text)
    
    def count_letters(self, text):
        count = 0
        for letter in text:
            if letter in string.ascii_letters:
                count += 1
        return count

t = TextContainer()

bones_in_london_url = 'http://www.gutenberg.org/cache/epub/27525/pg27525.txt'
wget.download(bones_in_london_url,'bones_in_london.txt')
with open('./bones_in_london.txt') as f:
    t.count_chars(f)
