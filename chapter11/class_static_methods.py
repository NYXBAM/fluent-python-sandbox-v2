class Demo:
    @classmethod
    def klassmeth(*args):
        return args
    
    @staticmethod
    def statmeth(*args):
        return args
    
print(Demo.klassmeth()) # (<class '__main__.Demo'>,)
print(Demo.klassmeth('Spam')) # (<class '__main__.Demo'>, 'Spam')
print(Demo.statmeth()) # ()
print(Demo.statmeth('Spam')) # ('Spam',)