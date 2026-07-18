import collections


class Text(collections.UserString):
    def __repr__(self):
        return "Text({!r})".format(self.data)

    def reverse(self):
        return self[::-1]


word = Text("forward")
print(word)  # forward
print(word.reverse())  # drawrof
print(Text.reverse(Text("backward")))  # drawkcab

print(type(Text.reverse), type(word.reverse))  # <class 'function'> <class 'method'>

print(
    list(map(Text.reverse, ["repaid", (10, 20, 30), Text("stressed")]))
)  # ['diaper', (30, 20, 10), Text('desserts')]

print(Text.reverse.__get__(word)) # <bound method Text.reverse of Text('forward')>
print(Text.reverse.__get__(None, Text)) # <function Text.reverse at 0x100bb72e0>
print(word.reverse) # <bound method Text.reverse of Text('forward')>
print(word.reverse.__self__) # forward
print(word.reverse.__func__ is Text.reverse) # True
