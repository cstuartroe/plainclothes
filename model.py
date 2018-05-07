from ngrams import *
from included import *
from dicthelper import *
import math
from random import randrange

##def model(context):
##    assert(all(ch in included_chs for ch in context))
##    grams = [context + ch for ch in included_chs]
##    counts = [ngrams.get(gram,0) + 1 for gram in grams]
##    s = sum(counts)
##    probs = list(map(lambda x: x/s, counts))
##    return probs

class LanguageModel:
    def __init__(self, gram_counts):
            
        self.gram_counts = gram_counts
        self.unique_grams = {}
        self.unique_continuations = {}
        for gram in self.gram_counts.keys():
            increment_or_create(self.unique_grams,len(gram))
            if len(gram)>1:
                increment_or_create(self.unique_continuations,gram[:-1])
        self.unique_continuations = sort_by_value(self.unique_continuations)

##        print(self.gram_counts)
##        print(self.unique_continuations)
##        print(self.unique_grams)
        
    def model(self, gram, discount):
##        print(gram)
        n = len(gram)
        if n == 1:
            occurrence = self.gram_counts.get(gram,0)/self.gram_counts['']
##            print(occurrence)
            return occurrence
            
        else:
            context = gram[:-1]
            if context in self.gram_counts:
                pkn = max(self.gram_counts.get(gram,0) - discount, 0)/self.gram_counts[context]
                lambdaw = (discount*self.unique_continuations.get(context,0)/self.gram_counts[context])
            else:
                pkn = 0
                lambdaw = 1
##            print(pkn)
##            print(lambdaw)
            prob = pkn + (lambdaw * self.model(gram[1:],discount))
            prob = round(prob,10)
            return prob if prob != 0 else 1e-10

    def suite(self, context, discount):
        suite = {}
        for letter in included_chs:
            suite[letter] = self.model(context + letter, discount)
        return sort_by_value(suite)

    def test(self, gram_size, discount):
        for context in self.gram_counts.keys():
            if len(context) == gram_size  - 1:
                prob_sum = sum([self.model(context + letter, discount) for letter in included_chs])
                try:
                    assert(round(prob_sum,5) == 1)
                except AssertionError:
                    raise ValueError('Context "%s" has continuation probability sum %f.' % (context, prob_sum))

    def perplexity(self, test_corpus, gram_size, discount):
        entropy = 0
        for i in range(len(test_corpus) - gram_size + 1):
            gram = test_corpus[i:i+gram_size]
            entropy += -math.log2(self.model(gram, discount))
        return entropy / (len(test_corpus) - gram_size + 1)

lm = LanguageModel(ngrams)

def model(context):
    grams = [context + ch for ch in included_chs]
    probs = [lm.model(gram,.75) for gram in grams]
    assert(round(sum(probs),5) == 1)
    return probs

##with open('test.txt','r') as fh:
##    test_corpus = fh.read()
##x = lm.perplexity(test_corpus,6,.75)
