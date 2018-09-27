from ngrams import *
from included import *
from dicthelper import *

import math
from bitstring import BitArray
from random import random, randrange

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
        
    def prob(self, gram, discount):
        n = len(gram)
        if n == 1:
            occurrence = self.gram_counts.get(gram,0)/self.gram_counts['']
            return occurrence
            
        else:
            context = gram[:-1]
            if context in self.gram_counts:
                pkn = max(self.gram_counts.get(gram,0) - discount, 0)/self.gram_counts[context]
                lambdaw = (discount*self.unique_continuations.get(context,0)/self.gram_counts[context])
            else:
                pkn = 0
                lambdaw = 1
            prob = pkn + (lambdaw * self.prob(gram[1:],discount))
            return prob

    def model(self, context, discount=.75):
        grams = [context + ch for ch in included_chs]
        probs = [self.prob(gram,discount) for gram in grams]
        return self.normalize(probs,20)

    def normalize(sel,probs,bits):
        probs = [prob + (2**-bits) for prob in probs]
        s = sum(probs)
        probs = [prob/s for prob in probs]
        
        tokens_left = 2**bits
        prob_left = sum(probs)
        discrete_probs = []
        for prob in probs:
            discrete_prob = round(prob*tokens_left/prob_left)
            tokens_left -= discrete_prob
            prob_left -= prob
            discrete_probs.append(discrete_prob)
        assert(tokens_left == 0)
        assert(sum(discrete_probs) == 2**bits)
        return [BitArray('uint:%d=%d' % (bits, discrete_prob)) for discrete_prob in discrete_probs]

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
            entropy += -math.log2(self.prob(gram, discount))
        return entropy / (len(test_corpus) - gram_size + 1)

lm = LanguageModel(ngrams)

def model(context):
    return lm.model(context)

def test_perplexity(gram_size):
    with open('test.txt','r') as fh:
        test_corpus = fh.read()
    return lm.perplexity(test_corpus,gram_size,.75)

def generate(seed,l):
    context = seed
    out = ''
    for i in range(l):
        roll = randrange(2**20)
        probs = model(context)
        cum_prob = 0
        j = -1
        while cum_prob < roll:
            j += 1
            cum_prob += probs[j].uint
        out += included_chs[j]
        context = context[1:] + included_chs[j]
    return out

print(generate('ers. ',1000))
print(test_perplexity(6))
