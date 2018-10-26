import math
import random

from readers.reader import included_chs
from . import ngrammer

class LanguageModel:
    charset = included_chs + "`"

    # to override: __init__(self), model(self), update_state(self,char)
    # update_state() updates state by adding a new character
    # model() gets an array of character predictions based on current state

    def put_char(self,char):
        try:
            assert(type(char)==str)
            assert(len(char)==1)
        except AssertionError:
            raise ValueError("LanguageModel.put_char(char) must be given a single character")
        self.update_state(char)

    def perplexitys(self, test_string, gram_size, discount):
        entropy = 0
        for i in range(len(test_string) - gram_size + 1):
            gram = test_string[i:i+gram_size]
            entropy += -math.log2(self.prob(gram, discount))
        return entropy / (len(test_string) - gram_size + 1)

    def generate(self,length):
        starting_context = "`````````` "
        out = ''
        
        for char in starting_context:
            self.put_char(char)
            
        for i in range(length):
            probs = self.get_probs()
            roll = random.random()
            cum_prob = 0
            j = -1
            while cum_prob < roll:
                j += 1
                cum_prob += probs[j]
            next_char = NgramModel.charset[j]
            out += next_char
            self.put_char(next_char)
            
        return out

    def get_probs(self):
        probs = self.model()
        s = sum(probs)
        probs = [prob/s for prob in probs]
        return probs
    
class NgramModel(LanguageModel):    
    def __init__(self, gram_size, _discount = .75):
        self.gram_size = gram_size
        self.gram_counts = {}
        self.unique_grams = {}
        self.unique_continuations = {}
        self.discount = _discount
        self.context = ""
        
        for n in range(gram_size):
            grams = ngrammer.load_ngrams(n+1)
            self.gram_counts.update(grams)
            self.unique_grams[n+1] = len(grams)
        
        self.corpus_length = self.gram_counts["CORPUS_LENGTH"]
        
        for gram in self.gram_counts.keys():
            if len(gram)>1:
                context = gram[:-1]
                self.unique_continuations[context] = self.unique_continuations.get(context,0) + 1

    def update_state(self, char):
        self.context += char
        if len(self.context) > self.gram_size-1:
            self.context = self.context[-self.gram_size+1:]

    def model(self):
        grams = [self.context + char for char in LanguageModel.charset]
        probs = [self.prob(gram) for gram in grams]
        return probs

    # Kneser-Ney smoothed ngram probability
    def prob(self, gram):
        n = len(gram)
        if n == 1:
            occurrence = self.gram_counts.get(gram,0)/self.corpus_length
            return occurrence
        else:
            context = gram[:-1]
            if context in self.gram_counts:
                pkn = max(self.gram_counts.get(gram,0) - self.discount, 0)/self.gram_counts[context]
                lambdaw = (self.discount*self.unique_continuations.get(context,0)/self.gram_counts[context])
            else:
                pkn = 0
                lambdaw = 1
            prob = pkn + (lambdaw * self.prob(gram[1:]))
            return prob
