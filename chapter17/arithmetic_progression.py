

class ArithmeticProgression:
    
    def __init__(self, begin, step, end=None):
        self.begin = begin 
        self.step = step
        self.end = end 
        
    def __iter__(self):
        result_type = type(self.begin + self.step)
        result = result_type(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index
            


# But easiest way use generator func
def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None 
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index
        

# USING itertools 
import itertools 

def aritprog_gen_v2(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is None:
        return ap_gen
    
    return itertools.takewhile(lambda n: n < end, ap_gen)
    

            
ap = ArithmeticProgression(0, 1, 5)
print(list(ap)) # [0, 1, 2, 3, 4]

ap = ArithmeticProgression(1, .5, 3)
print(list(ap)) # [1.0, 1.5, 2.0, 2.5]


ap = ArithmeticProgression(0, 1/3, 3)
print(list(ap))  # [0.0, 0.3333333333333333, 0.6666666666666666, 1.0, 1.3333333333333333, 1.6666666666666665, 2.0, 2.333333333333333, 2.6666666666666665]

from fractions import Fraction

ap = ArithmeticProgression(0, Fraction(1,3), 1)
print(list(ap)) # [Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]

