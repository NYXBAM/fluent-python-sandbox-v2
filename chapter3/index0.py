import re 
import sys 

WORD_RE = re.compile(r'\w+')

index = {}

with open(sys.argv[1], 'r') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
            
for word in sorted(index, key=str.upper):
    print(word, index[word])
    
'''
AMAZING [(3, 14)]
book [(3, 6)]
great [(2, 10)]
Hello [(1, 1)]
is [(2, 7), (3, 11)]
This [(3, 1)]
world [(1, 7)]
World [(2, 1)]
'''