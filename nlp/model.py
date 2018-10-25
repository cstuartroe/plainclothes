import math
from bitstring import BitArray
from random import random, randrange

from readers.reader import included_chs
from . import ngrammer

class NgramModel:
    charset = included_chs + "`"
    
    def __init__(self, gram_size):
        self.gram_size = gram_size
        self.gram_counts = {}
        for n in range(gram_size):
            self.gram_counts.update(ngrammer.load_ngrams(n+1))
        self.corpus_length = self.gram_counts["CORPUS_LENGTH"]
        self.unique_grams = 0
        self.unique_continuations = {}
        self.bits = 20
        for gram in self.gram_counts.keys():
            self.unique_grams += 1
            if len(gram)>1:
                self.unique_continuations[gram[:-1]] = self.unique_continuations.get(gram[:-1],0)+1
        
    def prob(self, gram, discount):
        n = len(gram)
        if n == 1:
            occurrence = self.gram_counts.get(gram,0)/self.corpus_length
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
        grams = [context + ch for ch in NgramModel.charset]
        probs = [self.prob(gram,discount) for gram in grams]
        return self.normalize(probs,self.bits)

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
        for letter in NgramModel.charset:
            suite[letter] = self.model(context + letter, discount)
        return suite

    def test(self, gram_size, discount):
        for context in self.gram_counts.keys():
            if len(context) == gram_size  - 1:
                prob_sum = sum([self.model(context + letter, discount) for letter in NgramModel.charset])
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

    def generate(self,length):
        context = "`"*self.gram_size
        out = ''
        for i in range(length):
            roll = randrange(2**self.bits)
            probs = self.model(context)
            cum_prob = 0
            j = -1
            while cum_prob < roll:
                j += 1
                cum_prob += probs[j].uint
            out += NgramModel.charset[j]
            context = context[1:] + NgramModel.charset[j]
        return out
