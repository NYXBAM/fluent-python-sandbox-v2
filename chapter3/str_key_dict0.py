class StrKeyDict0(dict):
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
    
    
    
d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])      # Output: two
print(d[4])        # Output: four   
print(d.get('3', 'N/A'))  # Output: N/A
print(2 in d)     # Output: True
print(3 in d)     # Output: False
print('4' in d)   # Output: True


