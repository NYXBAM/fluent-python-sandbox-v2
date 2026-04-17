import re
import reprlib

import pytest

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):
        return len(self.words)
    
    def __iter__(self):
        # to avoid Mypy error 
        return iter(self.words)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
s = Sentence('"The time has come," the Walrus said')
print(s) # Sentence('"The time ha...e Walrus said')
for word in s:  # mypy error: s has no attribute __iter__
    print(word)
    
"""
The
time
has
come
the
Walrus
said
"""

print(list(s)) # ['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']






# some simple testing cases (not from book)
def test_sentence():
    s = Sentence("Hello world")
    out = ["Hello", "world"]
    assert list(s) == out
    
def test_invalid_sentence():
    s = Sentence("Hello")
    inv_out = ['Helo', "hello"]
    assert list(s) != inv_out
    
def test_not_str():
    with pytest.raises(TypeError):
        s = Sentence(1, 2, 3, 4, 5, 6)
    


