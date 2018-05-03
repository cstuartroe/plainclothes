#from collector import *
from ngrams import *

def pretty_dict(dictionary, wrap_length):
    keys = list(dictionary.keys())
    lines = []
    
    for i in range(len(keys)//wrap_length+1):
        try:
            line = ["%s: %s, " % (repr(key),repr(dictionary[key])) for key in keys[wrap_length*i:wrap_length*i+wrap_length]]
            lines.append(''.join(line))
        except IndexError:
            line = ["%s: %s, " % (repr(key),repr(dictionary[key])) for key in keys[wrap_length*i:]]
            lines.append(''.join(line))
    return '{' + '\n'.join(lines) + '}'

with open('corpus.txt','r') as fh:
    corpus = fh.read()

n = 5
ngrams = {}

for i in range(0,len(corpus)-n):
    try:
        ngrams[corpus[i:i+n]] += 1
    except KeyError:
        ngrams[corpus[i:i+n]] = 1

ngrams = dict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))

with open('ngrams.py','w') as fh:
    fh.write('ngrams = ' + pretty_dict(ngrams,8))
