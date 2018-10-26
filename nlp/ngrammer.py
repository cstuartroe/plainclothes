import os

corpus_filepath = os.path.join(os.path.dirname(__file__),'../sources/corpus.txt')
with open(corpus_filepath,'r') as fh:
    corpus = fh.read()
corpus = corpus.replace("\n","```")

def compute_ngrams(n,recursive=False):    
    if n == 0:
        return
    print("Computing %dgrams..." % n)
    
    ngrams = {"CORPUS_LENGTH":len(corpus)}
    for i in range(0,len(corpus)-n):
        ngram = corpus[i:i+n]
        ngrams[ngram] = ngrams.get(ngram,0) + 1

    l = list(ngrams.items()) #sorted(list(ngrams.items()), key = lambda pair: pair[1], reverse=True)
    lines = ["%s\t%d" % pair for pair in l]

    ngrams_dir = os.path.join(os.path.dirname(__file__),'ngrams')
    if not os.path.isdir(ngrams_dir):
        os.makedirs(ngrams_dir)
    with open(os.path.join(ngrams_dir,"%dgrams.txt" % n), "w") as fh:
        fh.write("\n".join(lines))

    if recursive:
        compute_ngrams(n-1)

def load_ngrams(n):    
    ngrams = {}
    ngrams_dir = os.path.join(os.path.dirname(__file__),'ngrams')
    try:
        with open(os.path.join(ngrams_dir,"%dgrams.txt" % n), "r") as fh:
            lines = fh.read().split("\n")
    except FileNotFoundError:
        compute_ngrams(n)
        return load_ngrams(n)
    
    print("Loading %dgrams..." % n)
    for line in lines:
        ngram, count = line.split("\t")
        ngrams[ngram] = int(count)
    return ngrams
