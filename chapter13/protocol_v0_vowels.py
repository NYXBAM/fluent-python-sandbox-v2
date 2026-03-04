class Vowels:
    def __getitem__(self, i):
        return 'AEIOU'[i]
    
    
v = Vowels()
print(v[0]) # A 
print(v[-1]) # U
