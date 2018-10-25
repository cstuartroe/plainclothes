import os

corpus_filepath = os.path.join(os.path.dirname(__file__),'../sources/corpus.txt')

with open(corpus_filepath,'r') as fh:
    corpus = fh.read()

def get_ngrams(n):
    ngrams = {}
    for i in range(0,len(corpus)-n):
        ngram = corpus[i:i+n]
        ngrams[ngram] = ngrams.get(ngram,0) + 1

    l = sorted(list(ngrams.items()), key = lambda pair: pair[1], reverse=True)
    lines = ["%s\t%d" % pair for pair in l]

    ngrams_dir = os.path.join(os.path.dirname(__file__),'ngrams')
    if not os.path.isdir(ngrams_dir):
        os.makedirs(ngrams_dir)
    with open(os.path.join(ngrams_dir,"%dgrams.txt" % n), "w") as fh:
        fh.write("\n".join(lines))

    if n != 1:
        get_ngrams(n-1)
