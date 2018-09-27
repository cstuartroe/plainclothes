from collector import *
from dicthelper import *  

with open('corpus.txt','r') as fh:
    corpus = fh.read()

max_n = 6
ngrams = {}

ngrams[''] = len(corpus)
for n in range(1,max_n+1):
    for i in range(0,len(corpus)-n+1):
        increment_or_create(ngrams,corpus[i:i+n])

ngrams = sort_by_value(ngrams)

with open('ngrams.py','w') as fh:
    fh.write('ngrams = ' + pretty_dict(ngrams,8))
