#from collector import *

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
