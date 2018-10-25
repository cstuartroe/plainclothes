class Shantree:
    def __init__(self, probs, codes=None):
        assert(probs == sorted(probs))
        i = 0
        cum_prob = 0
        total = sum(probs)
        assert(total <= 1.000001)
##        print(total)
        
        if codes:
            self.codes = codes
        else:
            self.codes = ['']*len(probs)
        assert(len(self.codes) == len(probs))

        while cum_prob + probs[i]/2 < total/2:
            try:
                probs[i+1]
            except IndexError:
                print(cum_prob,total,probs,i)
                print(total/2 - (cum_prob + probs[i]/2))
                raise IndexError()
            cum_prob += probs[i]
            i += 1
            
        self.breakpt = i

        for i in range(self.breakpt):
            self.codes[i] += '0'
        for i in range(self.breakpt, len(self.codes)):
            self.codes[i] += '1'

        if self.breakpt != 1:
            self.codes[:self.breakpt] = Shantree(probs[:self.breakpt],codes=self.codes[:self.breakpt]).codes
        if self.breakpt != len(self.codes) - 1:
            self.codes[self.breakpt:] = Shantree(probs[self.breakpt:],codes=self.codes[self.breakpt:]).codes

def reverse_perm(permutation):
    l = [0]*len(permutation)
    for i in range(len(permutation)):
        l[permutation[i]] = i
    return l

class Shancode:
    def __init__(self,probs):
        try:
            assert(round(sum(probs),3) == 1)
        except AssertionError:
            raise ValueError('The sum of given probabilities is %f.' % sum(probs))
        
        p = sorted(list(range(len(probs))), key=lambda i: probs[i])
        r = reverse_perm(p)
        s = sorted(probs)
        st = Shantree(s)
        self.codes = [st.codes[i] for i in r]
        self.efficiency = sum([probs[i] * len(self.codes[i]) for i in range(len(probs))])
