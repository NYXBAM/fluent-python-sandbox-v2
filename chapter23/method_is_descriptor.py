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
